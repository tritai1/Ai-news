from fastapi import APIRouter
from app.core.rag import ask_rag
from app.model.schema import QueryRequest, QueryResponse

router = APIRouter()

@router.post("/ask", response_model=QueryResponse)
def ask(req: QueryRequest): # Chỗ này dùng QueryRequest để lấy câu hỏi từ người dùng
    return ask_rag(req.question)