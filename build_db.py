# build_db.py
from app.utils.loader import load_crawled_data
from app.services.retriver import build_db

docs = load_crawled_data(r"D:\artical-ai-agent\data\news_data.json")

if docs:
    build_db(docs)
    print("Docs:", len(docs))
    print("DONE")
else:
    print("Không có tài liệu nào được tìm thấy để xử lý.")