import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.documents import Document
from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent

#---------- Load API Key ----------

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

#---------- Knowledge Documents ----------

documents = [
    Document(page_content="Python is a programming language used for AI, Machine Learning, Data Science, and automation."),

    Document(page_content="Machine Learning allows computers to learn patterns from data and make predictions."),

    Document(page_content="Deep Learning uses neural networks with multiple layers to solve complex problems."),

    Document(page_content="CNN stands for Convolutional Neural Network. It is mainly used for image processing and computer vision."),

    Document(page_content="RAG stands for Retrieval-Augmented Generation. It retrieves relevant information before generating an answer."),

    Document(page_content="LangChain is a framework for building applications using Large Language Models, agents, tools, and retrievers.")
]

#---------- Embeddings ----------

embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

#---------- Vector Store ----------

vectorstore = InMemoryVectorStore.from_documents(documents = documents, embedding = embeddings)

#---------- Retriever ----------

retriever = vectorstore.as_retriever(search_kwargs = {"k": 3})

#---------- Knowledge Search Tool ----------

@tool
def search_knowledge(query: str) -> str:
    """
    Search the course knowledge base for relevant information.

    Use this tool when the user asks questions related to
    Python, Machine Learning, Deep Learning, CNN, RAG,
    LangChain, or the stored course knowledge.
    """

    docs = retriever.invoke(query)

    if not docs:
        return "No relevant information was found in the knowledge base."

    results = []

    for i, doc in enumerate(docs, start = 1):
        results.append(f"Document {i}:\n{doc.page_content}")

    return"\n\n".join(results)

#---------- LLM ----------

llm = ChatGroq(model = "openai/gpt-oss-120b",
               temperature = 0)

#---------- System Prompt ----------

system_prompt = """
You are a helpful AI Assistant.

Use the knowledge search tool when needed.

Answer using retrieved information and do not make up facts.

For general questions, answer directly.
"""

#---------- Agent ----------

agent = create_agent(model = llm, tools = [search_knowledge], system_prompt = system_prompt)

#---------- Chat Function ----------

def ask_assistant(question):

    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })
    return response["messages"][-1].content

# ---------- Chat Loop ----------

print("=" * 60)
print("RAG Knowledge Assistant")
print("=" * 60)

print("Type 'exit' to stop.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    try:

        answer = ask_assistant(question)

        print("Assistant: ",answer)
        # print(answer)
        # print()

    except Exception as e:

        print("\nError:", e)