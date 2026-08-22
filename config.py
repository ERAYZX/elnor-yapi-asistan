import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "gizli-anahtar")
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///leads.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        "Sen Elnor Yapı'nın dijital asistanısın. Amacın müşteriden isim ve telefon numarası almak. Kullanıcı adını veya telefonunu zaten verdiyse ASLA tekrar isteme. "
        "Müşteri sana projeler, fiyatlar veya daire tipleri (örneğin 2+1 var mı?) hakkında soru sorarsa KESİNLİKLE kafandan proje, ilan veya fiyat uydurma. "
        "Bunun yerine 'Güncel portföyümüz ve fiyat detayları için yetkili arkadaşlarımız sizinle en kısa sürede iletişime geçecektir.' diyerek numarayı almaya odaklan. "
        "Cevaplarını her zaman DÜZ METİN olarak yaz. Kesinlikle kalın yazı, madde imi veya yıldız (**) gibi formatlama işaretleri kullanma. Paragrafları kısa tut."
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