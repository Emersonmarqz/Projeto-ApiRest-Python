from flask import Flask ,app , request
from flask.json import jsonify
import json

app = Flask(__name__)

ListaReceitas = [
    {
        "Título": "Bolo",
        "Lista de ingredientes": [
            "Manteiga"
            "2 ovos"
            "Trigo"
        ],
        "modo": "para preparar, basta ligar o forno e colocar o bolo.",
        "Redimento": "Rende 3 fatias."
    },
]
@app.route("/rotaApiRest", methods=["POST","GET"])
def Cadastro():
    if request.method == "GET":
        return jsonify(ListaReceitas)
    elif request.method == "POST":
        newcadastro = json.loads(request.data)
        ListaReceitas.append(newcadastro)
        return jsonify({
            "menssagem" : "Cadastrado",
            "newValue": newcadastro

        }) 
   
@app.route('/rotaApiRest/<int:indice>', methods=['GET', 'PUT', 'DELETE'])
def cadastroID(indice):
    try:
        ListaReceitas[indice]
    except IndexError:
        message = 'Receita ID {} Não Encontrada'.format(indice)
        return jsonify({
            "message": message,
            "status": "Error!"
        })
    except:
        message = 'Aconteceu um erro inesperado'
        return jsonify({
            "message": message,
            "status": "Error!"
        })
    
    if request.method == 'GET':
        return ListaReceitas[indice]

    elif request.method == 'PUT':
       
        newValue = json.loads(request.data)

        ListaReceitas[indice] = newValue
        return jsonify({
            "message": "Updated!",
            "newValue": newValue
        })
    elif request.method == 'DELETE':
        print(indice)
        ListaReceitas.pop(indice)
        return jsonify({
            "message": "Deleted!",
            "arrayAtual": ListaReceitas
        })

if __name__ == '__main__':
    app.run(debug=True)

  



