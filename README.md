# 🏗️ Elnor Yapı Asistanı - SmartLead AI

Bu proje, inşaat ve emlak sektöründeki potansiyel müşterileri dijital ortamda karşılamak, sorularını yanıtlamak ve iletişim bilgilerini (lead) toplamak amacıyla geliştirilmiş **SmartLead AI** mimarisinin Elnor Yapı'ya uyarlanmış halidir.

## 📌 Projenin Amacı ve İşleyişi
Sistem iki temel arayüzden oluşmaktadır:
1. **B2C Karşılama Sayfası (Vitrin):** Wix Velo kullanılarak geliştirilmiş, Z-Pattern tasarımına sahip ön yüz. Ziyaretçiler burada yapay zeka ile projeler hakkında sohbet eder ve iletişim bilgilerini bırakabilirler.
2. **B2B Yönetim Paneli (Dashboard):** İşletme sahibinin, toplanan müşteri taleplerini (leads) F-Pattern düzeninde tasarlanmış bir Repeater tablosunda görüntülediği yönetim panelidir.

## 🏗️ Mimari ve Kullanılan Teknolojiler
Bu projede **Sorumlulukların Ayrılığı (Separation of Concerns - SoC)** ilkesine katı bir şekilde uyulmuştur. Her katman izole çalışır:
* **Backend:** Python & Flask
* **Yapay Zeka (Revizyonlu):** Groq API (openai/gpt-oss-120b modeli). 
  * *Geliştirici Notu:* Yönergede belirtilen `llama-3.1-8b-instant` modeli geliştirme ve test sürecinde yanıt verememe/stabilite sorunları yaşattığı için, projenin sunum anında kesintisiz çalışması ve müşteriye daha akıllı yanıtlar üretebilmesi adına inisiyatif alınarak `openai/gpt-oss-120b` modeline geçiş yapılmıştır. Mimari kurallar (AI çağrılarının sadece `ai_service.py` içinde izole edilmesi) %100 korunmuştur.
* **Veritabanı:** SQLite - *Sadece `database.py` içinde, SQL Injection korumalı (?) olarak çalışır.*
* **Rotalar (`routes.py`):** Sadece HTTP isteklerini (GET/POST) karşılayıp doğru katmana yönlendiren köprü görevini üstlenir. 
* **Frontend:** Wix Studio & Velo API

## 🚀 Projeyi Yerelde (Local) Çalıştırma Adımları

1. Repoyu bilgisayarınıza klonlayın:
   `git clone <repo-url>`
2. Proje dizinine gidin ve sanal ortamı (venv) aktif edin.
3. Gerekli kütüphaneleri kurun:
   `pip install -r requirements.txt`
4. Ana dizinde bir `.env` dosyası oluşturup içine ilgili API anahtarlarını (GROQ_API_KEY, SECRET_KEY) ekleyin.
5. Sunucuyu başlatın:
   `python run.py`
6. Tarayıcınızda `http://localhost:5000/health` adresine giderek sunucunun aktif olduğunu doğrulayabilirsiniz.