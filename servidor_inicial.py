from flask import Flask, request, jsonify
import model_aluno_professor as model

app = Flask(__name__)

@app.route("/") 
def hello():
    return "Hello World!"

@app.route("/alunos", methods=["GET"])
def alunos():
    return jsonify(model.lista_alunos())

@app.route("/alunos/<int:nAluno>", methods=["GET"]) 
def alunoPorId(nAluno):
    try:
        return jsonify(model.aluno_por_id(nAluno))
    except model.AlunoNaoEncontrado:
        return jsonify({"erro": "aluno nao encontrado"}), 400


@app.route("/alunos", methods=["POST"])
def cria_aluno():
    aluno_dict = request.json

    # Verifica se o ID está presente e é um número inteiro
    try:
        aluno_dict["id"] = int(aluno_dict["id"])
    except (ValueError, KeyError):
        return jsonify({"erro": "id inválido"}), 400

    # Verifica se o nome está presente e não está vazio
    if "nome" not in aluno_dict or not aluno_dict["nome"].strip():
        return jsonify({"erro": "aluno sem nome"}), 400

    # Se o ID já existir, retorna erro 400
    if model.aluno_existe(aluno_dict["id"]):
        return jsonify({"erro": "id ja utilizada"}), 400

    model.adiciona_aluno(aluno_dict)
    return jsonify({"mensagem": "aluno criado com sucesso"}), 200


@app.route("/reseta", methods=["POST", "DELETE"])
def reseta():
    model.apaga_tudo()
    return jsonify({"mensagem": "resetado"}), 200

@app.route("/alunos/<int:nAluno>", methods=["DELETE"])
def deletaAlunoPorId(nAluno):
    if model.deleta_aluno_por_id(nAluno):  
        return jsonify({"Sucesso": "aluno deletado"}), 200
    return jsonify({"erro": "aluno nao encontrado"}), 400

@app.route("/alunos/<int:nAluno>", methods=["PUT"])
def editaAlunoPorId(nAluno):
    aluno_dict = request.json

    # Verifica se o aluno existe antes de tentar editar
    if not model.aluno_existe(nAluno):
        return jsonify({"erro": "aluno nao encontrado"}), 400

    # Verifica se o nome está presente e não está vazio
    if "nome" not in aluno_dict or not aluno_dict["nome"].strip():
        return jsonify({"erro": "aluno sem nome"}), 400

    # Edita o aluno removendo o antigo e adicionando a versão nova
    model.deleta_aluno_por_id(nAluno)
    model.adiciona_aluno(aluno_dict)

    return jsonify({"mensagem": "aluno editado com sucesso", "alunos": model.lista_alunos()}), 200


@app.route("/professores", methods=["GET", "POST"])
def gerencia_professores():
    if request.method == "GET":
        # Retorna todos os professores
        professores = model.lista_professores()
        return jsonify(professores), 200

    elif request.method == "POST":
        data = request.json
        if "nome" not in data or "id" not in data:
            return jsonify({"erro": "professor sem nome"}), 400
        if model.professor_existe(data["id"]):
            return jsonify({"erro": "id ja utilizada"}), 400
        model.adiciona_professor(data)
        return jsonify(data), 200

@app.route("/professores/<int:id_professor>", methods=["GET", "PUT", "DELETE"])
def manipula_professor(id_professor):
    professor = None
    try:
        professor = model.professor_por_id(id_professor)
    except model.ProfessorNaoEncontrado:
        return jsonify({"erro": "professor nao encontrado"}), 400

    if request.method == "GET":
        return jsonify(professor), 200

    elif request.method == "PUT":
        data = request.json
        if "nome" not in data:
            return jsonify({"erro": "professor sem nome"}), 400
        model.edita_professor_por_id(id_professor, data)
        return jsonify(data), 200

    elif request.method == "DELETE":
        if model.deleta_professor_por_id(id_professor):
            return jsonify({"mensagem": "professor removido"}), 200
        return jsonify({"erro": "professor nao encontrado"}), 400
    

if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
