from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user



views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/items')
@login_required
def items():
    return render_template("items.html", user=current_user)


@views.route('/book')
@login_required
def book():
    return render_template("book.html", user=current_user)