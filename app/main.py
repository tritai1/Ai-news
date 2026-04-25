from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import router SAU khi tạo app (tránh lỗi import vòng)
from app.api.routes import router
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Cho phép tất cả các nguồn (để test local)
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/api")
@app.get("/")
def root():
    return {"msg": "running"}