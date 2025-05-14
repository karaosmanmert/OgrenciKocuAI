import os
import json
import requests
import openai
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors 
import webbrowser
import re

# Ortam değişkenlerini yükle
load_dotenv()

webbrowser.open("https://github.com/karaosmanmert/OgrenciKocuAI")

# API anahtarları
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")
openai.api_key = os.getenv("OPENAI_API_KEY")

# Embedding modeli
model_name = "all-MiniLM-L6-v2"
embedding_model = SentenceTransformer(model_name)

# İlgi alanları
ILGILI = {
    "diller": ["python", "java", "c++", "c#", "javascript", "html", "css", "sql", "typescript"],
    "araçlar": ["git", "github", "vscode", "pycharm", "jupyter", "notepad++", "docker", "linux", "terminal", "komut satırı"],
    "genel_kavramlar": ["yazılım", "programlama", "kodlama", "veri yapıları", "algoritma", "backend", "frontend", "full stack"],
    "teknolojiler": ["api", "rest", "graphql", "json", "web", "mobil", "uygulama", "sistem", "donanım"],
    "ai": ["yapay zeka", "machine learning", "makine öğrenmesi", "deeplearning", "openai", "tensorflow", "pytorch", "gpt"],
}

# Soru alakalı mı kontrolü
def alakalimi(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    score = 0
    for keywords in ILGILI.values():
        for kw in keywords:
            if kw in text or any(kw in word for word in words):
                score += 1
    return score >= 1

# Embedding üret
def get_embedding(text):
    return embedding_model.encode([text])[0]

# Airtable'dan tüm kayıtları çek
def get_all_records():
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
    records = []

    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return []
        data = response.json()
        records.extend(data.get("records", []))
        offset = data.get("offset")
        url = f"{url.split('?')[0]}?offset={offset}" if offset else None

    return records

# Embedding güncelle
def update_embedding(record_id, embedding):
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}/{record_id}"
    data = {"fields": {"embedding": json.dumps(embedding.tolist())}}
    requests.patch(url, headers=headers, json=data)

# Yeni kayıt ekle
def add_record_to_airtable(soru, cevap, kategori, embedding):
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
    data = {
        "fields": {
            "soru": soru,
            "cevap": cevap,
            "kategori": kategori,
            "embedding": json.dumps(embedding.tolist())
        }
    }
    requests.post(url, headers=headers, json=data)

# Verileri hazırla
def prepare_data():
    records = get_all_records()
    questions, answers, embeddings = [], [], []

    for rec in records:
        fields = rec.get("fields", {})
        if all(k in fields for k in ("soru", "cevap", "kategori")):
            try:
                if "embedding" in fields and fields["embedding"].strip() != "":
                    emb = np.array(json.loads(fields["embedding"]))
                else:
                    emb = get_embedding(fields["soru"])
                    update_embedding(rec["id"], emb)
            except:
                emb = get_embedding(fields["soru"])
                update_embedding(rec["id"], emb)

            questions.append(fields["soru"])
            answers.append(fields["cevap"])
            embeddings.append(emb)

    return questions, answers, np.array(embeddings)

# GPT'den cevap ve kategori al
def get_gpt_answer(user_question):
    system_msg = "Sen üniversite öğrencilerine kısa, açık ve öz cevaplar veren bir asistansın. Cevabın en fazla 2-3 cümle olsun."
    category_hint = "Aşağıdaki soruya hem kısa bir cevap ver hem de bu sorunun ait olduğu kategori etiketini üret. Sadece cevabı ve kategoriyi ver."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": f"{category_hint}\n\nSoru: {user_question}"}
        ],
        temperature=0.4
    )

    content = response.choices[0].message["content"]
    lines = content.strip().splitlines()
    cevap = ""
    kategori = ""
    for line in lines:
        if line.lower().startswith("cevap:"):
            cevap = line.split(":", 1)[1].strip()
        elif line.lower().startswith("kategori:"):
            kategori = line.split(":", 1)[1].strip()
    return cevap, kategori

# Ana akış
questions, answers, embeddings = prepare_data()

print("Soru-Cevap sistemine hoş geldiniz. Çıkmak için 'exit' yazın.")

while True:
    user_input = input("Soru: ").strip()
    if user_input.lower() == "exit":
        break

    if not alakalimi(user_input):
        print("Alakasız bir soru sordunuz.")
        continue

    if len(questions) == 0:
        print("Veri bulunamadı.")
        continue

    model = NearestNeighbors(n_neighbors=1, metric="cosine")
    model.fit(embeddings)
    user_emb = get_embedding(user_input)
    distance, index = model.kneighbors([user_emb])
    similarity = 1 - distance[0][0]

    if similarity > 0.5:
        print("Cevap:", answers[index[0][0]])
    else:
        gpt_answer, gpt_kategori = get_gpt_answer(user_input)
        add_record_to_airtable(user_input, gpt_answer, gpt_kategori, user_emb)
        questions.append(user_input)
        answers.append(gpt_answer)
        embeddings = np.vstack([embeddings, user_emb])
        print("Cevap:", gpt_answer)
