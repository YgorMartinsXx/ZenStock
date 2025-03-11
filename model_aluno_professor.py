dados = {
    "alunos": [
        {"nome": "lucas", "id": 15},
        {"nome": "cicero", "id": 29},
    ], 
    "professores": []
}

# Exceções personalizadas
class AlunoNaoEncontrado(Exception):
    pass

class ProfessorNaoEncontrado(Exception):
    pass

# Funções para Alunos
def aluno_por_id(id_aluno):
    for aluno in dados["alunos"]:
        if aluno["id"] == id_aluno:
            return aluno
    raise AlunoNaoEncontrado

def aluno_existe(id_aluno):
    try:
        aluno_por_id(id_aluno)
        return True
    except AlunoNaoEncontrado:
        return False

def adiciona_aluno(aluno_dict):
    dados["alunos"].append(aluno_dict)

def lista_alunos():
    return dados["alunos"]

def apaga_tudo():
    dados["alunos"] = []
    dados["professores"] = []  # Limpa também os dados dos professores

def deleta_aluno_por_id(id_aluno):
    for aluno in dados["alunos"]:
        if aluno["id"] == id_aluno:
            dados["alunos"].remove(aluno)
            return True
    return False

def edita_aluno_por_id(id_aluno, novo_dado):
    for aluno in dados["alunos"]:
        if aluno["id"] == id_aluno:
            aluno.update(novo_dado)
            return True
    return False


# Funções para Professores
def professor_por_id(id_professor):
    for professor in dados["professores"]:
        if professor["id"] == id_professor:
            return professor
    raise ProfessorNaoEncontrado

def professor_existe(id_professor):
    try:
        professor_por_id(id_professor)
        return True
    except ProfessorNaoEncontrado:
        return False

def adiciona_professor(professor_dict):
    dados["professores"].append(professor_dict)

def lista_professores():
    return dados["professores"]

def deleta_professor_por_id(id_professor):
    for professor in dados["professores"]:
        if professor["id"] == id_professor:
            dados["professores"].remove(professor)
            return True
    return False

def edita_professor_por_id(id_professor, novo_dado):
    for professor in dados["professores"]:
        if professor["id"] == id_professor:
            professor.update(novo_dado)
            return True
    return False
