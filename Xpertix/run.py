import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import crear_app

app = crear_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
