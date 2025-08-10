from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import crypto_bp
    app.register_blueprint(crypto_bp)
    
    return app