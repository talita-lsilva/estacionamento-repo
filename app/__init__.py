from flask import Flask
from .extensions import mongo

def create_app():
    app = Flask(__name__)
    #app.config["MONGO_URI"] = "mongodb+srv://teste:<BF3BCDBE>@estacionamento.wisalig.mongodb.net/estacionamento?retryWrites=true&w=majority&appName=Estacionamento"
    #app.config["MONGO_URI"] = "mongodb+srv://teste:BF3BCDBE@estacionamento.wisalig.mongodb.net/?retryWrites=true&w=majority&appName=Estacionamento"
    app.config["MONGO_URI"] = "mongodb+srv://teste:BF3BCDBE@estacionamento.wisalig.mongodb.net/estacionamento?retryWrites=true&w=majority&appName=Estacionamento"

    mongo.init_app(app)
    app.mongo = mongo  # <<< aqui adiciona mongo ao app
    
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

