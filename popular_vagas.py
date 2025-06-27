from flask import Flask
from app.extensions import mongo
from app.routes import layout
from app import create_app

app = create_app()

with app.app_context():
    mongo.db.vagas.delete_many({})  # Limpa qualquer dado antigo

    vagas = []
    idx = 0
    for row in layout:
        for cell in row:
            if cell is not None:
                vagas.append({
                    "idx": idx,
                    "identificador": str(cell),
                    "ocupada": False,
                    "chassi": "",
                    "modelo": "",
                    "ocupada_em": None
                })
                idx += 1

    mongo.db.vagas.insert_many(vagas)
    print(f"{len(vagas)} vagas inseridas com sucesso.")
