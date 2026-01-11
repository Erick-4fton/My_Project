from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("OPENROUTER_MODEL"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.4
)

def ask_ai(question, products):
    product_list = "\n".join([
        f"- {p['name']} ({p['category']}) Rp {p['price']}"
        for p in products
    ])

    prompt = f"""
    Kamu adalah AI asisten toko mainan.
    Rekomendasikan produk berdasarkan pertanyaan user.

    Daftar produk:
    {product_list}

    Pertanyaan user:
    {question}

    Jawab singkat, jelas, dan persuasif dalam Bahasa Indonesia.
    """

    return llm.invoke(prompt).content
