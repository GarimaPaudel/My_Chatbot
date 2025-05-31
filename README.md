# 🤖 Chatbot Task — Intelligent FastAPI Chatbot

A powerful, extensible chatbot system built with **FastAPI**, **LangChain**, and **Groq LLMs** — featuring **Conversational Q&A**, **Appointment Booking**, and **Dynamic Tool Agents**.

---

## 🚀 Features

- 🧠 **Conversational Q&A**  
  Ask natural-language questions about your uploaded documents using RAG (Retrieval-Augmented Generation).

- 📅 **Appointment Booking**  
  Seamlessly book appointments via a conversational form. Collects:
  - Name
  - Email
  - Phone
  - Preferred Date


- 🧬 **MongoDB & Qdrant Integration**  
  - MongoDB: Stores appointment records.
  - Qdrant: Stores vector embeddings of uploaded documents.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <Repository's URL>
cd Chatbot_Task
```

### 2. Clone the Repository
- Using uv
```bash
uv sync
```

### 3. Configure Environment
Create a .env file in the root directory. Use .env.sample as a reference and add your API keys and configuration.

### 4. Run the Server
```bash
python main.py
```

### 5. Docker Images
## 🐳 Docker Setup (Qdrant & Redis)

This project requires **Qdrant** (for vector storage) and **Redis** (for session management). Run both services using Docker.

- ### 📦 Start Qdrant

```bash
docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
```

- ### 📦 Start Redis
```bash
docker run -p 6379:6379 redis
```


## 📡 API Endpoints

| Method | Endpoint                                | Description                                           |
|--------|-----------------------------------------|-------------------------------------------------------|
| POST   | `/api/upload_documents`                | Upload documents to the vector store                 |
| POST   | `/api/documents/extract`               | Extract text from uploaded files                     |
| GET    | `/api/chat`                            | Ask a question about uploaded documents (via query)  |
| POST   | `/api/chat_with_agent`                 | Chat with LangChain agent (requires `user_message` and `session_id`) |
| POST   | `/api/create_collection`               | Create a new vector store collection                 |
| DELETE | `/api/delete_collection/{collection_name}` | Delete an existing vector collection              |
