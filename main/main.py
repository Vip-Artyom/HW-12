import logging
from flask import Blueprint, request, render_template
from functions import load_posts

# Импортируем все что нам нужно

logging.basicConfig(filename="basic.log", encoding='utf-8', level=logging.INFO)  # Настраиваем логирование

main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/')  # вьюшка главной страницы
def main():
    return render_template("index.html")


@main_blueprint.route('/search')  # вьюшка страницы поиска
def search():
    search_by = request.args['s']
    logging.info(f"Слово для поиска: {search_by}")
    posts = [x for x in load_posts() if search_by.lower() in x['content'].lower()]
    return render_template("post_list.html", search_by=search_by, posts=posts)
