import json  # импортируем библиотеку json

POST_PATH = "posts.json"


def load_posts():
    """Функция загружает json файл"""
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def upload_posts(posts):
    """Функция записывает данные в json файл"""
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file, indent=4)
