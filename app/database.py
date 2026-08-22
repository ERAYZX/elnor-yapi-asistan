import sqlite3

DB_NAME = "elnor_musteriler.db"

def init_db():
    # Veritabanı ve tablo kurulumu
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            telefon TEXT NOT NULL,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_lead(isim, telefon):
    # Yeni lead (müşteri) ekleme işlemi
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO leads (isim, telefon) VALUES (?, ?)', (isim, telefon))
    conn.commit()
    conn.close()

def get_all_leads():
    # Tüm kayıtlı müşterileri en son eklenenden başlayarak getir
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT isim, telefon, tarih FROM leads ORDER BY id DESC')
    leads = cursor.fetchall()
    conn.close()
    return leads    