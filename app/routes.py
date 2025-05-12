from flask import Blueprint, render_template, request, redirect, url_for, flash
from decimal import Decimal
from .models import Produto
from . import db

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Coleta dados do formulário
        nome = request.form.get("nome")
        codigo = request.form.get("codigo")
        preco = request.form.get("preco", type=float)
        quantidade = request.form.get("quantidade", type=int)

        # Validação simples
        if not nome or not codigo:
            flash("Nome e código são obrigatórios.", "error")
        else:
            p = Produto(
                nome=nome,
                codigo=codigo,
                preco=Decimal(preco),
                quantidade=quantidade,
            )
            db.session.add(p)
            db.session.commit()
            flash("Produto adicionado!", "success")
            return redirect(url_for("main.index"))

    produtos = Produto.query.all()
    return render_template("index.html", produtos=produtos)
