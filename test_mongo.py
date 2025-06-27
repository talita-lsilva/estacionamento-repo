from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://teste:BF3BCDBE@estacionamento.wisalig.mongodb.net/?retryWrites=true&w=majority&appName=Estacionamento"

mongo = PyMongo(app)

try:
    print("Conectando...")
    mongo.db.vagas.find_one()  # apenas para forçar a conexão
    print("✅ Conectado com sucesso!")
except Exception as e:
    print("❌ Erro de conexão:", e)
