
# Python ile yazılım geliştirme konularında sıkça sorulan sorular ve yanıtları
# Bu program, kullanıcıdan gelen sorulara yanıt vermek için basit bir sözlük yapısı kullanır.

from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
import webbrowser

webbrowser.open("https://github.com/karaosmanmert/OgrenciKocuAI")

qa_data_cleaned = [
    {
        "question": "Algoritma Nedir?",
        "answer": "Belirli bir problemi çözmek veya belirli bir görevi yerine getirmek için kullanılan, adım adım ilerleyen bir talimatlar dizisidir.",
        "category": "Algoritma"
    },
    {
        "question": "Algoritmanın önemi nedir?",
        "answer": "Algoritmalar, yazılım geliştirme sürecinde problemleri çözmek için sistematik bir yaklaşım sağlar. Doğru algoritmalar, yazılımın performansını ve verimliliğini artırır.",
        "category": "Algoritma"
    },
    {
        "question": "Belirginlik nedir?",
        "answer": "Algoritmanın her adımının açık ve net bir şekilde tanımlanmasıdır. Her adımın ne yapacağı ve nasıl yapılacağı belirgin olmalıdır.",
        "category": "Algoritma"
    },
    {
        "question": "Bir algoritma örneği verin.",
        "answer": "Bir sıralama algoritması örneği olarak 'Bubble Sort' algoritması verilebilir. Bu algoritma, bir dizi sayıyı sıralamak için ardışık karşılaştırmalar yapar.",
        "category": "Algoritma"
    },
    {
        "question": "Bubble Sort algoritması nedir?",
        "answer": "Bubble Sort, ardışık elemanları karşılaştırarak ve gerektiğinde takas yaparak bir diziyi sıralayan basit bir sıralama algoritmasıdır.",
        "category": "Algoritma"
    },
    {
        "question": "Etkinlik nedir?",
        "answer": "Algoritmanın belirli bir problemi çözme süresinin mümkün olan en kısa sürede tamamlanmasıdır. Algoritmanın gereksiz adımlar içermemesi gerekir.",
        "category": "Algoritma"
    },
    {
        "question": "İki sayıyı bölme işlemi kullanmadan bölen algoritma nasıldır?",
        "answer": "Bu algoritma, bölünen sayıdan böleni tekrar tekrar çıkararak kaç kez çıkarıldığını sayar; bu sayı bölüm değeridir.",
        "category": "Algoritma"
    },
    {
        "question": "İki sayıyı çarpma işlemi kullanmadan çarpan algoritma nasıldır?",
        "answer": "Bu algoritma, ikinci çarpan kadar birinci çarpanı toplar. Örneğin, 4 ile 5'i çarpmak için 4 sayısı 5 kez toplanır.",
        "category": "Algoritma"
    },
    {
        "question": "Sonluluk nedir?",
        "answer": "Algoritmanın belirli bir sayıda adımda sonlanmasıdır. Algoritma sonsuz döngüye girmemelidir.",
        "category": "Algoritma"
    },
    {
        "question": "CI/CD nedir?",
        "answer": "CI/CD, yazılımın sürekli entegre edilmesi (Continuous Integration) ve sürekli dağıtımını (Continuous Delivery) ifade eder.",
        "category": "CI/CD"
    },
    {
        "question": "GitHub Actions nedir?",
        "answer": "GitHub Actions, GitHub üzerindeki projeler için otomatik iş akışları oluşturmayı sağlayan CI/CD platformudur.",
        "category": "CI/CD"
    },
    {
        "question": "Jenkins ne işe yarar?",
        "answer": "Jenkins, yazılım geliştirme süreçlerini otomatikleştirmek için kullanılan açık kaynaklı bir CI/CD aracıdır.",
        "category": "CI/CD"
    },
    {
        "question": "Markdown nedir?",
        "answer": "Markdown, düz metin içinde biçimlendirme yapmaya olanak tanıyan hafif bir işaretleme dilidir.",
        "category": "Dökümantasyon"
    },
    {
        "question": "README dosyası ne işe yarar?",
        "answer": "README, projeyi tanıtan ve nasıl kullanılacağını anlatan dökümantasyon dosyasıdır.",
        "category": "Dökümantasyon"
    },
    {
        "question": "Sanal ortam (virtual environment) nedir?",
        "answer": "Sanal ortam, projeye özel bağımlılıkları izole bir şekilde tutan Python ortamıdır.",
        "category": "Geliştirme Ortamı"
    },
    {
        "question": "Terminal nedir?",
        "answer": "Terminal, komut satırı aracılığıyla işletim sistemiyle etkileşim kurmayı sağlayan bir araçtır.",
        "category": "Geliştirme Ortamı"
    },
    {
        "question": "venv nasıl oluşturulur?",
        "answer": "`python -m venv env_adi` komutu ile bir sanal ortam oluşturulur.",
        "category": "Geliştirme Ortamı"
    },
    {
        "question": "Visual Studio Code nedir?",
        "answer": "VS Code, Microsoft tarafından geliştirilen hafif ve özelleştirilebilir bir kaynak kod editörüdür.",
        "category": "IDE"
    },
    {
        "question": "VS Code uzantıları ne işe yarar?",
        "answer": "VS Code uzantıları, editöre ekstra özellikler kazandırarak yazılım geliştirmeyi kolaylaştırır.",
        "category": "IDE"
    },
    {
        "question": "Black nedir?",
        "answer": "Black, Python kodlarını otomatik olarak biçimlendiren bir araçtır.",
        "category": "Kod Kalitesi"
    },
    {
        "question": "Linting nedir?",
        "answer": "Linting, kodunuzu analiz ederek yazım hatalarını ve stil sorunlarını tespit eden bir işlemdir.",
        "category": "Kod Kalitesi"
    },
    {
        "question": "Prettier nedir?",
        "answer": "Prettier, kodun otomatik olarak biçimlendirilmesini sağlayan bir kod formatlama aracıdır.",
        "category": "Kod Kalitesi"
    },
    {
        "question": "pip install komutu ne işe yarar?",
        "answer": "pip install komutu, belirtilen paketi Python ortamınıza yükler.",
        "category": "Paket Yönetimi"
    },
    {
        "question": "Python'da pip ne işe yarar?",
        "answer": "pip, Python paketlerini yüklemek ve yönetmek için kullanılan bir paket yöneticisidir.",
        "category": "Paket Yönetimi"
    },
    {
        "question": "requirements.txt dosyası ne için kullanılır?",
        "answer": "Python projelerinde ihtiyaç duyulan paketlerin listelendiği dosyadır ve `pip install -r` ile yüklenir.",
        "category": "Paket Yönetimi"
    },
    {
        "question": "Gereksinim analizi aşamasının amacı nedir?",
        "answer": "Yazılımın ne yapması gerektiğini belirlemek, kullanıcı ve sistem gereksinimlerini dokümante etmektir.",
        "category": "SDLC"
    },
    {
        "question": "Planlama aşamasında ne yapılır?",
        "answer": "Projenin neden yapılacağı belirlenir, hedef kitle analiz edilir, risk analizi yapılır ve proje planı hazırlanır.",
        "category": "SDLC"
    },
    {
        "question": "SDLC nedir?",
        "answer": "SDLC (Software Development Life Cycle), bir yazılımın planlanmasından bakımına kadar geçen süreci tanımlayan sistematik bir yaklaşımdır.",
        "category": "SDLC"
    },
    {
        "question": "SDLC'nin amaçları nelerdir?",
        "answer": "SDLC'nin temel amaçları, yazılım projelerine standart bir süreç sunmak, hataları azaltmak, kullanıcı gereksinimlerini karşılamak ve projeyi zamanında tamamlamaktır.",
        "category": "SDLC"
    },
    {
        "question": "Tasarım aşamasında neler yapılır?",
        "answer": "Sistem mimarisi belirlenir, UI/UX tasarımı yapılır, veri tabanı yapısı ve yazılım bileşenleri planlanır.",
        "category": "SDLC"
    },
    {
        "question": "Çevik modelin avantajları nelerdir?",
        "answer": "Agile modelde kullanıcı geri bildirimi alınır, değişikliklere hızlı adapte olunur ve erken çalışan yazılım teslimi mümkündür.",
        "category": "SDLC Modeli"
    },
    {
        "question": "Şelale modeli nedir?",
        "answer": "Şelale modeli, SDLC'de adımların sıralı ve geri dönüşsüz şekilde izlendiği klasik bir yazılım geliştirme modelidir.",
        "category": "SDLC Modeli"
    },
    {
        "question": "Branch nedir?",
        "answer": "Branch, projede bağımsız olarak geliştirme yapmayı sağlayan Git yapısıdır.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Git commit nedir?",
        "answer": "Commit, Git deposunda yapılan değişiklikleri kalıcı hale getirir ve geçmişteki değişikliklerin kaydını tutar.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Git nedir?",
        "answer": "Git, yazılım projelerinde değişiklikleri takip etmek için kullanılan dağıtık bir versiyon kontrol sistemidir.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Git pull komutu ne yapar?",
        "answer": "`git pull`, uzak depodaki değişiklikleri yerel depoya indirip birleştirir.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Git push komutu ne yapar?",
        "answer": "`git push`, yerel değişiklikleri uzak Git deposuna gönderir.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Git branching (dallanma) ne işe yarar?",
        "answer": "Git branching, geliştiricilerin projede bağımsız özellikler veya düzeltmeler üzerinde paralel olarak çalışabilmesini sağlar.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Git ve GitHub arasındaki fark nedir?",
        "answer": "Git bir versiyon kontrol sistemidir, GitHub ise Git depolarının çevrim içi olarak barındırılmasını ve paylaşılmasını sağlayan bir platformdur.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "GitHub ile Git arasındaki fark nedir?",
        "answer": "Git, versiyon kontrol sistemidir; GitHub ise Git ile yönetilen projeleri barındırmak için kullanılan çevrim içi bir platformdur.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "GitHub nedir?",
        "answer": "GitHub, Git tabanlı projelerin barındırılması, paylaşılması ve iş birliği yapılması için kullanılan bir platformdur.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "GitHub Actions nedir?",
        "answer": "GitHub Actions, yazılım projelerinde otomatikleştirilmiş işlemler oluşturmak için kullanılan bir CI/CD aracıdır.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "GitHub üzerinde Pull Request (PR) nedir?",
        "answer": "Pull Request, bir projede yapılan değişiklikleri incelemek ve ana dala dahil edilmesini istemek için kullanılan GitHub özelliğidir.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Merge işlemi ne yapar?",
        "answer": "Merge, bir branch'teki değişiklikleri başka bir branch'e entegre eder.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Versiyon kontrol sistemine neden ihtiyaç duyarız?",
        "answer": "Kod değişikliklerini takip etmek, ekip içi iş birliğini sağlamak, veri kaybını önlemek ve eski sürümlere dönmek gibi ihtiyaçlar nedeniyle versiyon kontrol sistemlerine ihtiyaç duyulur.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Git’in tarihçesi nedir?",
        "answer": "Git, 2005 yılında Linus Torvalds tarafından, Linux çekirdeğini yönetmek için geliştirilmiştir. Daha önce kullanılan BitKeeper yazılımının eksiklerini gidermek amacıyla oluşturulmuştur.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Git’in temel özellikleri nelerdir?",
        "answer": "Git hızlıdır, dağıtık bir yapıya sahiptir, dallanma (branching) sistemini destekler ve açık kaynaklıdır.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Merkezi ve dağıtık versiyon kontrol sistemleri arasındaki fark nedir?",
        "answer": "Merkezi sistemlerde tüm değişiklikler tek bir sunucuda tutulur, dağıtık sistemlerde ise her geliştirici proje geçmişinin bir kopyasını kendi bilgisayarında tutar.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Python'da test nasıl yazılır?",
        "answer": "`assert` ifadeleri veya `unittest`, `pytest` gibi kütüphanelerle test yazılabilir.",
        "category": "Test Araçları"
    },
    {
        "question": "pytest nedir?",
        "answer": "pytest, Python programlama dili için geliştirilmiş bir test framework'üdür.",
        "category": "Test Araçları"
    },
    {
        "question": "unittest nedir?",
        "answer": "unittest, Python'da birim testi yazmak için kullanılan yerleşik bir kütüphanedir.",
        "category": "Test Araçları"
    }
]



sorular = [item["question"] for item in qa_data_cleaned]
cevaplar = [item["answer"] for item in qa_data_cleaned]

model = SentenceTransformer('all-MiniLM-L6-v2')
soru_embeddings = model.encode(sorular)
nn = NearestNeighbors(n_neighbors=1, metric='cosine')
nn.fit(soru_embeddings)


def get_answer(question):
    for qa in qa_data_cleaned:
        if qa["question"].lower() == question.lower():
            return qa["answer"]
    return "Bu soruya yanıt bulamadım."

print("Sorularınızı yazabilirsiniz. Çıkmak için 'exit' yazın.")
while True:
    user_input = input("Soru: ")
    if user_input.lower() == 'exit':
        print("Çıkılıyor...")
        break

    input_embedding = model.encode([user_input])

    distance, index = nn.kneighbors(input_embedding)
    similarity = 1 - distance[0][0]

    if similarity > 0.7:
        answer = cevaplar[index[0][0]]
    else:
        answer = "Bu soruyu anlayamadım veya veri setimde yok."

    print("Cevap:", answer)



