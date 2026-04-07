/**
 * Classe Animal - Exemplo básico de herança em TypeScript
 * Esta é a classe "pai" ou "base"
 */
export class Animal {
    // protected = pode ser acessado pelas classes filhas
    protected nome: string;
    protected idade: number;

    constructor(nome: string, idade: number) {
        this.nome = nome;
        this.idade = idade;
    }

    // Método que pode ser sobrescrito pelas classes filhas
    public falar(): string {
        return `${this.nome} faz algum som`;
    }

    public getInfo(): string {
        return `${this.nome}, ${this.idade} anos`;
    }
}