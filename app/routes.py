from flask import Blueprint, render_template, request, jsonify
from .database import add_lead, get_all_leads
from .services.ai_service import yapay_zeka_ile_konus
import re  # Python'un kelime ve numara avcısı kütüphanesi

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/sohbet', methods=['POST'])
def chat():
    data = request.get_json()
    kullanici_mesaji = data.get('mesaj', '')
    
    if not kullanici_mesaji:
        return jsonify({'hata': 'Mesaj alanı boş olamaz'}), 400

   # --- 1.  VERİ AVCISI: Her türlü telefon formatını yakalar (+90, tire, boşluk) ---
    telefon_deseni = r'(?:\+90|0)?\s*5\d{2}[\s\-]*\d{3}[\s\-]*\d{2}[\s\-]*\d{2}'
    bulunan_numaralar = re.findall(telefon_deseni, kullanici_mesaji)

    # --- 2. KÖPRÜ: Bulunan numarayı veritabanına kaydet ---
    if bulunan_numaralar:
        # Yakalanan numaranın içindeki tüm tireleri ve boşlukları temizler, jilet gibi kaydeder
        yakalanan_numara = re.sub(r'[\s\-]', '', bulunan_numaralar[0]) 
        add_lead("Sohbet Ziyaretçisi", yakalanan_numara)

    # 3. Mesajı her halükarda yapay zekaya gönder ve cevabı al
    ai_cevabi = yapay_zeka_ile_konus(kullanici_mesaji)
    return jsonify({'cevap': ai_cevabi})

@main.route('/api/leads', methods=['POST'])
def lead_ekle():
    data = request.get_json()
    isim = data.get('isim')
    telefon = data.get('telefon')
    
    if isim and telefon:
        add_lead(isim, telefon)
        return jsonify({'mesaj': 'Kayıt başarılı'}), 200
        
    return jsonify({'hata': 'Eksik bilgi gönderildi'}), 400

@main.route('/dashboard')
def dashboard():
    leads = get_all_leads()
    return render_template('dashboard.html', leads=leads)