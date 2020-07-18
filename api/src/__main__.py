from src import FLASK_PORT
from src.auto_rotate import connexion_app


if __name__ == '__main__':
    connexion_app.run(host='0.0.0.0', port=FLASK_PORT)
