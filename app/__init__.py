from flask import Flask, jsonify
from flask_cors import CORS
from config import config
from .database import init_db

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Yönerge: CORS aç ve veritabanını başlat
    CORS(app)
    init_db(app)
    
    # Yönerge: Blueprint'leri kaydet
    from .routes import main, api
    app.register_blueprint(main)
    app.register_blueprint(api)
    
    # Yönerge: Bir /health uç noktası (sunucu canlılık kontrolü)
    @app.route('/health')
    def health_check():
        return jsonify({'durum': 'aktif', 'mesaj': 'Sunucu ayakta'})
        
    return app