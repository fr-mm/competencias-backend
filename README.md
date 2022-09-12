# competencias-backend
Backend do projeto de TCC do curso técninco de Desenvolvimento de Sistemas do SENAI Cetind.

# Índice
- [Sobre](#Sobre)
- [Uso](#Uso)
- [Dependências](#Dependências)
- [Convenções](#Convenções)
- [Estrutura](#Estrutura)
- [Como desenvolver](#Como-desenvolver)

# Sobre
## Objetivo
Automatizar a planinlha de competência de docentes utilizada pelo SENAI.

## Turma
- G77166 (segundo semestre de 2022)

## Integrantes
- Ariely Floquet
- Francisco Mascrenhas
- Rafael Vecchi

# Rotas da API
## Raiz (acessando do localhost)
http://localhost:8000/apiv1/

## Rotas
#### docentes/
- **GET**: lista todos os docentes ativos
- **POST**: cria um novo docente a partir do request

#### docentes/{id}/
- **GET**: retorna docente 
- **POST**: atualiza docente de acordo com o payload da request
- **DELETE**: desativa docente

# Uso
Pelo Linux, os comandos a seguir devem ser precedidos por `sudo` para dar
permissão de administrador. 

Pelo Windows, rodar pelo Powershell iniciado como administrador ou usar
a interface gráfica do Docker (Docker Desktop)

### Construir as imagens
```
docker compose build
```
### Ativar containers 
acrescente `-d` ao final para rodar no plano de fundo
```
docker compose up
```
### Desativar containers
```
docker compose down
```
### Iniciar um terminal de dentro do container web
```
docker exec -it web bash
```
### Rodar testes
No terminal do container web
```
pytest
```

# Dependências
## Externas
Versões compatíveis dessas dependências precisam estar instaladas para rodar o projeto.
- [Python 3.10.6](https://python.org/downloads/release/python-3106/) (linguagem usada)
- [Docker 20.10.17](https://docs.docker.com/engine/release-notes/#201017) (administra ambientes isolados)

## Internas
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

# Convenções
## Cases
### SNAKE_CASE_MAIUSCULO
- constantes
### PascalCase
- classes
### snake_case
- todo o resto

## Testes
### Estrutura de diretórios
O diretório de testes unitários deve espelhar a estrutura que o projeto 
(módulos dominio e aplicacao)

### Convenções para o Pytest reconhecer os testes
As três convenções abaixo servem para que os testes sejam identificados pelo Pytest:
- O nome dos arquivos contento testes deve começar com `test_`
- O nome das classes de teste deve começar com `Test`
- O nome dos métodos de teste deve começar com `test_`

### Estrutura de um teste
#### Nome da classe
Deve haveer uma classe de teste para cada classe a ser testada, de mesmo nome. A entidade `Docente`, por
exemplo, será testada pela classe `TestDocente`

#### Nome do método
Deve ser dividido em três partes
- O QUE: nome do método a ser testado
- QUANDO: situação a ser testada
- ENTAO: resultado esperado  

Exemplo: queremos testar se o método `construir` do `Docente` cria e atribui uma nova `IdDeDocente` quando
a `id` não é informada. O nome do teste seria:
```
class TestDocente(TestCase):
    def test_construir_QUANDO_id_nao_informado_ENTAO_atribui_id_criado(self) -> None:
```
*Escrever QUANDO e ENTAO em maiúsculo mesmo

#### Corpo do método
Deve ser dividido em três partes separadas por uma linha em branco:
- ATRIBUIR: construir o cenário do teste
- AGIR: chamar o método a ser testado
- AFIRMAR: comparar o resultado com o esperado

Exemplo: queremos testar se o método `para_entidade` do `OTDDocente` retorna a entidade esperada
(consideremos que `Docente` tenha um único atributo `nome`):
```
# ATRIBUIR
otd_docente = OTDDocente(nome='Nome do Docente')

# AGIR
docente_resultante = otd_docente.para_entidade()

# AFIRMAR
docente_esperado = Docente(nome=otd.nome)
self.assertEqual(docente_resultante, docente_esperado)
```
*Não incluir comentários

## Nomes
### Idioma
Sempre em portugês sem acento, a menos quando referencia algo externo
(nesse caso deve usar o nome original)

### Formato
- Começar o nome de uma classe sempre como O QUE ela é, seguido de DO QUE ela é
- Não usar acento
- Omitir a palavra 'de'
#### Exemplos
- Um modelo de docente deve chamar-se ModeloDocente
- Uma fábrica de testes de modelo de docente deve chamar-se FabricaTesteModeloDocente

### Imports
Sempre que possível, organizar do mais externo (no topo) para o mais interno. 
Dividir em três sessões separadas por um espaço:
#### Topo
`from __future__ import annotations`
#### Meio
Demais imports externos (não criados por nós)
#### Abaixo
Imports de nossas criações (dominio ou aplicacao)

# Estrutura
## apllicacao
Essa camada é a ponte entre nosso domínio (ver abaixo) e a aplicação Django. É composta por:

### container
No container ficam instanciadas classes que dependem de outras classes externas ao domínio,
por exemplo: repositórios concretos, casos de uso.

### migrations
Migrações do banco de dados. Ao alterar a forma que as entidades são representadas 
no banco de dados, fazemos as migrações (para atualizar o banco) rodando os
comandos `python manage.py makemigrations` e `python manage.py migrate`
(dentro do container do Docker)

#### models
Aqui ficam as representações das nossas entidades no banco de dados.

#### repositorios
Aqui ficam os repositórios concretos que implementam os repositórios abstratos
contidos no domínio

#### serializers
Serializers são responsáveis por converter entre OTD e JSON, traduzindo entre
informações entre nossos casos de uso e a API.
#### urls
Contém as rotas da nossa API. Para evitar problemas caso um dia a
API venha a mudar, devemos separar por versões. A princípio iremos 
construir as rotas da apiv1 (versão 1 da API).
#### views
Aqui ficam as funções chamadas pelo sistema quando uma request
for requisitada em uma rota. É onde fica a lógica da API.

## competencias_backend
Aqui ficam as configurações gerais do Django. A princípio não vamos mexer aqui.

## dominio
Nessa camada vamos descrever nossa lógica de negócio em python puro. Ela deve ser
independente e isolada do mundo externo, ou seja, não pode importar nada de fora.
Faremos isso para isolar nossa lógica de negócio da lógica de infraestrutura. Devemos discutir
como organiza-la e documentar nossas decisões nesse arquivo README. Nosso trabalho 
aconotecerá nessa camada na maior parte do tempo. A princípio, nela temos:

#### casos_de_uso
Aqui ficam classes que representam os casos de uso definidos na modelagem.
A lógica de negócios está centralizda aqui, e são essas classes que serão
chamadas quando alguma tarefa for requisitada. Essas classes devem conter
um único método público chamado 'executar'.

#### entidades
Essa é a fonte da verdade quantos às nossas entidades. Elas serão manipuladas
ao realizar as tarefas, as outras representações são meramente reflexos das
entidades aqui descritas.

#### erros
Nossos erros customizados. Um erro não é necessariamente um bug. Erros são
esperados e carregam informações, e serão tratados pelo sistema. Todos os
erros de domínio devem herdar da classe ErroDeDominio, para que fique clara
a separação entre nossos erros customizados e os demais.

#### objetos_de_valor
São classes muito simples (@dataclass) que representam atributos de nossas entidades.
Elas devem ser capazes de se auto-validar e se comparar. Por exemplo, numa etidade 'Pessoa'
com um atributo 'nome', esse atributo não seria uma string, e sim o objeto de valor
chamado 'NomeDePessoa'. Ao instanciar esse objeto, ele faria as validações necessárias
e lançaria um erro caso o nome fosse inválido.

#### otds
OTD (Objeto de Transferência de Dados) são a última fronteira entre o
domínio e mundo externo. Casos de uso recebem e retornam OTDs.
Serializers os traduzem.

#### repositorios
Repositórios são responsáveis por guardar objetos. 
Aqui ficam classes abstratas (que cumprem o papel de interfaces) dos
repositórios. As classes concretas serão implementadas na camada de aplicação,
pois irão lidar com questões da infraestrutura (banco de dados). Declaramos
essas interfaces no domínio para que possamos fazer referência a elas sem
'sujar' o domínio com lógica de infraestrutura.

## testes
Aqui ficam os testes do projeto. É de extrema importância que tudo seja testado.
Antes de submeter qualquer alteração é preciso rodar os testes e verificar
que todos estão passando. A estrutura desse diretório é a seguinte:

#### fabricas  
Aqui ficam guardadas as fábricas de teste. Elas existem para facilitar a testagem.

#### integracao  
Testes de integração têm o objetivo de testar a aplicação como um todo, 
com todas as partes integradas

#### unitarios
Testes unitários têm o objetivo de testar cada mínima parte de forma isolada.
Cada classe, método e função devem ser testados exaustivamente.

## .env.dev
O Docker usa esse arquivo para definir as variáveis de ambiente.

## .gitignore
O Git usa esse arquivo para saber quais pastas e arquivos devem ser ignorados 
pelo versionamento.

## docker-compose.yml
Esse arquivo descreve os serviços, redes e volumes da aplicação Docker.

## Dockerfile
É basicamente um script que o Docker usa para construir uma imagem.

### manage.py
É a porta de entrada da aplicação Django. Usamos ele para executar uma série de 
tarefas do Django. Rodar esse arquivo (`python manage.py`) traz uma lista de
comandos possíveis. Para rodar o servidor, por exemplo, usamos o comando 
`python manage.py runserver`. O Docker roda o servidor automaticamente ao
ativar um container, mas para outras tarefas, como migraçã de banco de dados,
iremos usá-lo manualmente (de dentro do container).

## poetry.lock
Arquivo usado pelo Poetry para previnir atualizações indesejáveis das dependências,
garantindo assim um ambiente estável e previsível.

## pyproject.toml
Arquivo usado pelo Poetry que contém informações do projeto e suas dependências.

# Como desenvolver
## Criando um objeto de valor
#### domínio
- criar classe em `dominio/objetos_de_valor/`
- criar testes (quando necessário) em `testes/unitarios/dominios/objetos_de_valor/`
- criar fabrica teste em `testes/fabricas/dominio/objetos_de_valor/`
- atualizar entidade que irá conter o objeto de valor criado em `dominio/entidades/`
(ex: atualizar `Docente` para incluir `EmailDeDocente`)
- atualizar fabrica teste da entidade modificada em `testes/fabricas/dominio/entidades/`
- atualizar testes da entidade modificada em `testes/unitarios/dominio/entidades/`
- atualizar OTD da entidade para incluir novo objeto de valor em `dominio/otds/`
- atualizar testes dos OTDs modificados em `testes/unitarios/dominio/otds/`
#### aplicação
- atualizar modelo da entidade em `aplicacao/models/`
- atualizar testes do modelo modificado em `testes/unitarios/aplicacao/models/`
- atualizar fabrica teste do modelo modificado em `testes/fabricas/aplicacao/models/`
- migrar modelo atualizado para o banco de dados. Executar no terminal do Docker container: 
`python manage.py makemigrations` e `python manage.py migrate`
- atualizar serializer dos OTDs referentes à entidade modificada em `aplicacao/serializers/`












