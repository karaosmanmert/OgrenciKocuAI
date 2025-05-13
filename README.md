Embedding Tabanlı Soru-Cevap Botu

Bu proje, öğrencilere kısa ve öz yanıtlar veren bir soru-cevap asistanıdır. 
Uygulama, kullanıcının sorduğu sorularla Airtable veritabanındaki kayıtları karşılaştırır. 
Benzer bir soru bulunamazsa, OpenAI API kullanılarak yeni bir yanıt oluşturulur ve veritabanına kaydedilir.

Dosyalar:

- main.py: OpenAI API kullanarak çalışır. Gerekirse yeni cevap üretir.
- main2.py: Sadece Airtable'daki mevcut verilerle çalışır.
- .env: API anahtarlarının güvenli saklanması için kullanılır.
- requirements.txt: Proje için gerekli Python kütüphanelerini içerir.

Kurulum:

1. Python 3.8 veya üzeri kurulu olmalıdır.
2. Gerekli paketler aşağıdaki komutla yüklenebilir:
   pip install -r requirements.txt
3. Aynı klasöre bir .env dosyası ekleyin ve aşağıdaki bilgileri doldurun:

AIRTABLE_API_KEY=airtable_api_key
AIRTABLE_BASE_ID=airtable_base_id
AIRTABLE_TABLE_NAME=Table 1
OPENAI_API_KEY=openai_api_key   (sadece main.py için gereklidir)

Kullanım:

- OpenAI destekli tam sürüm için: python main.py
- Sadece mevcut verilerle çalışmak için: python main2.py

Not:

- .env dosyasını kimseyle paylaşmayın ve GitHub'a yüklemeyin.
