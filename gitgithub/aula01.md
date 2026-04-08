# 🚀 Aula: Primeiros Passos com GitHub + Como Deixar seu Perfil Atraente

## 🎯 Objetivo da Aula
Ao final dessa aula você será capaz de:
- Entender o que é Git e GitHub
- Usar os principais comandos do Git
- Subir seu primeiro projeto
- Organizar um perfil atrativo para recrutadores

---

## 📌 1. O que é Git e GitHub?

### 🔹 Git
Sistema de controle de versão (versionamento de código)

👉 Permite:
- Salvar histórico do código
- Voltar versões
- Trabalhar em equipe

### 🔹 GitHub
Plataforma online para hospedar repositórios Git

👉 Funciona como:
- Portfólio de desenvolvedor
- Rede social de código

---

## ⚙️ 2. Instalação do Git

👉 Baixar:
https://git-scm.com

---

## 🔧 3. Configuração Inicial

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@email.com"
```

Verificar:

```bash
git config --list
```

---

## 📁 4. Criando seu primeiro repositório

```bash
mkdir meu-projeto
cd meu-projeto
git init
```

---

## 📄 5. Primeiro arquivo

```bash
touch README.md
```

---

## 💾 6. Primeiros comandos Git

```bash
git status
git add .
git commit -m "primeiro commit"
```

---

## 🔗 7. Conectando com GitHub

```bash
git remote add origin https://github.com/seu-usuario/meu-projeto.git
```

---

## 🚀 8. Enviando código para o GitHub

```bash
git branch -M main
git push -u origin main
```

---

## 🔄 9. Fluxo do dia a dia

```bash
git add .
git commit -m "descrição do que foi feito"
git push
```

---

## 🌱 10. Trabalhando com branches

```bash
git checkout -b nova-feature
git checkout main
```

---

## 🔀 11. Atualizar código do repositório

```bash
git pull
```

---

## 📚 12. Estrutura de um bom projeto

```
meu-projeto/
├── README.md
├── src/
├── tests/
├── .gitignore
└── requirements.txt / package.json
```

---

## ✨ 13. Como deixar seu perfil do GitHub atraente

### 🧠 Foto e nome profissional
- Foto clara
- Nome real

### 📝 Bio estratégica
Backend Developer | Python | FastAPI | Django

### 📌 Repositórios organizados
- 1 API
- 1 projeto com banco
- 1 CRUD completo

### ⭐ README bem feito
Inclua:
- Descrição
- Tecnologias
- Como rodar

---

## 🧪 14. Desafio

Criar:
- Repositório: api-alunos
- CRUD
- README completo
- Subir no GitHub

---

## 🏁 Conclusão

✔ Git básico  
✔ GitHub organizado  
✔ Projetos publicados  
✔ README profissional  
