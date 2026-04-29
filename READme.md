# Article AI Agent — RAG-powered News & Knowledge Assistant

Một ứng dụng **RAG (Retrieval-Augmented Generation)** giúp truy vấn dữ liệu bài báo / khóa học bằng **FAISS Vector Database + LLM**, cung cấp câu trả lời có ngữ cảnh, có nguồn tham chiếu và hỗ trợ kiến trúc Agentic RAG.

---

## Overview

Article AI Agent là prototype mô phỏng pipeline RAG production-ready gồm:

- Data ingestion & preprocessing  
- Smart chunking + embeddings  
- Semantic retrieval với FAISS  
- LLM generation với grounded context  
- Agentic query optimization loop

### Architecture

<p align="center">
  <img src="https://github.com/user-attachments/assets/ac5483b4-4fb1-4379-bbe7-fa35a9b4331d" width="700"/>
</p>

---

# Features

## Core RAG Pipeline
- Document loading & preprocessing
- Chunking with overlap
- Embedding generation
- FAISS vector indexing
- Context-aware response generation

## Retrieval Features
- Semantic similarity search (Top-K)
- Hybrid retrieval ready (Dense + BM25)
- Reranking support
- Similarity threshold filtering

## Agentic RAG
Unlike traditional RAG (single retrieval), this project simulates an **Agentic RAG loop**:

- Query reformulation  
- Multi-step retrieval  
- Result fusion  
- Decide when retrieval is unnecessary

---

# Tech Stack

## Embeddings
- Transformer Embeddings
- Vector normalization (L2)
- Batch embedding generation

## Vector Database
- FAISS
- Flat Index
- IVF / HNSW support
- GPU acceleration ready

## LLMs
- Mistral
- Mixtral
- Prompt-engineered response generation

---

# RAG Components

## 1. Chunking Strategy

Fixed-length chunking (500–1000 tokens)

- Sliding window overlap (20–30%)
- Sentence-aware splitting
- Metadata preserved

<p align="center">
<img src="https://github.com/user-attachments/assets/3673141b-be27-4b49-bfcb-464dbe083b67" width="900"/>
</p>

---

## 2. Embeddings

Semantic vector representations for:

- Documents  
- Queries  
- Similarity search

<p align="center">
<img src="https://github.com/user-attachments/assets/22830d4d-b84d-46b0-b744-b4cf256603cc" width="900"/>
</p>

---

## 3. Retrieval with FAISS

Supported index types:

- Flat
- IVF
- HNSW
- PQ

Key tuning:

- `nlist`
- `nprobe`
- `efSearch`

<p align="center">
<img src="https://github.com/user-attachments/assets/c4dd0877-5f32-486c-beea-146a3f11ba46" width="850"/>
</p>

---

## 4. Prompted Generation

Prompt template:

```text
Context
Instruction
Question
Answer
```

- Low-temperature generation
- Source-grounded responses
- Hallucination reduction

---

#  Project Structure

```bash
artical-ai-agent/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── services/
│   └── frontEnd/
│
├── data/
├── vector_db/
├── build_db.py
└── requirements.txt
```

---

# Installation

## Create Virtual Environment

```bash
python -m venv rag_env
rag_env\Scripts\Activate.ps1
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python app/main.py
```

Open:

```bash
app/frontEnd/index.html
```

or test API with Postman / Curl.

---

# Index Rebuild

Rebuild vector DB:

```bash
python build_db.py
```

or

```bash
python app/utils/loader.py
```

---

# Retrieval Workflow

```text
User Query
 ↓
Embedding
 ↓
FAISS Search
 ↓
Top-K Chunks
 ↓
(Optional Rerank)
 ↓
LLM Prompting
 ↓
Grounded Answer
```

---

# Safety & Reliability

- Confidence threshold filtering  
- “I don't know” fallback  
- Citation-ready answers  
- Reduced hallucination through retrieval grounding

---

# Future Improvements

- [ ] Hybrid Search (BM25 + Dense)
- [ ] Cross-encoder reranking
- [ ] Conversation memory
- [ ] Agent tools integration
- [ ] Multi-document reasoning
- [ ] Production deployment
