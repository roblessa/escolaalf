from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


gabarito = [
{
    "1": {
        "gabarito": {
            "1": 1, 
            "2": 1, 
            "3": 2, 
            "4": 2
            },
        "respostas": [
            {
                "aluno_id": "1",
                "aluno": "Joao",
                "respostas": {
                    "1": 4,
                    "2": 1,
                    "3": 2,
                    "1": 2
                }
            },
            {
                "aluno_id": "2",
                "aluno": "Ana",
                "respostas": {
                    "1": 2,
                    "2": 1,
                    "3": 2,
                    "1": 2
                }
            },
            {
                "aluno_id": "3",
                "aluno": "Maria",
                "respostas": {
                    "1": 1,
                    "2": 3,
                    "3": 2,
                    "1": 2
                }
            },
            {
                "aluno_id": "4",
                "aluno": "Miguel",
                "respostas": {
                    "1": 2,
                    "2": 3,
                    "3": 3,
                    "1": 2
                }
            },
        ]
    }
},

{
    "2": {
        "gabarito": {
            "1": 2, 
            "2": 2, 
            "3": 1, 
            "4": 3
            },
        "respostas": [
            {
                "aluno_id": "1",
                "aluno": "Joao",
                "respostas": {
                    "1": 2,
                    "2": 2,
                    "3": 1,
                    "1": 2
                }
            },
            {
                "aluno_id": "2",
                "aluno": "Ana",
                "respostas": {
                    "1": 3,
                    "2": 2,
                    "3": 1,
                    "1": 2
                }
            },
            {
                "aluno_id": "3",
                "aluno": "Maria",
                "respostas": {
                    "1": 2,
                    "2": 3,
                    "3": 1,
                    "1": 3
                }
            },
            {
                "aluno_id": "4",
                "aluno": "Miguel",
                "respostas": {
                    "1": 2,
                    "2": 3,
                    "3": 1,
                    "1": 2
                }
            },
        ]
    }
},

{
    "3": {
        "gabarito": {
            "1": 1, 
            "2": 2, 
            "3": 4, 
            "4": 3
            },
        "respostas": [
            {
                "aluno_id": "1",
                "aluno": "Joao",
                "respostas": {
                    "1": 1,
                    "2": 4,
                    "3": 3,
                    "1": 3
                }
            },
            {
                "aluno_id": "2",
                "aluno": "Ana",
                "respostas": {
                    "1": 1,
                    "2": 2,
                    "3": 2,
                    "1": 3
                }
            },
            {
                "aluno_id": "3",
                "aluno": "Maria",
                "respostas": {
                    "1": 1,
                    "2": 2,
                    "3": 2,
                    "1": 1
                }
            },
            {
                "aluno_id": "4",
                "aluno": "Miguel",
                "respostas": {
                    "1": 2,
                    "2": 2,
                    "3": 1,
                    "1": 3
                }
            },
        ]
    }
}, 
]


{
"nota_final": 7
}

{
"alunos_aprovados": [4, Miguel]
}
