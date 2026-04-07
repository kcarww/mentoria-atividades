# Aula: Herança e Polimorfismo em TypeScript

## 📚 Objetivos da Aula
Ao final desta aula, você será capaz de:
- Entender o conceito de **herança** em TypeScript
- Aplicar **polimorfismo** através de sobrescrita de métodos
- Criar hierarquias de classes simples e efetivas

---

## 🚀 Passo a Passo

### **Passo 1: Configuração Inicial**

1. **Instale o TypeScript globalmente (se ainda não tiver):**
```bash
npm install -g typescript ts-node
```

2. **Instale as dependências do projeto:**
```bash
npm install
```

3. **Execute o projeto:**
```bash
npm run dev
```

---

### **Passo 2: Entendendo Herança** 

#### O que é Herança?
Herança permite que uma classe **filha** receba características de uma classe **pai**.

#### Exemplo Prático: Animais

Vamos ver o arquivo `src/examples/1-heranca-basica/Animal.ts`:

**Classe Pai (Animal):**
```typescript
export class Animal {
    protected nome: string;
    protected idade: number;

    constructor(nome: string, idade: number) {
        this.nome = nome;
        this.idade = idade;
    }

    public falar(): string {
        return `${this.nome} faz algum som`;
    }
}
```

**Classes Filhas:**
```typescript
export class Cachorro extends Animal {
    public falar(): string {
        return `${this.nome} faz: Au au!`;
    }
}

export class Gato extends Animal {
    public falar(): string {
        return `${this.nome} faz: Miau!`;
    }
}
```

#### **Execute o Exemplo 1:**
```bash
npx ts-node src/examples/1-heranca-basica/index.ts
```

---

### **Passo 3: Entendendo Polimorfismo**

#### O que é Polimorfismo?
Polimorfismo permite que o **mesmo método** tenha **comportamentos diferentes** em classes diferentes.

#### Exemplo Prático: Veículos

Examine o arquivo `src/examples/2-polimorfismo/Veiculo.ts`:

**Classe Abstrata:**
```typescript
export abstract class Veiculo {
    protected marca: string;

    // Método que DEVE ser implementado pelas classes filhas
    public abstract acelerar(): string;
}
```

**Implementações Específicas:**
```typescript
export class Carro extends Veiculo {
    public acelerar(): string {
        return "Carro acelerando suavemente";
    }
}

export class Moto extends Veiculo {
    public acelerar(): string {
        return "Moto acelerando rapidamente";
    }
}
```

#### **Execute o Exemplo 2:**
```bash
npx ts-node src/examples/2-polimorfismo/index.ts
```

---

### **Passo 4: Testando na Prática**

1. **Execute os exemplos em sequência:**
   - Exemplo 1: Herança básica
   - Exemplo 2: Polimorfismo

2. **Observe os conceitos:**
   - **Herança**: `extends`, `super()`, `protected`
   - **Polimorfismo**: Mesmos métodos, comportamentos diferentes

---

## 🎯 Exercícios Práticos

### **Exercício 1: Criar sua própria hierarquia**
Crie classes para:
- `Forma` (classe pai)
- `Retangulo` (classe filha)
- `Circulo` (classe filha)

Cada forma deve calcular sua área de forma diferente.

### **Exercício 2: Polimorfismo**
Crie um array de formas e calcule a área total usando polimorfismo.

---

## ✅ Conceitos Aprendidos

- **Herança com `extends`**
- **Constructor da classe pai com `super()`**
- **Modificadores `protected` e `private`**
- **Polimorfismo por sobrescrita**
- **Classes abstratas**

---

## 🔧 Comandos Principais

```bash
# Executar projeto
npm run dev

# Executar exemplo específico
npx ts-node src/examples/1-heranca-basica/index.ts
npx ts-node src/examples/2-polimorfismo/index.ts

# Compilar TypeScript
npm run build
```