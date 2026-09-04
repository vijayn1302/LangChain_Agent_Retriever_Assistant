# 🤖 LangChain Agent Retriever Assistant

An AI-powered **RAG Assistant** built using **LangChain, Groq, HuggingFace Embeddings, and In-Memory Vector Store**.

The agent decides whether to search the knowledge base and uses retrieved documents to generate relevant answers.

## 🔄 Workflow

```text
USER
  ↓
AGENT
  ↓
LLM
  ↓
Decide to Search
  ↓
SEARCH KNOWLEDGE TOOL
  ↓
RETRIEVER
  ↓
VECTOR STORE
  ↓
RELEVANT DOCUMENTS
  ↓
TOOL RESULT
  ↓
LLM
  ↓
FINAL ANSWER
```

## ✨ Features

* 🤖 Agent-based AI assistant
* 🔍 Knowledge search tool
* 📚 Retriever-based document search
* 🧠 HuggingFace embeddings
* 🗂️ In-Memory Vector Store
* ⚡ Groq LLM
* 💬 Interactive command-line chat
* 📖 RAG-based question answering

## 🛠️ Technologies

* Python
* LangChain
* Groq
* HuggingFace
* Sentence Transformers
* In-Memory Vector Store

## 📚 Knowledge Base

The assistant contains short documents about:

* Python
* Machine Learning
* Deep Learning
* CNN
* RAG
* LangChain

The project creates embeddings and stores the documents in a vector store for retrieval.

## ⚙️ Installation

```bash
pip install -U langchain langchain-core langchain-groq
pip install -U langchain-huggingface sentence-transformers
```

## 🔑 API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

## ▶️ Run

```bash
python LangChain_Agent_Retriever_Assistant.py
```

Then ask questions such as:

```text
What is CNN?
What is Machine Learning?
What is RAG?
What is LangChain?
```

Type `exit` to close the assistant.

## 🎯 Project Goal

The goal of this project is to demonstrate how an **AI Agent can intelligently use a Retriever and Vector Store to search knowledge and generate grounded responses using an LLM**.

## 👨‍💻 Author

**Vijay N**
