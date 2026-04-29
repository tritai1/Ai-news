from app.services.retriver import load_db
from app.services.LLM import get_llm
from langchain_community.chat_message_histories import ChatMessageHistory
from duckduckgo_search import DDGS
db = load_db() 
llm = get_llm()


chat_history = ChatMessageHistory() 

def get_internet_news(query: str):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(f"{query} tin tức mới nhất", max_results=5)
            context = ""
            sources = []
            for r in results:
                context += f"Nội dung: {r['body']}\n\n"
                sources.append({"title": r['title'], "link": r['href']})
            return context, sources
    except Exception as e:
        print(f"err sreaching: {e}")
        return "", []

def ask_rag(question: str):
    try:
        # Tìm kiếm tài liệu
        docs_and_scores = db.similarity_search_with_score(question, k=3)     
        
        realtime_keywords = ["hôm nay", "mới nhất", "vừa xong", "giá vàng", "thời tiết", "hiện tại"]
        is_realtime = any(word in question.lower() for word in realtime_keywords)

        context = ""
        sources = []

        if is_realtime:
            print("---LOOKING FOR REAL-TIME NEWS ONLINE ---")
            context, sources = get_internet_news(question)
        
        # Nếu không phải câu hỏi real-time HOẶC tìm trên mạng không thấy, quay lại dùng Database local
        if not context:
            docs_and_scores = db.similarity_search_with_score(question, k=3)
            filtered_docs = [d for d, score in docs_and_scores if score < 1.3]
            
            if filtered_docs:
                context = "\n\n".join([d.page_content[:500] for d in filtered_docs])
                sources = [{"title": d.metadata.get("title", "Local News"), "link": d.metadata.get("source", "#")} for d in filtered_docs]
        # print(f"\n--- DEBUG: CÁC ĐOẠN VĂN TÌM ĐƯỢC ---")
        # for i, (doc, score) in enumerate(docs_and_scores):
        #     print(f"Top {i+1} - Score: {score:.4f} - {doc.page_content[:50]}...")
        

        filtered_docs = [d for d, score in docs_and_scores if score < 1]

        greetings = ["hi", "hello", "chào", "xin chào", "hey", "tạm biệt", "bye"]
        is_greeting = any(word in question.lower() for word in greetings) and len(question.split()) < 5

        # Nếu KHÔNG PHẢI chào hỏi VÀ KHÔNG CÓ tài liệu -> Báo không biết (Chống bịa chuyện)
        if not is_greeting and not filtered_docs:
            return {
                "answer": "I don't know. This information isn't in my database.", 
                "sources": []
            }   

        # Chuẩn bị Context
        context = "\n\n".join([str(d.page_content[:500]) for d in filtered_docs])
         
        history_context = ""
    
        messages = chat_history.messages[-4:] 
        for msg in messages:
            prefix = "Human" if msg.type == "human" else "AI"
            history_context += f"{prefix}: {msg.content}\n"
         
        prompt = f"""
                You are a helpful and friendly News Assistant. 

                GENERAL RULES:
                - If the user greets you or asks about you (e.g., "Hi", "Who are you?"), respond politely and introduce yourself as a News Assistant.
                - Identify the language of the question and answer in that same language.
                - Use the History to keep the conversation natural.

                RAG RULES:
                - Use the following pieces of retrieved context to answer news-related questions. 
                - If the question is about "today" or "latest news", summarize the top news in the context.
                - If a question is about news but you don't know the answer based on the context, just say that you don't know, don't try to make up an answer.
                - Use the context below to provide a concise and accurate response.
                
                History:
                {history_context}
                
                Context:
                {context}

                Question: 
                {question}

                Answer:
            """


        try:
            response = llm.invoke(prompt)
            
            # Trích xuất nội dung văn bản
            answer_text = response.content if hasattr(response, 'content') else str(response)
            
            # CẬP NHẬT BỘ NHỚ: Lưu cả câu hỏi và câu trả lời vào chat_history
            chat_history.add_user_message(question)
            chat_history.add_ai_message(answer_text)
            
        except Exception as llm_error:
            print(f"call er LLM: {llm_error}")
            return {"answer": "connect err model AI.", "sources": []}

        return {
            "answer": answer_text.strip(),
            "sources": [
                {
                    "title": doc.metadata.get("title", "News"),
                    "link": doc.metadata.get("source", "#") 
                } for doc in filtered_docs
            ]
        }

    except Exception as e:
        print(f"err system in ask_rag: {e}")
        return {
            "answer": "err technical.",
            "sources": []
        }