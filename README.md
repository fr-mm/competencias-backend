# competencias-backend
Backend do projeto de TCC do curso técninco de Desenvolvimento de Sistemas do SENAI Cetind.

## Objetivo
Automatizar a planinlha de competência de docentes utilizada pelo SENAI.

## Turma
- G77166 (segundo semestre de 2022)

## Integrantes
- Ariely Floquet
- Francisco Mascrenhas
- Rafael Vecchi

# Uso
Pelo Linux, os comandos a seguir devem ser precedidos por `sudo` para dar
permissão de administrador. 

Pelo Windows, rodar pelo Powershell iniciado como administrador ou usar
a interface gráfica do Docker (Docker Desktop)

Construir as imagens:
```
docker compose build
```
Ativar containers (acrescente `-d` ao final para rodar no plano de fundo):
```
docker compose up
```
Desativar containers:
```
docker compose down
```

# Sobre o projeto
## Dependências
### Externas
Versões compatíveis dessas dependências precisam estar instaladas para rodar o projeto.
- [Python 3.10.6](https://python.org/downloads/release/python-3106/) (linguagem usada)
- [Docker 20.10.17](https://docs.docker.com/engine/release-notes/#201017) (administra ambientes isolados)

### Internas
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

## Estrutura
### apllicacao
Essa camada é a ponte entre nosso domínio (ver abaixo) e a aplicação Django. É composta por:

#### migrations
Migrações do banco de dados. Ao alterar a forma que as entidades são representadas 
no banco de dados, fazemos as migrações (para atualizar o banco) rodando os
comandos `python manage.py makemigrations` e `python manage.py migrate`
(dentro do container do Docker)

- #### models
Aqui ficam as representações das nossas entidades no banco de dados.

- #### serializers
Serializers são responsáveis por formatar as entidades em 
JSON (Javascript Object Notation), formato usado pela API para
comunicar os dados.
- #### urls
Contém as rotas da nossa API. Para evitar problemas caso um dia a
API venha a mudar, devemos separar por versões. A princípio iremos 
construir as rotas da apiv1 (versão 1 da API).
- #### views
Aqui ficam as funções chamadas pelo sistema quando uma request
for requisitada em uma rota. É onde fica a lógica da API.

### competencias_backend
Aqui ficam as configurações gerais do Django. A princípio não vamos mexer aqui.

### dominio
Nessa camada vamos descrever nossa lógica de negócio em python puro. Ela deve ser
independente e isolada do mundo externo, ou seja, não pode importar nada de fora.
Faremos isso para isolar nossa lógica de negócio da infraestrutura. Devemos discutir
como organiza-la e documentar nossas decisões nesse arquivo README. Nosso trabalho 
aconotecerá nessa camada, na maior parte do tempo. A estrutura desse diretório
é fruto de nossas decisões, e pode mudar caso julguemos conveniente. 
A princípio teremos:

- #### casos_de_uso
Aqui ficam classes que representam os casos de uso definidos na modelagem.
A lógica de negócios está centralizda aqui, e são essas classes que serão
chamadas quando alguma tarefa for requisitada. Essas classes devem conter
um único método público chamado 'executar'.

- #### entidades
Essa é a fonte da verdade quantos às nossas entidades. Elas serão manipuladas
ao realizar as tarefas, as outras representações são meramente reflexos das
entidades aqui descritas.

- #### erros
Nossos erros customizados. Um erro não é necessariamente um bug. Erros são
esperados e carregam informações, e serão tratados pelo sistema. Todos os
erros de domínio devem herdar da classe ErroDeDominio, para que fique clara
a separação entre nossos erros customizados e os demais.

- #### objetos_de_valor
São classes muito simples (@dataclass) que representam atributos de nossas entidades.
Elas devem ser capazes de se auto-validar e se comparar. Por exemplo, numa etidade 'Pessoa'
com um atributo 'nome', esse atributo não seria uma string, e sim o objeto de valor
chamado 'NomeDePessoa'. Ao instanciar esse objeto, ele faria as validações necessárias
e lançaria um erro caso o nome fosse inválido.

- #### repositorios
Repositórios são responsáveis por guardar objetos. 
Aqui ficam classes abstratas (que cumprem o papel de interfaces) dos
repositórios. As classes concretas serão implementadas na camada de aplicação,
pois irão lidar com questões da infraestrutura (banco de dados). Declaramos
essas interfaces no domínio para que possamos fazer referência a elas sem
'sujar' o domínio com lógica de infraestrutura.

### testes
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

### .env.dev
O Docker usa esse arquivo para definir as variáveis de ambiente.

### .gitignore
O Git usa esse arquivo para saber quais pastas e arquivos devem ser ignorados 
pelo versionamento.

### docker-compose.yml
Esse arquivo descreve os serviços, redes e volumes da aplicação Docker.

### Dockerfile
É basicamente um script que o Docker usa para construir uma imagem.

### manage.py
É a porta de entrada da aplicação Django. Usamos ele para executar uma série de 
tarefas do Django. Rodar esse arquivo (`python manage.py`) traz uma lista de
comandos possíveis. Para rodar o servidor, por exemplo, usamos o comando 
`python manage.py runserver`. O Docker roda o servidor automaticamente ao
ativar um container, mas para outras tarefas, como migraçã de banco de dados,
iremos usá-lo manualmente (de dentro do container).

### poetry.lock
Arquivo usado pelo Poetry para previnir atualizações indesejáveis das dependências,
garantindo assim um ambiente estável e previsível.

### pyproject.toml
Arquivo usado pelo Poetry que contém informações do projeto e suas dependências.
