import logging
from flask import Blueprint, request, render_template
from functions import load_posts, upload_posts

# Импортируем все что нам нужно

logging.basicConfig(filename="basic.log", encoding='utf-8', level=logging.INFO)  # Настраиваем логирование

loader_blueprint = Blueprint('loader', __name__, url_prefix='/post', static_folder='static',
                             template_folder='templates')


@loader_blueprint.route('/form/')  # вьюшка добавление поста
def form():
    return render_template("post_form.html")


@loader_blueprint.route('/upload/', methods=['POST'])  # вьюшка добавленного поста
def upload():
    try:
        file = request.files['picture']
        filename = file.filename
        content = request.values['content']
        posts = load_posts()
        posts.append({
            'pic': f'uploads/images/{filename}',
            'content': content
        })
        upload_posts(posts)
        file.save(f'./uploads/images/{filename}')
        if filename.split('.')[-1] not in ['png', 'jpeg', 'jpg']:
            logging.info('Файл не изображение')
    except FileNotFoundError:
        logging.error("Ошибка при загрузке файла")
        return '<h1>Файл не найден</h1>'
    else:
        return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)
