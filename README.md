# Escola Alf
### Projeto

  A escola Alf aplica provas de múltipla escolha para os alunos. A nota do aluno na prova é determinada pela média ponderada das questões com os pesos de cada questão. Cada questão correta soma 1 ponto multiplicada pelo peso e cada questão errada 0. 
  A nota final é a média aritmética das notas de todas as provas.
  
  ### Recursos
  * Cadastro de provas
  * Cadastro de gabaritos 
  * Identificação de alunos e suas notas
  * Lista de Aprovados
  


### Instalação
* [Python] - É uma linguagem de programação que permite trabalhar rapidamente
e integrar sistemas de forma mais eficaz. 

* [Flask]:  É um micro framework que utiliza a linguagem Python para criar aplicativos Web
* [Postman] - É uma plataforma de colaboração para desenvolvimento de API. Seus recursos simplificam cada etapa da construção de uma API e otimizam a colaboração para criar APIs melhores.
* Para executar este projeto, utilizei o sistema operacional macOs e rodei tudo dentro de um virtual environment de Python3.
* Dentro do ambiente ativado, use o seguinte comando para instalar o Flask e Flask-RESTful


```sh
$ pip3 install Flask
$ pip3 install flask-restful
```

## Utilização 
#### Cadastrar Gabarito:
###### POST /prova 
Crie uma prova e cadastre o gabarito, com a nota total sendo maior que 0 e menor ou igual a 10. O peso de cada questão correta deve ser um  número inteiro sempre maior que 0. 

Exemplo: 
``` sh
gabarito = [
{
    "1": {
        "gabarito": {
            "1": 1, 
            "2": 1, 
            "3": 2, 
            "4": 2
            }
            };
```


###### POST/prova/aluno
Registra as respostas dos alunos.

Exemplo:
``` sh
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
            }
            ];
```

###### GET/aluno/nota_final
Retornas as notas dos alunos.

Exemplo: 
``` sh
{
"nota_final": 7
};
``` 
###### GET/ alunos/aprovados
Retorna o nome e matrícula de cada aluno aprovado.

Exemplo:
``` sh
{
"alunos_aprovados": [4, Miguel]
};
```






   [Python]: <https://www.python.org/>
   [Flask]: <https://flask.palletsprojects.com/en/1.1.x/>
   [Postman]: <https://www.postman.com/> 
   
