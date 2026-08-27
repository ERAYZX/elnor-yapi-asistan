from flask import Blueprint, render_template, request, jsonify
from .database import lead_ekle, tum_leadler
from .services.ai_service import ai_service, AIServiceError

# Blueprint tanımları 
main = Blueprint('main', __name__)
api = Blueprint('api', __name__, url_prefix='/api')

# Yönerge: GET / - Karşılama sayfasını gösterir
@main.route('/')
def index():
    return render_template('index.html')

# Yönerge: GET /dashboard - Yönetim panelini gösterir
@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Yönerge: POST /api/sohbet - AI'a mesaj iletir
@api.route('/sohbet', methods=['POST'])
def chat():
    data = request.get_json()
    mesaj = data.get('mesaj', '')
    
    if not mesaj:
        return jsonify({'basari': False, 'hata': 'Mesaj eksik'}), 400
        
    try:
        cevap = ai_service.yanit_uret(mesaj)
        return jsonify({'basari': True, 'cevap': cevap})
    except AIServiceError as e:
        return jsonify({'basari': False, 'hata': str(e)}), 503

# Yönerge: POST /api/leads - Yeni lead kaydeder
@api.route('/leads', methods=['POST'])
def add_lead_route():
    data = request.get_json()
    isim = data.get('isim')
    telefon = data.get('telefon')
    
    if not isim or not telefon:
        return jsonify({'basari': False, 'hata': 'İsim ve telefon zorunlu'}), 400
        
    kayit_basarili = lead_ekle(isim, telefon, data.get('mesaj', ''))
    if kayit_basarili:
        return jsonify({'basari': True, 'mesaj': 'Kayıt başarılı'}), 201
    return jsonify({'basari': False, 'hata': 'Veritabanı hatası'}), 500

# Yönerge: GET /api/leads - Tüm lead'leri getirir
@api.route('/leads', methods=['GET'])
def get_leads_route():
    leadler = tum_leadler()
    return jsonify({'basari': True, 'data': leadler})