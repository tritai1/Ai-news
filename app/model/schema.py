from pydantic import BaseModel
from typing import List

# 1. Schema cho dữ liệu người dùng gửi lên
class QueryRequest(BaseModel):
    question: str

# 2. Schema cho từng nguồn tin trả về (Dùng trong QueryResponse)
class SourceItem(BaseModel):
    title: str
    link: str

# 3. Schema cho toàn bộ phản hồi của API
class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceItem] # Danh sách các Object chứa title và link