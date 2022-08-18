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
- [PostgreSQL 14.4](https://www.postgresql.org/docs/current/release-14-4.html) (banco de dados)

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
