from flask import Flask
from config import Config
from .database import init_db
from flask_cors import CORS

def create_app():
    # Uygulamayı ve ayarları başlat
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    # Veritabanı tablosunu hazırla
    with app.app_context():
        init_db()

    # Rotaları (trafik polisini) sisteme tanıt
    from .routes import main
    app.register_blueprint(main)

    return app