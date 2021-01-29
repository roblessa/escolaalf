from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

dados = {}

 # Rota para cadastrar o gabarito
@app.route('/prova/<int:id_prova>/', methods=['POST'])
def gabarito(id_prova):
    dados[id_prova] = {"gabarito": request.json}
    print(dados)
    return 'Gabarito cadastrado'

    total_nota = 0
    for question in request.json['questions']:
        if int(question['peso_question']) == 0:
            return jsonify('O peso da questao precisa ser maior do que 0.')
        total_nota += question['peso_question']
    if total_nota == 0 or total_nota <= 10:
        return jsonify('A nota esta correta.')

    for question in request.json['questions']:
        prova = Gabarito(
            id_prova = request.json ['id_pprova'],
            id_aluno =  request.json ['id_aluno'],
            aluno = request.json ['aluno'],
            num_questao = question ['num_questao'],
            peso_questao = question['peso_question'],
            alternativa = question['alternativa']

        )
        return jsonify('Gabarito cadastrado com sucesso.')
    else:
        return jsonify('Erro ao cadastrar gabarito.')

# Rota para cadastrar respostas dos alunos
@app.route('/prova/<int:id_prova>/aluno/<int:id_aluno>', methods=['POST'])
def aluno (id_prova, id_aluno):
    dados[id_prova] ={"respostas": []}
    if prova(id=request.json ['id_prova']):
        return jsonify('n existe')
    elif aluno(id=request.json ['id_aluno' >= 100]):
        return jsonify('A capacidade máxima de 100 alunos já foi registrada.')
    
    for aluno in request.json['resposta']:
        resposta = Respostas(
            id_prova = request.json ['id_pprova'],
            id_aluno =  request.json ['id_aluno'],
            aluno = request.json ['aluno'],
            num_questao = question ['num_questao'],
            alternativa = question ['alternativa']
        )
        return jsonify('ok')

# Rota para cadastrar notas dos alunos
@app.route('/aluno/<int:ID_ALUNO>/nota_final', methods=['GET'])
def nota_final(id_aluno):
    prova_aluno = filter(id_aluno, id_prova)
    nota_final = 0
    for gabarito in id_prova:
         nota_prova = 0
         resposta = filter(id_prova=prova, id_aluno=prova.aluno).all()
         gabarito = filter(id_prova=prova).all()
    for resposta in resposta:
            for gabarito in gabarito:
                if resposta.num_questao == gabarito.num_questao:
                    if resposta.alternativa == gabarito.alternativa:
                        nota_prova += 1 * gabarito.peso_questao
                    break
            print(sum(nota_prova/len(resposta)))
    return jsonify(nota_final= int(nota_final))

# Rota com os aprovados
@app.route('/alunos/aprovados', methods=['GET'])
def alunos_aprovados():
    for aluno in aluno:
        if nota_final(aluno[0]).json()['nota_final'] < 7:
            aluno.append(aluno)
    wrapper.__name__ = func.__name__
    return jsonify(id_aluno_aprovado = aluno)


if __name__ == '__main__':
    app.run(debug=True)