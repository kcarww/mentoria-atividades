# Sistema de Vendas (Django + PostgreSQL)

Projeto Django para controle de produtos, estoque (entrada/saída) e
vendas, com autenticação via usuário administrativo (e-mail e senha).

------------------------------------------------------------------------

## Funcionalidades

### Produtos

-   Código (único)
-   Nome
-   Preço de custo
-   Preço de venda
-   Quantidade em estoque

### Estoque

Controle através de movimentações: 
- Tipo: ENTRADA ou SAIDA 
- Produto 
- Quantidade 
- Observação 
- Data/Hora

Regra: 
- ENTRADA → soma no estoque 
- SAIDA → subtrai do estoque (validando saldo)

------------------------------------------------------------------------

### Usuário Administrativo

-   Login com e-mail e senha
-   Acesso via Django Admin
-   Pode cadastrar produtos
-   Pode lançar vendas

------------------------------------------------------------------------

### Vendas

Fluxo: 
1. Seleciona cliente 
2. Adiciona produtos e quantidades 
3. Finaliza venda

Regras: 
- Não permite vender acima do estoque 
- Ao finalizar: 
- Debita o estoque 
- Cria movimentação de saída 
- Gera nota em TXT

------------------------------------------------------------------------

## Estrutura do Projeto

sales_system/ ├── manage.py ├── config/ ├── apps/ │ ├── accounts/ │ ├──
products/ │ ├── inventory/ │ └── sales/ ├── media/ │ └── notas/ ├──
Dockerfile ├── docker-compose.yml ├── requirements.txt └── .env

------------------------------------------------------------------------

## Modelos Sugeridos

### Product

-   codigo (unique)
-   nome
-   preco_custo (DecimalField)
-   preco_venda (DecimalField)
-   quantidade_estoque (IntegerField)

### StockMovement

-   tipo (ENTRADA/SAIDA)
-   produto (FK)
-   quantidade
-   observacao
-   created_at

### Customer

-   nome
-   documento
-   telefone
-   email

### Sale

-   cliente (FK)
-   created_at
-   total
-   status (RASCUNHO, FINALIZADA)
-   nota_txt

### SaleItem

-   venda (FK)
-   produto (FK)
-   quantidade
-   preco_unitario
-   subtotal

------------------------------------------------------------------------

## Geração da Nota TXT

Exemplo de conteúdo gerado:

NOTA DE VENDA #000012 Data: 2026-02-12

Cliente: Nome: João da Silva Documento: 123.456.789-00

Itens: - \[P001\] Produto X x2 R\$ 25,00 - \[P010\] Produto Y x1 R\$
10,00

Total: R\$ 60,00

Arquivo salvo em: media/notas/nota_venda\_`<id>`{=html}.txt

------------------------------------------------------------------------

## Setup com Docker

### 1) Criar arquivo .env

DEBUG=1 SECRET_KEY=django-insecure-troque-isso
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=sales_db DB_USER=postgres DB_PASSWORD=postgres DB_HOST=db
DB_PORT=5432

------------------------------------------------------------------------

### 2) Subir containers

docker compose up --build

------------------------------------------------------------------------

### 3) Rodar migrações

docker compose exec web python manage.py migrate

------------------------------------------------------------------------

### 4) Criar superusuário

docker compose exec web python manage.py createsuperuser

------------------------------------------------------------------------

### 5) Acessar sistema

Admin: http://localhost:8000/admin

------------------------------------------------------------------------

## Regras Importantes

-   Finalizar venda deve rodar dentro de transaction.atomic()
-   Sempre validar estoque antes de debitar
-   Nunca permitir estoque negativo

------------------------------------------------------------------------

## Próximas Evoluções

-   API com Django REST Framework
-   Relatórios de vendas
-   Exportação em PDF
-   Controle de permissões por grupo
-   Dashboard com métricas