dados = {"alunos":[
                   {"nome":"lucas","id":15},
                   {"nome":"cicero","id":29},
                  ], 
        "professores":[]
        }

class AlunoNaoEncontrado(Exception):
    pass #palavra-chave que serve como uma instrução nula, ou seja, não faz nada

def aluno_por_id(id_aluno):
    lista_alunos = dados['alunos']
    for dicionario in lista_alunos:
        if dicionario['id'] == id_aluno:
            return dicionario
    raise AlunoNaoEncontrado

def aluno_existe(id_aluno):
    try:
        aluno_por_id(id_aluno)
        return True
    except AlunoNaoEncontrado:
        return False

def deleta_por_id(id_aluno):
    lista_alunos = dados['alunos']
    for index, aluno in enumerate(lista_alunos):
        if aluno["id"] == id_aluno:
            dados['alunos'].pop(index)
            return
        
    raise AlunoNaoEncontrado(f"Aluno com ID {id_aluno} não encontrado")
    

def adiciona_aluno(dict):
    dados['alunos'].append(dict)

def lista_alunos():
    return dados["alunos"]

def apaga_tudo():
    dados['alunos'] = []