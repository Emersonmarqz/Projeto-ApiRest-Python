from flask import Flask ,app , request
from flask.json import jsonify
import json

app = Flask(__name__)

receitas = [
    {
        "Título": "Bolo01",
        "Lista de ingredientes": [
            "ingrediente01"
            "ingrediente02"
            "ingrediente03"
        ],
        "modo": "modo01",
        "Redimento": "Redimento01"
    },
]
@app.route("/cadastro", methods=["POST","GET"])
def Cadastro():
    if request.method == "GET":
        return jsonify(receitas)
    elif request.method == "POST":
        newcadastro = json.loads(request.data)
        receitas.append(newcadastro)
        return jsonify({
            "menssagem" : "Cadastrado",
            "newValue": newcadastro

        }) 
   
@app.route('/cadastro/<int:indice>', methods=['GET', 'PUT', 'DELETE'])
def cadastroID(indice):
    try:
        receitas[indice]
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
        return receitas[indice]

    elif request.method == 'PUT':
       
        newValue = json.loads(request.data)

        receitas[indice] = newValue
        return jsonify({
            "message": "Updated!",
            "newValue": newValue
        })
    elif request.method == 'DELETE':
        print(indice)
        receitas.pop(indice)
        return jsonify({
            "message": "Deleted!",
            "arrayAtual": receitas
        })

if __name__ == '__main__':
    app.run(debug=True)

  



