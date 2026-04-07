import { Veiculo } from './Veiculo';

/**
 * Classe Moto - implementa os métodos abstratos
 */
export class Moto extends Veiculo {
    private cilindradas: number;

    constructor(marca: string, modelo: string, cilindradas: number) {
        super(marca, modelo);
        this.cilindradas = cilindradas;
    }

    // IMPLEMENTAÇÃO OBRIGATÓRIA dos métodos abstratos
    // Comportamento diferente do carro!
    public acelerar(): string {
        return `${this.getInfo()} acelera rapidamente`;
    }

    public frear(): string {
        return `${this.getInfo()} freia bruscamente`;
    }

    public getCilindradas(): number {
        return this.cilindradas;
    }
}