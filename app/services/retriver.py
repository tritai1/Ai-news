# '''
# FAISS: thư viện để lưu vector và tìm kiếm similarity (Facebook AI)
# GoogleGenerativeAIEmbeddings: dùng Gemini để biến text → vector
# RecursiveCharacterTextSplitter: chia nhỏ văn bản
# os: lấy API key từ môi trường
# '''


# '''
# Dùng model: "embedding-001" của Gemini
# Mỗi đoạn text → 1 vector (dạng số)
# API key lấy từ biến môi trường (an toàn hơn hardcode)'''


# def get_embedding():
#     return GoogleGenerativeAIEmbeddings(
#         model="text-embedding-004",
#         google_api_key=os.getenv("GEMINI_API_KEY")
#     )


# def build_db(docs):
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50 # chia nho du lieu moi doan 500 ki tu va chong lan 50 ki tu
#     )
#     #chia nho cac doc ra nhieu doan hơn
#     split_docs = splitter.split_documents(docs)

#     embeddings = get_embedding() # bien giu lieu về vector
#     db = FAISS.from_documents(split_docs, embeddings) # dung Fass de luu lai tat cả các vector

#     db.save_local(DB_PATH)

# '''
# Load lại vector DB đã lưu
# allow_dangerous_deserialization=True:
# Cho phép load object pickle
# chỉ dùng khi bạn tin tưởng dữ liệu
# '''

# def load_db():
#     embeddings = get_embedding()
#     return FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

DB_PATH = r"D:\artical-ai-agent\vector_db"

#  dùng embedding local (ổn định, free 100%)
def get_embedding():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def build_db(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    split_docs = splitter.split_documents(docs)
    print(split_docs)
    embeddings = get_embedding()

    db = FAISS.from_documents(split_docs, embeddings)

    db.save_local(DB_PATH)


def load_db():
    embeddings = get_embedding()
    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
