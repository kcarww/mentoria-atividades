import { Animal } from './Animal';

/**
 * Classe Cachorro - herda de Animal
 * Demonstra como uma classe filha sobrescreve métodos da classe pai
 */
export class Cachorro extends Animal {
    private raca: string;

    constructor(nome: string, idade: number, raca: string) {
        super(nome, idade); // chama o constructor da classe pai
        this.raca = raca;
    }

    // POLIMORFISMO: sobrescreve o método falar() da classe pai
    public falar(): string {
        return `${this.nome} faz: Au au!`;
    }

    // Método específico da classe Cachorro
    public brincar(): string {
        return `${this.nome} está brincando!`;
    }

    public getRaca(): string {
        return this.raca;
    }
}