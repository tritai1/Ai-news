import json
import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

# 1. Khởi tạo model Embedding 
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def load_crawled_data(file_path=r"D:\artical-ai-agent\data\news_data.json"):
    if not os.path.exists(file_path):
        print(f"Lỗi: Không tìm thấy file {file_path}")
        return
    
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Lỗi: File JSON không đúng định dạng.")
            return
    
    documents = []
    for item in data:
        # Kiểm tra các trường dữ liệu có tồn tại trong item không
        title = item.get('title', 'Không có tiêu đề')
        content = item.get('content', '')
        link = item.get('link', 'Unknown')
        
        if content: 
            doc = Document(
                page_content=f"Tiêu đề: {title}\nNội dung: {content}",
                metadata={"source": link, "title": title}
            )
            documents.append(doc)
    
    if documents:
        # 2. Tạo và Lưu vào database FAISS
        db = FAISS.from_documents(documents, embeddings)
        db.save_local("faiss_index")
        print(f"Đã nạp thành công {len(documents)} tin tức vào faiss_index")
        return documents  
    else:
        print("Không có dữ liệu để nạp.")
        return []

if __name__ == "__main__":
    load_crawled_data()