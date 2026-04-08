# 🚀 Plataforma SaaS de Gestão de Serviços

## 📌 Descrição

Este projeto é uma **API backend completa** para uma plataforma de gestão de serviços (modelo SaaS), onde empresas podem gerenciar clientes, pedidos e usuários.

O sistema foi desenvolvido com foco em **boas práticas de mercado**, incluindo arquitetura limpa, autenticação e separação por empresa (multi-tenant).

---

## 🎯 Objetivo

Este projeto tem como objetivo simular um sistema real utilizado por empresas, servindo como **projeto de portfólio profissional**.

---

## 🧠 Funcionalidades

### 👤 Usuários

* Cadastro de usuários
* Login com autenticação
* Controle de permissões (admin / usuário)

---

### 🏢 Empresas (Multi-tenant)

* Cada empresa possui seus próprios dados
* Isolamento de informações entre empresas

---

### 👥 Clientes

* Cadastro de clientes
* Listagem e histórico de pedidos

---

### 📦 Pedidos / Serviços

* Criar pedidos
* Atualizar status:

  * Aberto
  * Em andamento
  * Finalizado

---

### 📊 Relatórios

* Total de pedidos
* Pedidos por status
* Clientes mais ativos

---

## 🛠️ Tecnologias

* Python
* FastAPI
* SQLAlchemy
* MySQL ou PostgreSQL
* Docker
* JWT (ou Keycloak)

---

## 🧱 Arquitetura

O projeto segue princípios de **Clean Architecture + DDD**:

```
src/
├── domain/
├── application/
├── infrastructure/
└── interfaces/
```

---

## 🔐 Autenticação

* Login com JWT
* Proteção de rotas
* Controle de acesso por usuário

---

## 📁 Estrutura do Projeto

```
service-platform/
│
├── src/
├── tests/
├── docker/
├── README.md
├── .env
└── docker-compose.yml
```

---

## 🚀 Como rodar o projeto

### 1. Clonar repositório

```bash
git clone https://github.com/seu-usuario/service-platform.git
cd service-platform
```

---

### 2. Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env`:

```
DATABASE_URL=mysql://user:password@localhost:3306/db
SECRET_KEY=sua_chave_secreta
```

---

### 5. Rodar o projeto

```bash
uvicorn src.main:app --reload
```

---

### 6. Acessar documentação

```
http://localhost:8000/docs
```

---

## 🐳 Rodando com Docker

```bash
docker-compose up --build
```

---

## 🔌 Endpoints principais

### 🔐 Autenticação

```
POST /auth/login
```

### 👤 Usuários

```
POST /users
GET /users
```

### 🏢 Empresas

```
POST /companies
GET /companies
```

### 👥 Clientes

```
POST /clients
GET /clients
```

### 📦 Pedidos

```
POST   /orders
GET    /orders
PATCH  /orders/{id}
```

---

## 🧪 Testes

```bash
pytest
```

---

## 📈 Diferenciais do Projeto

✔ Arquitetura profissional (DDD + Clean Architecture)
✔ Multi-tenant (nível mercado)
✔ Autenticação e autorização
✔ API documentada automaticamente
✔ Estrutura escalável

---

## 💼 Como usar no currículo

> Desenvolvi uma plataforma SaaS para gestão de serviços, com autenticação, arquitetura baseada em Clean Architecture e suporte a múltiplas empresas (multi-tenant), utilizando Python (FastAPI) e banco de dados relacional.

---

## 🔥 Melhorias futuras

* Integração com pagamento (Stripe)
* Notificações (email / WhatsApp)
* Dashboard frontend
* Upload de arquivos
* Logs e monitoramento

---

## 👨‍💻 Autor

Seu Nome

---

## ⭐ Contribuição

Pull requests são bem-vindos!
Para mudanças maiores, abra uma issue primeiro.

---

## 📄 Licença

Este projeto está sob a licença MIT.
