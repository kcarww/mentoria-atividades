# README — E-commerce em Java

## Visão geral
Backend de e-commerce em Java com rotas para:
- Usuários
- Produtos
- Pedidos

Inclui requisitos funcionais e não funcionais, modelo de dados (tabelas e colunas) e rotas REST sugeridas.

## Stack sugerida
- Java 17+
- Spring Boot 3.x (Web, Validation, Data JPA, Security opcional)
- Banco: MySQL, PostgreSQL (Qualquer outro que tu achar melhor tbm)
- Migrações: Flyway ou Liquibase (Veremos em breve)
- Build: Gradle ou Maven
- Testes: JUnit 5, Mockito (Veremos em breve)
- Documentação: OpenAPI/Swagger (Veremos em breve)

## Requisitos funcionais
### Usuários
- Criar usuário (e-mail único)
- Editar dados do usuário
- Excluir (soft delete recomendado)
- Listar/buscar com paginação
- Login/autenticação (opcional)

### Produtos
- Criar produto (SKU único)
- Editar produto
- Excluir (soft delete recomendado)
- Listar/buscar com filtros
- Atualização de estoque em operações de pedido

### Pedidos
- Criar pedido para um usuário
- Adicionar itens (quantidade, preço capturado no momento)
- Atualizar status: CREATED, PAID, SHIPPED, DELIVERED, CANCELED
- Calcular total
- Listar por usuário e status

### Extras opcionais
- Pagamentos
- Endereços de usuário
- Categorias e relacionamento produto-categoria
- Movimentação de estoque (auditoria)
- Audit log

## Requisitos não funcionais
- API RESTful JSON
- Validação (Bean Validation)
- Desafio: Paginação (page, size, sort)
- Tratamento de erros padrão (Problem Details opcional)
- Logs estruturados (Opcional)
- Testes unitários e de integração (Opcional)
- Migrações do banco versionadas (Opcional)
- Segurança com JWT e papéis (ROLE_USER, ROLE_ADMIN) (Opcional) 

## Modelo de dados 

### users
- id: UUID PK
- name: varchar(120) not null
- email: varchar(255) not null unique
- password_hash: varchar(255) not null
- phone: varchar(30) null
- role: varchar(30) not null default 'ROLE_USER' 
- is_active: boolean not null default true
- created_at: timestamp not null default now()
- updated_at: timestamp not null default now()
- deleted_at: timestamp null

### user_addresses (opcional)
- id: UUID PK
- user_id: UUID FK -> users(id) not null
- address: varchar(160) not null
- district: varchar(100) null
- city: varchar(100) not null
- state: varchar(100) not null
- country: char(2) not null (ISO-3166)
- postal_code: varchar(20) not null
- is_default: boolean not null default false
- created_at, updated_at

### categories (opcional)
- id: UUID PK
- name: varchar(120) not null unique
- description: text null
- is_active: boolean not null default true
- created_at, updated_at, deleted_at

### products
- id: UUID PK
- name: varchar(160) not null
- description: text null
- sku: varchar(64) not null unique
- price: numeric(12,2) not null
- currency: char(3) not null default 'BRL'
- stock_quantity: integer not null default 0
- weight_grams: integer null
- width_cm: numeric(8,2) null
- height_cm: numeric(8,2) null
- length_cm: numeric(8,2) null
- is_active: boolean not null default true
- created_at, updated_at, deleted_at

### product_categories (opcional, N:N)
- product_id: UUID FK -> products(id)
- category_id: UUID FK -> categories(id)
- PK composta (product_id, category_id)

### orders
- id: UUID PK
- user_id: UUID FK -> users(id) not null
- status: varchar(20) not null (CREATED, PAID, SHIPPED, DELIVERED, CANCELED)
- total_amount: numeric(12,2) not null
- currency: char(3) not null default 'BRL'
- shipping_address_id: UUID FK -> user_addresses(id) null
- notes: text null
- created_at, updated_at

### order_items
- id: UUID PK
- order_id: UUID FK -> orders(id) not null
- product_id: UUID FK -> products(id) not null
- product_name: varchar(160) not null
- product_sku: varchar(64) not null
- unit_price: numeric(12,2) not null
- quantity: integer not null
- total_price: numeric(12,2) not null (unit_price * quantity)
- created_at

### payments (opcional)
- id: UUID PK
- order_id: UUID FK -> orders(id) unique not null
- provider: varchar(60) not null
- external_reference: varchar(120) null
- status: varchar(30) not null (PENDING, AUTHORIZED, PAID, FAILED, CANCELED)
- amount: numeric(12,2) not null
- currency: char(3) not null default 'BRL'
- payload: jsonb null
- created_at, updated_at

### inventory_movements (opcional)
- id: UUID PK
- product_id: UUID FK -> products(id) not null
- type: varchar(20) not null (IN, OUT, ADJUST)
- quantity: integer not null
- reason: varchar(80) null (ex: ORDER_CREATED, ORDER_CANCELED)
- reference_id: UUID null (ex: order_id)
- created_at

### audit_log (opcional)
- id: UUID PK
- entity: varchar(60) not null
- entity_id: UUID not null
- action: varchar(30) not null (CREATE, UPDATE, DELETE)
- actor_id: UUID null
- data_before: jsonb null
- data_after: jsonb null
- created_at

### Índices/constraints
- users(email) unique
- products(sku) unique
- products(name) index
- orders(user_id), orders(status) index
- order_items(order_id) index
- inventory_movements(product_id) index

## Rotas REST

### Usuários (/api/v1/users)
- POST /users — cria usuário
- GET /users — lista com paginação e filtro
- GET /users/{id}
- PUT /users/{id}
- DELETE /users/{id} — soft delete
- POST /auth/login — autenticação JWT

Payloads básicos:
- POST /users
```
{
  "name": "Maria Silva",
  "email": "maria@exemplo.com",
  "password": "senhaSegura123",
  "phone": "+55 11 99999-9999"
}
```

### Produtos (/api/v1/products)
- POST /products
- GET /products
- GET /products/{id}
- PUT /products/{id}
- DELETE /products/{id}
- POST /products/{id}/stock — movimenta estoque (IN|OUT|ADJUST) (Opcional)

### Categorias (/api/v1/categories) — opcional
- POST /categories
- GET /categories
- GET /categories/{id}
- PUT /categories/{id}
- DELETE /categories/{id}
- POST /products/{productId}/categories/{categoryId}
- DELETE /products/{productId}/categories/{categoryId}

### Pedidos (/api/v1/orders)
- POST /orders — cria pedido
- GET /orders — lista pedidos (page, size, userId, status)
- GET /orders/{id}
- PATCH /orders/{id}/status — altera status
- GET /users/{userId}/orders — atalho

Exemplo POST /orders
```
{
  "userId": "<uuid>",
  "shippingAddressId": "<uuid>",
  "items": [
    { "productId": "<uuid>", "quantity": 2 },
    { "productId": "<uuid>", "quantity": 1 }
  ]
}
```

## Políticas/negócio
- E-mail e SKU únicos
- Preço e estoque não negativos
- Nos itens de pedido, capturar snapshot de name, sku e unit_price
- Estoque (duas opções):
  - A) Deduzir no CREATED e devolver no CANCELED
  - B) Reservar no CREATED, deduzir no PAID, devolver se CANCELED antes do pagamento

## Validações (sugestões)
- name: @NotBlank, tamanho máximo
- email: @Email, @NotBlank
- password: mínimo 8 caracteres
- price: @PositiveOrZero
- stockQuantity: @PositiveOrZero
- quantity (order item): @Positive

## DDL SQL (PostgreSQL) — exemplo simplificado

```sql
create extension if not exists "uuid-ossp";

create table users (
  id uuid primary key default uuid_generate_v4(),
  name varchar(120) not null,
  email varchar(255) not null unique,
  password_hash varchar(255) not null,
  phone varchar(30),
  role varchar(30) not null default 'ROLE_USER',
  is_active boolean not null default true,
  created_at timestamp not null default now(),
  updated_at timestamp not null default now(),
  deleted_at timestamp
);

create table products (
  id uuid primary key default uuid_generate_v4(),
  name varchar(160) not null,
  description text,
  sku varchar(64) not null unique,
  price numeric(12,2) not null,
  currency char(3) not null default 'BRL',
  stock_quantity integer not null default 0,
  weight_grams integer,
  width_cm numeric(8,2),
  height_cm numeric(8,2),
  length_cm numeric(8,2),
  is_active boolean not null default true,
  created_at timestamp not null default now(),
  updated_at timestamp not null default now(),
  deleted_at timestamp
);

create table orders (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid not null references users(id),
  status varchar(20) not null,
  total_amount numeric(12,2) not null,
  currency char(3) not null default 'BRL',
  shipping_address_id uuid,
  notes text,
  created_at timestamp not null default now(),
  updated_at timestamp not null default now()
);

create table order_items (
  id uuid primary key default uuid_generate_v4(),
  order_id uuid not null references orders(id),
  product_id uuid not null references products(id),
  product_name varchar(160) not null,
  product_sku varchar(64) not null,
  unit_price numeric(12,2) not null,
  quantity integer not null,
  total_price numeric(12,2) not null,
  created_at timestamp not null default now()
);
```
