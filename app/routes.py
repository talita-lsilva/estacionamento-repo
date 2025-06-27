from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime, timedelta
from .extensions import mongo  # importar mongo direto
import pytz

main = Blueprint('main', __name__)
fuso_br = pytz.timezone('America/Sao_Paulo')

# Criação do layout do estacionamento
# None = espaço vazio (rua), 0 = vaga sem número, n = vaga com número
layout = [
    [38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 'N4', 'N3', 'N2', 'N1', None],
    [None]*28 + [14],
    [None]*28 + [13],
    [None, None,39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, None, None, None, None,    12],
    [None, None,82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, None, None, None, None,   11],
    [None]*28 + [10],
    [None]*28 + [9],
    [None, None,83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, None, None, None, None,   8],
    [ None, None,None, None, None, None, None, None, None, None, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, None, None, None, None,    7],
    [None]*28 + [6],
    [ None, None,   None, None, None, None, None, None, None, None,"E", "E", "E", "E", "E", "E",None, 139, 140, 141, None, None, None, None, None,  None,None, None, 5],
    [None]*28 + [4],
    [None]*28 + [3],
    [None]*28 + [2],
    [None]*28 + [1],
]

@main.route('/', methods=['GET'])
def index():
    vagas = list(mongo.db.vagas.find())
    agora = datetime.now(fuso_br)
    for vaga in vagas:
        if vaga.get('ocupada') and vaga.get('ocupada_em'):
            vaga['ocupada_em_str'] = vaga['ocupada_em'].isoformat()
            vaga['alerta'] = (agora - vaga['ocupada_em'] > timedelta(days=5))
        else:
            vaga['ocupada_em_str'] = ''
            vaga['alerta'] = False

    layout_indices = []
    idx = 0
    for row in layout:
        row_indices = []
        for cell in row:
            if cell is not None:
                row_indices.append(idx)
                idx += 1
            else:
                row_indices.append(None)
        layout_indices.append(row_indices)

    total_livres = sum(1 for vaga in vagas if not vaga.get('ocupada'))
    total_ocupadas = sum(1 for vaga in vagas if vaga.get('ocupada'))
    total_alerta = sum(1 for vaga in vagas if vaga.get('alerta'))

    return render_template(
        'index.html',
        vagas=vagas,
        layout=layout,
        layout_indices=layout_indices,
        zip=zip,
        total_livres=total_livres,
        total_ocupadas=total_ocupadas,
        total_alerta=total_alerta
    )

@main.route('/ocupar', methods=['POST'])
def ocupar():
    try:
        idx = int(request.form['idx'])
        chassi = request.form['chassi']
        modelo = request.form['modelo']
        if not chassi or not modelo:
            return "Chassi e modelo são obrigatórios", 400
        agora = datetime.now(fuso_br)
        mongo.db.vagas.update_one(
            {"idx": idx},
            {"$set": {
                "ocupada": True,
                "chassi": chassi,
                "modelo": modelo,
                "ocupada_em": agora
            }},
            upsert=True
        )
    except Exception as e:
        return str(e), 500
    return redirect(url_for('main.index'))

@main.route('/liberar', methods=['POST'])
def liberar():
    try:
        idx = int(request.form['idx'])
        mongo.db.vagas.update_one(
            {"idx": idx},
            {"$set": {
                "ocupada": False,
                "chassi": "",
                "modelo": "",
                "ocupada_em": None
            }}
        )
    except Exception as e:
        return str(e), 500
    return redirect(url_for('main.index'))
