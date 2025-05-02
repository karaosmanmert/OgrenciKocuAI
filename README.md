Kullanıcıdan alınan sorular, önceden tanımlanmış bir veri kümesindeki sorularla karşılaştırılır.
Anlamca en benzer soru bulunur ve o soruya ait cevap kullanıcıya gösterilir.

Proje Özellikleri:
- Sorular ve cevaplar Python sözlüğü (list of dictionaries) yapısında tanımlanmıştır.
- Kullanıcıdan gelen soru, embedding yöntemi ile sayısal vektöre çevrilir.
- Veritabanındaki soruların embedding'leri ile karşılaştırma yapılır.
- Cosine benzerliği esas alınarak en yakın soru belirlenir.
- %70 ve üzeri benzerlik varsa ilgili cevap gösterilir, aksi halde anlaşılmadığı bilgisi verilir.

Kullanılan Kütüphaneler:
- sentence-transformers: metinleri sayısal embedding'e çevirmek için kullanılır.
- scikit-learn: en yakın komşuyu (NearestNeighbors) bulmak için kullanılır.

Kurulum:
1. Python 3 yüklü olmalıdır.
2. Gerekli kütüphaneleri yükleyin:
   pip install sentence-transformers scikit-learn

3. script'i çalıştırın:
   python bot.py

Kullanım:
- Program çalıştığında kullanıcıya "Soru:" yazısıyla giriş istenir.
- Kullanıcı metin olarak bir soru yazar.
- Bot anlamlı bir eşleşme bulursa cevabı gösterir.
- Çıkmak için 'exit' yazılması yeterlidir.

Veri Yapısı:
Veri seti Python içinde qa_data_cleaned isminde bir değişkende tutulur.
Her bir öğe aşağıdaki formatta yazılmıştır:

{
    "question": "Soru metni",
    "answer": "Cevap metni",
    "category": "Kategori"
}

Sistem temel düzeyde metin benzerliği üzerine kuruludur.
