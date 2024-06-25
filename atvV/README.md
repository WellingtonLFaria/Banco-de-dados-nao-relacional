# Atividade 4

Crie uma conta gratuita no Neo4j https://neo4j.com AuraDB

1. Implemente em Python as funções de manipulação da Base de Dados Não Relacional do Mercado Livre (EX1) no Neo4j

    a. Insert em todas as coleções (Usuário, Vendedor, Produto, Compra)

    b. Search em todas as coleções


## Instalando as dependências
```bash
pip install -r requirements.txt
```

## Configurando as variáveis de ambiente

Crie o arquivo .env dentro do diretório ./src, e adicione as seguintes variáveis:
```bash
URI="<uri_da_instância_do_neo4j>"
USERNAMEDB="neo4j"
PASSWORD="<senha_da_instância_do_neo4j>"
```

## Executando o projeto
```bash
python ./src/main.py
```