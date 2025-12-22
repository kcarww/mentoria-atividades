# 🎥 API Simples de Upload/Cadastro de Vídeos

API REST simples para cadastro de vídeos, desenvolvida com **Django** e **Django REST Framework**.

Cada vídeo possui apenas:
- `id`
- `titulo`
- `descricao`
- `link`

---

## 📌 Visão Geral

Esta API permite:

- Cadastrar vídeos
- Listar todos os vídeos
- Buscar um vídeo pelo `id`
- Atualizar um vídeo
- Excluir um vídeo

Sem autenticação, sem upload de arquivo binário — apenas **metadados + link do vídeo** (por exemplo, URL do YouTube, Vimeo ou arquivo hospedado em outro lugar).

---

## 🛠 Tecnologias

- **Python 3.10+**
- **Django 4+**
- **Django REST Framework 3+**
- **SQLite** 

---

## 📁 Modelo de Dados

Modelo `Video`:

```python
id:        inteiro (gerado automaticamente pelo Django)
titulo:    string (máx. 255 caracteres)
descricao: texto
link:      string (URL ou caminho do vídeo)
```

---



## 🌐 Endpoints

Assumindo que as URLs foram configuradas em `/api/videos/`:

### 1. Listar vídeos

**GET** `/api/videos/`

**Resposta 200 (exemplo):**

```json
[
  {
    "id": 1,
    "titulo": "Introdução ao Django",
    "descricao": "Vídeo básico explicando os conceitos iniciais do Django.",
    "link": "https://www.youtube.com/watch?v=XXXXXXX"
  },
  {
    "id": 2,
    "titulo": "API com Django REST",
    "descricao": "Criando uma API simples com DRF.",
    "link": "https://www.youtube.com/watch?v=YYYYYYY"
  }
]
```

---

### 2. Criar vídeo

**POST** `/api/videos/`  
**Content-Type:** `application/json`

**Body (exemplo):**

```json
{
  "titulo": "Meu primeiro vídeo",
  "descricao": "Um vídeo qualquer para teste.",
  "link": "https://meu-servidor.com/videos/video1.mp4"
}
```

**Resposta 201 (exemplo):**

```json
{
  "id": 3,
  "titulo": "Meu primeiro vídeo",
  "descricao": "Um vídeo qualquer para teste.",
  "link": "https://meu-servidor.com/videos/video1.mp4"
}
```

---

### 3. Buscar vídeo por ID

**GET** `/api/videos/{id}/`

Exemplo:

`GET /api/videos/3/`

**Resposta 200 (exemplo):**

```json
{
  "id": 3,
  "titulo": "Meu primeiro vídeo",
  "descricao": "Um vídeo qualquer para teste.",
  "link": "https://meu-servidor.com/videos/video1.mp4"
}
```

**Resposta 404 (caso não exista):**

```json
{
  "detail": "Not found."
}
```

---

### 4. Atualizar vídeo

**PUT** `/api/videos/{id}/`  
ou  
**PATCH** `/api/videos/{id}/`

**Body (PUT – exemplo):**

```json
{
  "titulo": "Meu primeiro vídeo (atualizado)",
  "descricao": "Descrição atualizada.",
  "link": "https://meu-servidor.com/videos/video1.mp4"
}
```

**Resposta 200 (exemplo):**

```json
{
  "id": 3,
  "titulo": "Meu primeiro vídeo (atualizado)",
  "descricao": "Descrição atualizada.",
  "link": "https://meu-servidor.com/videos/video1.mp4"
}
```

---

### 5. Excluir vídeo

**DELETE** `/api/videos/{id}/`

**Resposta 204 (sem corpo):**

```text
(no content)
```
