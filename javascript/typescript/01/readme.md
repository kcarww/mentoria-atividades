# 📘 README — Do Zero até POO com TypeScript

## 🚀 Objetivo

Este guia ensina TypeScript desde o básico até Programação Orientada a Objetos (POO), de forma prática e progressiva.

---

## 📦 Pré-requisitos

- Node.js instalado
- npm ou yarn
- VS Code (recomendado)

### Verificar instalação:

```bash
node -v
npm -v
```

---

## ⚙️ 1. Criando o Projeto

```bash
mkdir projeto-ts
cd projeto-ts

npm init -y
npm install typescript --save-dev
npx tsc --init
```

---

## 📁 Estrutura do Projeto

```bash
projeto-ts/
│
├── src/
│   ├── index.ts
│   ├── fundamentos/
│   └── poo/
│
├── package.json
└── tsconfig.json
```

---

# 🧠 2. Fundamentos do TypeScript

---

## 🔹 Tipos Básicos

```ts
let nome: string = "Carlos";
let idade: number = 25;
let ativo: boolean = true;
```

---

## 🔹 Arrays

```ts
let numeros: number[] = [1, 2, 3];
let nomes: Array<string> = ["Ana", "João"];
```

---

## 🔹 Tuplas

```ts
let pessoa: [string, number] = ["Carlos", 25];
```

---

## 🔹 Enum

```ts
enum Status {
  Ativo,
  Inativo
}

let userStatus: Status = Status.Ativo;
```

---

## 🔹 Funções

```ts
function soma(a: number, b: number): number {
  return a + b;
}
```

---

## 🔹 Interfaces

```ts
interface Pessoa {
  nome: string;
  idade: number;
}

const pessoa: Pessoa = {
  nome: "Carlos",
  idade: 25
};
```

---

# ⚙️ 3. Classes no TypeScript

---

## 🔹 Criando uma classe

```ts
class Pessoa {
  nome: string;
  idade: number;

  constructor(nome: string, idade: number) {
    this.nome = nome;
    this.idade = idade;
  }

  apresentar(): string {
    return `Meu nome é ${this.nome}`;
  }
}
```

---

# 🔐 4. Encapsulamento

```ts
class Conta {
  private saldo: number;

  constructor(saldo: number) {
    this.saldo = saldo;
  }

  depositar(valor: number): void {
    this.saldo += valor;
  }

  verSaldo(): number {
    return this.saldo;
  }
}
```

---

# 🧬 5. Herança

```ts
class Animal {
  falar(): void {
    console.log("Som do animal");
  }
}

class Cachorro extends Animal {
  falar(): void {
    console.log("Latido");
  }
}
```

---

# 🎭 6. Polimorfismo

```ts
const animais: Animal[] = [new Animal(), new Cachorro()];

animais.forEach(animal => animal.falar());
```

---

# 🧪 7. Exercício Final

Crie uma classe Aluno:

```ts
class Aluno {
  nome: string;
  nota: number;

  constructor(nome: string, nota: number) {
    this.nome = nome;
    this.nota = nota;
  }

  aprovado(): boolean {
    return this.nota >= 7;
  }
}
```

---

# ▶️ Rodando o Projeto

```bash
npx tsc
node dist/index.js
```

---

# 📚 Próximos Passos

- APIs com Node.js (Express / Fastify)
- Banco de dados (Prisma)
- Testes (Jest)
- Clean Architecture

---

# 💡 Dica Final

TypeScript é JavaScript com superpoderes. Pratique criando projetos reais.
