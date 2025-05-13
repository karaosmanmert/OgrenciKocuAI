import os
import json
import requests
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
import webbrowser

load_dotenv()

webbrowser.open("https://github.com/karaosmanmert/OgrenciKocuAI")

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

model_name = "all-MiniLM-L6-v2"
embedding_model = SentenceTransformer(model_name)

def get_embedding(text):
    return embedding_model.encode([text])[0]

#airtable dan verileri cek
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
        url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}?offset={offset}" if offset else None

    return records

#emb eksşkse guncelle
def update_embedding(record_id, embedding):
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}/{record_id}"
    data = {
        "fields": {
            "embedding": json.dumps(embedding.tolist())
        }
    }
    requests.patch(url, headers=headers, json=data)

#verileri hazırlama
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
            except: # hata alırsak yeni embedding oluştur
                emb = get_embedding(fields["soru"])
                update_embedding(rec["id"], emb)

            questions.append(fields["soru"])
            answers.append(fields["cevap"])
            embeddings.append(emb)

    return questions, answers, np.array(embeddings)

# Yalnızca mevcut veriyi yükle
questions, answers, embeddings = prepare_data()

print("Soru-Cevap sistemine hoş geldiniz. Çıkmak için 'exit' yazın.")

while True:
    user_input = input("Soru: ").strip()
    if user_input.lower() == "exit":
        break

    if len(questions) == 0:
        print("Veri bulunamadı.")
        continue
# en yakin soruyu  bul
    model = NearestNeighbors(n_neighbors=1, metric="cosine")
    model.fit(embeddings)
    user_emb = get_embedding(user_input)
    distance, index = model.kneighbors([user_emb])
    similarity = 1 - distance[0][0]
#yeterince benziyorsa cevabı ver
    if similarity > 0.4:
        print("Cevap:", answers[index[0][0]])
    else:
        print("Bu soruya karşılık gelen bir cevap bulunamadı.")
