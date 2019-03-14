from flask import Flask
from routes import main as main_blueprint
from events import socketio
import secret


# socketio = SocketIO(app)

def configured_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret.secret_key
    app.debug = True

    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app


if __name__ == '__main__':
    app = configured_app()
    socketio.run(app, host='0.0.0.0', port=80)
