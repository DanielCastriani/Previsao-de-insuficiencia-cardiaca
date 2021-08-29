# https://github.com/DanielCastriani/Previsao-de-insuficiencia-cardiaca

from flask import Flask
from flask.helpers import send_from_directory

from model.train_test import train_test_pipeline
from database.load_dataset import load_dataset
from eda.plots import plots

app = Flask(__name__,
            static_url_path='/public',
            static_folder='public')


@app.route("/public/<path:path>")
def public_dir(path):
    return send_from_directory("public", path)


@app.route('/train_test')
def train_test_endpoint():

    heart_failure = load_dataset()
    plots(heart_failure, show=False)

    train_test_pipeline(heart_failure, show=False)

    return 'Modelo treinado', 200


if __name__ == '__main__':
    app.run()
