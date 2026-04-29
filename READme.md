<img width="569" height="553" alt="image" src="https://github.com/user-attachments/assets/93d4eec9-8522-40d1-b9c7-59fb925cd231" />
# Artical AI Agent

Một ứng dụng RAG (Retrieval-Augmented Generation) nhỏ giúp truy vấn dữ liệu báo/khóa học bằng cách dùng FAISS làm vector DB và một LLM để sinh phản hồi.

## Mô tả

<img width="569" height="553" alt="image" src="https://github.com/user-attachments/assets/ac5483b4-4fb1-4379-bbe7-fa35a9b4331d" />
** RAG (Retrieval-Augmented Generation)
   - Thế hệ tăng cường truy xuất (RAG) đã chuyển từ một khái niệm mới lạ thành tiêu chuẩn tối ưu để tạo ra các ứng dụng AI thông minh, đáng tin cậy và sẵn sàng cho sản xuất.
   - RAG là yếu tố phân biệt các mô hình lạc hậu với các giải pháp tiên tiến. Nó tăng cường sức mạnh cho các mô hình LLM bằng cách kết nối chúng với các nguồn dữ liệu bên ngoài, thời gian thực, cho phép phản hồi chính xác, giàu ngữ cảnh mà không cần chu kỳ tinh chỉnh liên tục.
   - RAG tác nhân: RAG thông thường thực hiện một lần truy xuất cho mỗi truy vấn. Một hệ thống tác nhân có thể định dạng lại truy vấn, tìm kiếm nhiều lần, hợp nhất kết quả hoặc quyết định rằng nó không cần truy xuất gì cả. Bài thực hành này mô phỏng vòng lặp quyết định đó bằng Python thuần túy.
** Chunking
   - Token có độ dài cố định: Phương pháp cổ điển (ví dụ: 512–1024 token) vẫn là một nền tảng vững chắc.
** Embeddings
   - Các embedding chuyển đổi tài liệu và truy vấn của bạn thành các biểu diễn vector phong phú, tạo nên nền tảng của tìm kiếm ngữ nghĩa. Mô hình embedding phù hợp là vô cùng quan trọng. chúng tôi sử dụng embeding dưới dạng model
** Retrieval Tool
   - FAISS: Dành cho tìm kiếm tương đồng siêu nhanh, được tăng tốc bằng GPU.
     <img width="1280" height="330" alt="image" src="https://github.com/user-attachments/assets/a9fd2386-5567-4fb2-bf77-35e8bc17d7b6" />
** LLMs for Generation
   - Mistral & Mixtral: Nhẹ và hiệu năng cao, lý tưởng cho các trường hợp đặc biệt và các tác vụ nhạy cảm về tốc độ.
** Query Optimization
   - Cách bạn hiểu truy vấn của người dùng và cấu trúc lời nhắc sẽ ảnh hưởng trực tiếp đến chất lượng của kết quả cuối cùng.
** Prompt Engineering Methods
   - Tự hỏi/Phản ứng: Trao quyền cho mô hình thực hiện suy luận đa bước để trả lời các câu hỏi phức tạp.
     
<img width="894" height="73" alt="image" src="https://github.com/user-attachments/assets/46f719a0-4867-4e97-a828-fb26828feac8" />


`artical-ai-agent` là một prototype cho pipeline RAG: thu thập dữ liệu, chunking, tạo embeddings, lưu vào FAISS index, và trả lời truy vấn bằng cách lấy ngữ cảnh từ vector DB rồi gọi LLM để tổng hợp.

## Tính năng chính

- Chuẩn hoá và tải dữ liệu bài báo (hoặc dữ liệu văn bản) từ `data/`.
- Xây dựng / sử dụng FAISS index ở `faiss_index/index.faiss` và `vector_db/index.faiss`.
- Module RAG trung tâm (`app/core/rag.py`) kết hợp retrieval + generation.
- API đơn giản nằm trong `app/api/routes.py` và một frontend mẫu `app/frontEnd/index.html`.

## Yêu cầu

- Python 3.13
- Các thư viện trong `requirements.txt` hoặc môi trường ảo trong `rag_env`.

## Cài đặt nhanh

1. Tạo và kích hoạt môi trường ảo (Windows PowerShell):

```
python -m venv rag_env
.\n+rag_env\Scripts\Activate.ps1
```

2. Cài đặt phụ thuộc:

```
pip install -r requirements.txt
```

3. (Tuỳ chọn) Nếu đã có file index FAISS trong `faiss_index/index.faiss` hoặc `vector_db/index.faiss`, có thể bỏ qua bước build index.

## Chạy ứng dụng

Chạy API / backend:

```
python app/main.py
```

Sau khi chạy, mở `app/frontEnd/index.html` trong trình duyệt hoặc gọi endpoint API phù hợp để thử nghiệm.

## Cấu trúc thư mục (tóm tắt)

- `app/` - mã nguồn chính (API, core RAG, frontend mẫu).
- `data/` - mã nguồn/đầu vào dữ liệu, script thu thập.
- `faiss_index/` - index FAISS đã lưu.
- `vector_db/` - bản sao/backup của index vector nếu có.
- `rag_env/` - môi trường ảo (không bắt buộc commit).

## Ghi chú về dữ liệu & index

- Nếu muốn rebuild index: chạy script trong `app/utils/loader.py` hoặc `build_db.py` để tạo embeddings và lưu FAISS index.
- Đảm bảo có đủ bộ nhớ khi xây index lớn; FAISS có các chế độ index khác nhau phù hợp cho dataset lớn.

## Phát triển

- Thêm dữ liệu vào `data/` rồi chạy pipeline tạo embeddings.
- Kiểm thử endpoint API bằng `curl` hoặc Postman.

## Liên hệ

Nếu cần trợ giúp, mở issue hoặc liên hệ trực tiếp với tác giả dự án.

## Chi tiết kỹ thuật

Dưới đây là phần mô tả chi tiết các kỹ thuật và lựa chọn kiến trúc được sử dụng (và các tuỳ chọn khuyến nghị) cho dự án RAG này.

- **Tiền xử lý (Preprocessing):**
	- Chuẩn hoá encoding (UTF-8), loại bỏ ký tự thừa, chuẩn hoá unicode.
	- Loại bỏ HTML, metadata không cần thiết, và normalise dấu câu.
	- Tách câu/token tuỳ theo ngôn ngữ (Việt Nam cần xử lý dấu, phân tách từ bằng các thư viện như `pyvi` hay `underthesea` nếu cần).

- **Chunking / phân đoạn văn bản:**
  - <img width="1004" height="482" alt="image" src="https://github.com/user-attachments/assets/3673141b-be27-4b49-bfcb-464dbe083b67" />
	- Cắt tài liệu thành các đoạn (chunks) theo kích thước cố định (ví dụ ~500–1000 token) hoặc theo ranh giới câu.
	- Sử dụng overlap (20–30%) giữa các chunk để giữ ngữ cảnh khi truy hồi.
	- Lưu metadata (tên file, vị trí offset, title, date) để hiện nguồn trích dẫn khi trả lời.

- **Embeddings (mã hoá vector):**
  - <img width="1204" height="444" alt="image" src="https://github.com/user-attachments/assets/22830d4d-b84d-46b0-b744-b4cf256603cc" />
	- Dùng model embedding phù hợp (ví dụ các model transformer nhỏ hoặc dịch vụ embedding như OpenAI/Anthropic tùy cấu hình).
	- Batch hoá việc tạo embedding để tối ưu tốc độ và hạn chế latency.
	- Thông thường chuẩn hoá vector (L2-normalize) trước khi lưu để cải thiện truy vấn theo cosine similarity.

- **FAISS / chỉ mục vector:**
  - <img width="1126" height="1166" alt="image" src="https://github.com/user-attachments/assets/c4dd0877-5f32-486c-beea-146a3f11ba46" />
	- Hỗ trợ nhiều loại index: `Flat` (tìm chính xác, tốt cho dataset nhỏ), `IVF`, `HNSW`, hoặc `PQ` (nén) cho tập lớn.
	- Tham số quan trọng: `nlist` (số cluster cho IVF), `nprobe` (số cluster truy vấn), hoặc `efConstruction/efSearch` cho HNSW.
	- Nếu cần throughput cao, cân nhắc chạy FAISS trên GPU (nếu phần cứng cho phép).

- **Chiến lược truy hồi (Retrieval):**
	- Truy vấn k-NN trên vector (k = 3..10 tuỳ nhu cầu) để lấy các đoạn có liên quan.
	- (Tuỳ chọn) Kết hợp hybrid retrieval: BM25 (sparse) + dense embeddings để tăng độ chính xác tìm kiếm thông tin thực tế.
	- Reranking: sau khi lấy top-k, dùng một model nhẹ (cross-encoder) để sắp xếp lại kết quả nếu cần độ chính xác cao hơn.

- **LLM & Prompting (Generation):**
  - <img width="896" height="330" alt="image" src="https://github.com/user-attachments/assets/3ecc4c82-0da7-4102-a378-04eaaffa162a" />
  - <img width="942" height="520" alt="image" src="https://github.com/user-attachments/assets/38dbb641-e419-44d4-934a-dee0dea74d17" />
	- Ghép các đoạn được truy xuất vào prompt theo template: context + instruction + question.
    <img width="1420" height="330" alt="image" src="https://github.com/user-attachments/assets/fe72ba27-e73a-44b2-b210-0bec2061121f" />
	- Giới hạn tổng tokens trong prompt theo hạn mức context window của LLM; ưu tiên các đoạn có điểm tương đồng cao nhất.
    <img width="2742" height="1242" alt="image" src="https://github.com/user-attachments/assets/4a3da59b-9edb-4c61-932e-bfbcdb61dd1d" />
	- Sử dụng temperature thấp (0–0.7) cho câu trả lời chính xác; điều chỉnh `max_tokens` để kiểm soát độ dài trả lời.
	- Luôn yêu cầu LLM trích dẫn nguồn (file/offset) nếu dự án cần provenance.
    <img width="2404" height="558" alt="image" src="https://github.com/user-attachments/assets/f6f529d7-a8b2-4b93-859f-369fd4370e74" />

- **Chiến lược trả lời an toàn & chính xác:**
	- Nếu thông tin không rõ ràng trong context, trả lời với trạng thái không có đủ thông tin thay vì bịa đặt.
	- Sử dụng flag kiểm tra confidence (ví dụ điểm similarity threshold) để quyết định trả lời hay yêu cầu người dùng cung cấp thêm thông tin.

- **Cập nhật index & xử lý dữ liệu mới:**
	- Hỗ trợ rebuild toàn bộ index bằng `build_db.py` hoặc chạy pipeline trong `app/utils/loader.py`.
	- Với dữ liệu lớn, ưu tiên incremental indexing: tạo embeddings mới rồi thêm vào index (với FAISS dạng hỗ trợ add).

- **Hiệu năng & triển khai:**
	- Batch requests tới embedding/LLM, cache embeddings cho tài liệu không thay đổi.
	- Đặt TTL/limit cho cache retrieval, theo dõi latency và throughput.

- **Bảo mật & quyền riêng tư:**
	- Trước khi index, loại bỏ hoặc ẩn thông tin nhạy cảm/PII.
	- Lưu ý chính sách chia sẻ dữ liệu nếu dùng dịch vụ embedding hoặc LLM bên thứ ba.

### Vị trí mã liên quan

- Pipeline tạo index: `build_db.py`, `app/utils/loader.py`.
- Retrieval: `app/services/retriver.py` (hoặc file tương đương trong `app/`).
- Core RAG logic: `app/core/rag.py`
- Gọi LLM / service wrapper: `app/services/LLM.py`.
- API routes: `app/api/routes.py`.



