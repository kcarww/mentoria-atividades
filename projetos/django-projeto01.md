# 📄 Requisitos para Criação de um E-commerce (Django)

## 📌 Objetivo
Desenvolver um sistema de **e-commerce** utilizando **Python + Django**, com funcionalidades de gerenciamento de produtos, clientes e pedidos, além de integração com sistemas de pagamento.

---

## 🗄️ Entidades Principais

### 🔑 Admin
- Responsável por gerenciar toda a operação.
- Acesso ao painel administrativo (Django Admin).
- Permissões: cadastrar/editar/deletar produtos, gerenciar clientes, visualizar pedidos.

### 👤 Cliente
- Campos principais:
  - Nome
  - E-mail
  - CPF/CNPJ
  - Senha (autenticação com Django Auth)
  - Telefone
- Relações:
  - Pode ter vários **endereços de entrega**.
  - Pode realizar vários **pedidos**.

### 📦 Produto
- Campos principais:
  - Nome
  - Descrição
  - Preço
  - SKU / Código interno
  - Estoque
  - Data de criação / atualização
- Relações:
  - Pertence a uma ou mais **categorias**.
  - Pode ter várias imagens.

### 📑 Pedido
- Campos principais:
  - Cliente (FK → Cliente)
  - Data do pedido
  - Status (Criado, Pago, Enviado, Concluído, Cancelado)
  - Forma de pagamento
  - Valor total
- Relações:
  - Contém vários **itens de pedido**.

### 🧾 Item Pedido
- Campos principais:
  - Pedido (FK → Pedido)
  - Produto (FK → Produto)
  - Quantidade
  - Preço unitário
  - Subtotal

---

## 🔗 Outras Entidades Importantes (Sugestões)

### 📍 Endereço
- Associado ao **Cliente**.
- Campos:
  - Rua, número, complemento
  - Cidade, Estado, CEP, País
- Pode ser marcado como **principal** ou **entrega padrão**.

### 🛒 Carrinho de Compras
- Pode ser armazenado em sessão ou persistido no banco.
- Campos:
  - Cliente (FK, opcional se visitante)
  - Data de criação
- Relação:
  - Vários **itens de carrinho** (produto + quantidade).

### 📂 Categoria de Produto
- Exemplo: Eletrônicos > Celulares.
- Suporte para **hierarquia** (subcategorias).
- Facilita busca e organização.

### 💳 Pagamento
- Armazena dados da transação com o gateway.
- Campos:
  - Pedido (FK → Pedido)
  - Status do pagamento (pendente, aprovado, recusado)
  - Código de transação do gateway (ex: Stripe, PayPal, PagSeguro)
  - Data/hora
- Relação direta com integração externa.

---

## ⚙️ Funcionalidades Essenciais
- **Cadastro e autenticação de clientes**
- **Gerenciamento de produtos e categorias** (CRUD completo)
- **Controle de estoque**
- **Carrinho de Compras**
- **Checkout**
- **Geração de Pedidos**
- **Integração com Gateway de Pagamento**
- **Histórico de pedidos do cliente**
- **Painel administrativo (Django Admin)**
- **Notificação por e-mail** (confirmação de pedido, recuperação de senha, etc.)

---

## 🔌 Integrações de Pagamento (opções)
- **Stripe** (internacional, simples de integrar).
- **PayPal**.
- **Mercado Pago** ou **PagSeguro** (para Brasil).
- **Pix** (usando API de bancos ou intermediadores).

---

## 🛠️ Stack Tecnológica
- **Backend**: Python 3 + Django (com Django Rest Framework para APIs).
- **Banco de Dados**: PostgreSQL ou MySQL.
- **Frontend**: Django Templates ou SPA (React/Vue/Angular) consumindo API.
- **Autenticação**: Django default + JWT (para integração com API).
- **Pagamentos**: Stripe / MercadoPago / PagSeguro.
- **Containerização (opcional)**: Docker.

---

## 📊 Diagrama Simplificado (Entidades)
```
Cliente ----< Pedido ----< ItemPedido >---- Produto >---- Categoria
   |
   +----< Endereço

Carrinho ----< ItemCarrinho >---- Produto
```
