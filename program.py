

# Python ile yazılım geliştirme konularında sıkça sorulan sorular ve yanıtları
# Bu program, kullanıcıdan gelen sorulara yanıt vermek için basit bir sözlük yapısı kullanır.

qa_data = [
    {
        "question": "Git nedir?",
        "answer": "Git, yazılım projelerinde değişiklikleri takip etmek için kullanılan dağıtık bir versiyon kontrol sistemidir.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "GitHub ile Git arasındaki fark nedir?",
        "answer": "Git, versiyon kontrol sistemidir; GitHub ise Git ile yönetilen projeleri barındırmak için kullanılan çevrim içi bir platformdur.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Visual Studio Code nedir?",
        "answer": "VS Code, Microsoft tarafından geliştirilen hafif ve özelleştirilebilir bir kaynak kod editörüdür.",
        "category": "IDE"
    },
    {
        "question": "Python'da pip ne işe yarar?",
        "answer": "pip, Python paketlerini yüklemek ve yönetmek için kullanılan bir paket yöneticisidir.",
        "category": "Paket Yönetimi"
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
    },
    {
        "question": "Jenkins ne işe yarar?",
        "answer": "Jenkins, yazılım geliştirme süreçlerini otomatikleştirmek için kullanılan açık kaynaklı bir CI/CD aracıdır.",
        "category": "CI/CD"
    },
    {
        "question": "Git commit nedir?",
        "answer": "Commit, Git deposunda yapılan değişiklikleri kalıcı hale getirir ve geçmişteki değişikliklerin kaydını tutar.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Branch nedir?",
        "answer": "Branch, projede bağımsız olarak geliştirme yapmayı sağlayan Git yapısıdır.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "Merge işlemi ne yapar?",
        "answer": "Merge, bir branch'teki değişiklikleri başka bir branch'e entegre eder.",
        "category": "Versiyon Kontrol"
    },
    {
        "question": "VS Code uzantıları ne işe yarar?",
        "answer": "VS Code uzantıları, editöre ekstra özellikler kazandırarak yazılım geliştirmeyi kolaylaştırır.",
        "category": "IDE"
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
        "question": "requirements.txt dosyası ne için kullanılır?",
        "answer": "Python projelerinde ihtiyaç duyulan paketlerin listelendiği dosyadır ve `pip install -r` ile yüklenir.",
        "category": "Paket Yönetimi"
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
        "question": "Terminal nedir?",
        "answer": "Terminal, komut satırı aracılığıyla işletim sistemiyle etkileşim kurmayı sağlayan bir araçtır.",
        "category": "Geliştirme Ortamı"
    },
    {
        "question": "Sanal ortam (virtual environment) nedir?",
        "answer": "Sanal ortam, projeye özel bağımlılıkları izole bir şekilde tutan Python ortamıdır.",
        "category": "Geliştirme Ortamı"
    },
    {
        "question": "venv nasıl oluşturulur?",
        "answer": "`python -m venv env_adi` komutu ile bir sanal ortam oluşturulur.",
        "category": "Geliştirme Ortamı"
    },
    {
        "question": "Black nedir?",
        "answer": "Black, Python kodlarını otomatik olarak biçimlendiren bir araçtır.",
        "category": "Kod Kalitesi"
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
        "question": "README dosyası ne işe yarar?",
        "answer": "README, projeyi tanıtan ve nasıl kullanılacağını anlatan dökümantasyon dosyasıdır.",
        "category": "Dökümantasyon"
    },
    {
        "question": "Markdown nedir?",
        "answer": "Markdown, düz metin içinde biçimlendirme yapmaya olanak tanıyan hafif bir işaretleme dilidir.",
        "category": "Dökümantasyon"
    },
    {
        "question": "Python'da test nasıl yazılır?",
        "answer": "`assert` ifadeleri veya `unittest`, `pytest` gibi kütüphanelerle test yazılabilir.",
        "category": "Test Araçları"
    }
]



def get_answer(question):
    for qa in qa_data:
        if qa["question"].lower() == question.lower():
            return qa["answer"]
    return "Bu soruya yanıt bulamadım."

print("Sorularınızı yazabilirsiniz. Çıkmak için 'exit' yazın.")
while True:
    user_input = input("Soru: ")
    if user_input.lower() == 'exit':
        print("Çıkılıyor...")
        break
    answer = get_answer(user_input)
    print("Cevap:", answer)

