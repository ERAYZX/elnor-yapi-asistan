import sqlite3
from flask import current_app, g

# Yönerge: Veritabanına bağlanır; satırlara sütun adıyla erişim sağlar
def get_db():
    if 'db' not in g:
        # Config'den gelen URL'yi al (sqlite:/// kısmını temizleyerek yolu bul)
        db_path = current_app.config.get('DATABASE_URL', 'leads.db').replace('sqlite:///', '')
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row  # Sütunlara isimle erişmek için
    return g.db

# Yönerge: 'leads' tablosunu oluşturur
def init_db(app):
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()

# Yönerge: Yeni kayıt ekler. SQL koruması (?) zorunludur!
def lead_ekle(isim, telefon, mesaj=""):
    try:
        db = get_db()
        # GÜVENLİK KURALI: Değerleri doğrudan SQL'e yazmak yasaktır, ? kullanılır.
        db.execute(
            'INSERT INTO leads (isim, telefon, mesaj) VALUES (?, ?, ?)',
            (isim, telefon, mesaj)
        )
        db.commit()
        return True
    except Exception as e:
        print(f"Veritabanı kayit hatasi: {e}")
        return False

# Yönerge: Tüm kayıtları en yeniden eskiye getirir
def tum_leadler():
    db = get_db()
    cursor = db.execute('SELECT * FROM leads ORDER BY id DESC')
    return [dict(row) for row in cursor.fetchall()]