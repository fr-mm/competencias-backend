# competencias-backend
Backend do projeto de TCC do curso técninco de Desenvolvimento de Sistemas do SENAI Cetind.

### Objetivo
Automatizar a planinlha de competência de docentes utilizada pelo SENAI.

### Turma
- G77166 (segundo semestre de 2022)

### Integrantes
- Ariely Floquet
- Francisco Mascrenhas
- Rafael Vecchi

## Uso
### Linux
Construir as imagens:
```
sudo docker compose build
```
Ativar containers (acrescente `-d` ao final para rodar no plano de fundo):
```
sudo docker compose up
```
Desativar containers:
```
sudo docker compose down
```

## Sobre o projeto
### Dependências
#### Externas
Versões compatíveis dessas dependências precisam estar instaladas para rodar o projeto.
- [Python 3.10.6](https://python.org/downloads/release/python-3106/) (linguagem usada)
- [Docker 20.10.17](https://docs.docker.com/engine/release-notes/#201017) (administra ambientes isolados)

#### Internas
O Docker irá instalar essas dependências
- [Poetry 1.1.14](https://python-poetry.org/blog/announcing-poetry-1.1.14/) (gerenciador de pacotes)
- [Django 4.1](https://docs.djangoproject.com/en/4.1/releases/4.1/) (framework web)
- [Django Rest Framework 3.13.1](https://www.django-rest-framework.org/community/release-notes/#313x-series) (framework REST API)
- [PostgreSQL 14.4](https://www.postgresql.org/docs/current/release-14-4.html) (banco de dados)
- [psycopg2-binary 2.9.3](https://pypi.org/project/psycopg2-binary/) (requisito do PostgreSQL) 
- [Pytest 7.1.2](https://docs.pytest.org/en/7.1.x/) (framework de testes)
- [Pytest Django 4.5.2](https://pytest-django.readthedocs.io/en/latest/) (plugin para testar aplicação Django com Pytest)
- [Mockito 1.3.5](https://pypi.org/project/mockito/) (framework para mock e spy em testes)
- [Factory Boy 3.2.1](https://factoryboy.readthedocs.io/en/stable/) (ferramentas para criar fábricas de teste)

### Estrutura
#### api
Nessa camada deveremos criar a API, assim como liga-la ao domínio. Deve conter:
- rotas (endererços das endpoints)
- views (funções chamadas quando as rotas recebem request)
- serializers (traduzem entre linguagem de API e de domínio)
  <br><br>

#### competencias_backend
Aqui ficam as configurações gerais do Django. A princípio não vamos mexer aqui.
<br><br>

#### dominio
Nessa camada vamos descrever nossa lógica de negócio em python puro. Ela deve ser
independente e isolada do mundo externo, ou seja, não pode importar nada de fora.
Faremos isso para isolar nossa lógica de negócio da infraestrutura. Devemos discutir
como organiza-la e documentar nossas decisões nesse arquivo README. Nosso trabalho 
aconotecerá nessa camada, na maior parte do tempo.

#### testes
Aqui ficam os testes do projeto. É de extrema importância que tudo seja testado.
Antes de submeter qualquer alteração é preciso rodar os testes e verificar
que todos estão passando. A estrutura desse diretório é a seguinte:

- #### fabricas  
Aqui ficam guardadas as fábricas de teste. Elas existem para facilitar a testagem.

- #### integracao  
Testes de integração têm o objetivo de testar a aplicação como um todo, 
com todas as partes integradas

- #### unitarios
Testes unitários têm o objetivo de testar cada mínima parte de forma isolada.
Cada classe, método e função devem ser testados exaustivamente.
<br><br>

#### .env.dev
O Docker usa esse arquivo para definir as variáveis de ambiente.
<br><br>

#### .gitignore
O Git usa esse arquivo para saber quais pastas e arquivos devem ser ignorados 
pelo versionamento.
<br><br>

#### docker-compose.yml
Esse arquivo descreve os serviços, redes e volumes da aplicação Docker.
<br><br>

#### Dockerfile
É basicamente um script que o Docker usa para construir uma imagem.
<br><br>

#### manage.py
É a porta de entrada da aplicação Django. Usamos ele para executar uma série de 
tarefas do Django. Rodar esse arquivo (`python manage.py`) traz uma lista de
comandos possíveis. Para rodar o servidor, por exemplo, usamos o comando 
`python manage.py runserver`. O Docker roda o servidor automaticamente ao
ativar um container, mas para outras tarefas, como migraçã de banco de dados,
iremos usá-lo manualmente (de dentro do container).
<br><br>

#### poetry.lock
Arquivo usado pelo Poetry para previnir atualizações indesejáveis das dependências,
garantindo assim um ambiente estável e previsível.
<br><br>

#### pyproject.toml
Arquivo usado pelo Poetry que contém informações do projeto e suas dependências.
<br><br>
