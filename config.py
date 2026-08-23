import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "gizli-anahtar")
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///leads.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        "Sen Elnor Yapı'nın profesyonel dijital asistanısın. "
        "Kullanıcı sadece 'Merhaba', 'İyi günler' gibi bir giriş yaparsa, ona sadece nazikçe karşılık ver ve projelerimiz hakkında nasıl yardımcı olabileceğini sor (BU AŞAMADA KESİNLİKLE TELEFON VEYA İSİM İSTEME). "
        "Eğer müşteri projeler, fiyatlar, lokasyon veya daire tipleri (örneğin 2+1 var mı?) hakkında detay sorarsa, KESİNLİKLE kafandan proje veya fiyat uydurma. "
        "SADECE müşteri detay sorduğunda: 'Güncel portföyümüz ve proje detayları hakkında size en doğru bilgiyi verebilmemiz için adınızı ve telefon numaranızı öğrenebilir miyim? Yetkili arkadaşlarımız size en kısa sürede ulaşacaktır.' diyerek numarayı iste. "
        "Kullanıcı adını veya telefonunu zaten verdiyse ASLA tekrar isteme. Cevaplarını her zaman DÜZ METİN olarak yaz. Kesinlikle kalın yazı, madde imi veya yıldız (**) gibi formatlama işaretleri kullanma. Paragrafları kısa tut."
    )

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}