from flask import Flask, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint

# импортируем все что нужно

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


# регистриуем Blueprintы

@app.route("/uploads/images/<path:path>")  # вьюшка для открытия папки к просмотру
def static_dir(path):
    return send_from_directory("uploads/images", path)


if __name__ == "__main__":  # запуск app
    app.run()
