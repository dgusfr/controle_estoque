from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Diretório-base do projeto
    base_dir = Path(__file__).resolve().parent.parent
    db_path = base_dir / "database" / "estoque.db"
    db_path.parent.mkdir(exist_ok=True)  # garante pasta database/

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "troque-esta-chave"

    db.init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Cria tabelas se não existirem
    with app.app_context():
        db.create_all()

    return app
