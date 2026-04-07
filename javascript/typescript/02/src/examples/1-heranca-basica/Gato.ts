import { Animal } from './Animal';

/**
 * Classe Gato - herda de Animal
 * Demonstra polimorfismo com comportamento diferente do Cachorro
 */
export class Gato extends Animal {
    private cor: string;

    constructor(nome: string, idade: number, cor: string) {
        super(nome, idade); // chama o constructor da classe pai
        this.cor = cor;
    }

    // POLIMORFISMO: sobrescreve o método falar() da classe pai
    // Mesmo método, comportamento diferente!
    public falar(): string {
        return `${this.nome} faz: Miau!`;
    }

    // Método específico da classe Gato
    public dormir(): string {
        return `${this.nome} está dormindo no sol`;
    }

    public getCor(): string {
        return this.cor;
    }
}