
# 🧩 Projeto: Sistema de Cadastro com Menu (JavaScript)

## 📘 Descrição
Crie um programa em JavaScript que simule um **sistema de cadastro** usando um **menu interativo**. O usuário irá interagir pelo `prompt()` e os dados serão guardados em um **array de objetos**. O menu deve permitir **cadastrar**, **listar**, **buscar**, **remover** itens e **sair**.


---

## 🎯 Objetivos de Aprendizagem
- Praticar a coleta de dados com `prompt()`
- Organizar código em **funções**
- Armazenar dados em **arrays de objetos**
- Percorrer e manipular coleções (listar, buscar, remover)

---

## 🧱 Requisitos Técnicos
- Entrada: `prompt()`
- Organização: funções
- Estrutura de dados: array e objetos
- Saída: `console.log()`
- Encerramento: opção de sair do menu

---

## 📋 Funcionalidades Obrigatórias
1. Menu principal com as opções:
   ```
   1 - Cadastrar item
   2 - Listar todos os itens
   3 - Buscar item por nome
   4 - Remover item
   5 - Sair
   ```
2. Cadastrar item
   - Pedir: `nome`, `categoria`, `preco`
   - Criar um objeto com esses campos
   - Inserir no array principal
3. Listar itens
   - Exibir todos os objetos cadastrados
4. Buscar por nome
   - Pedir o nome
   - Exibir o item encontrado (ou dizer que não existe)
5. Remover item
   - Pedir o nome
   - Remover o objeto correspondente, se existir
6. Sair
   - Encerra o programa

---

## ✅ Regras de Validação (mínimo recomendado)
- Não cadastrar itens com `nome` vazio
- Exibir mensagens claras para ações realizadas ou erros

---

## 💡 Desafios (opcional)
- Impedir nomes duplicados
- Mostrar quantidade total de itens cadastrados
- Editar um item existente
- Ordenar listagem por nome ou preço

---

## 🗂️ Estrutura Sugerida do Código
```javascript
let itens = [];

function menu() {
  // loop exibindo opções e chamando funções conforme a escolha
}

function cadastrarItem() {
  // cria objeto { nome, categoria, preco } e adiciona ao array
}

function listarItens() {
  // percorre e exibe itens
}

function buscarItem() {
  // busca por nome e mostra resultado
}

function removerItem() {
  // remove pelo nome
}

// ponto de entrada
menu();
```

---

## ▶️ Como Executar
Você pode executar o programa de duas formas simples:

1) No navegador (recomendado para iniciantes)
- Abra o navegador (Chrome/Firefox)
- Pressione F12 e vá até a aba "Console"
- Cole o seu código completo e pressione Enter
- Interaja com os `prompt()` que aparecerem

2) Em um arquivo .js aberto no navegador
- Crie um arquivo `index.html` simples contendo apenas a tag `<script>` com o seu código JavaScript dentro
- Abra o `index.html` no navegador e o programa iniciará

---
- Você pode adaptar os campos do item conforme o tema escolhido (ex.: produtos, alunos, livros, tarefas)
- Mantenha o código simples e comentado, priorizando legibilidade

