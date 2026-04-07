import { Veiculo } from './Veiculo';

/**
 * Classe Carro - implementa os métodos abstratos
 */
export class Carro extends Veiculo {
    private portas: number;

    constructor(marca: string, modelo: string, portas: number) {
        super(marca, modelo);
        this.portas = portas;
    }

    // IMPLEMENTAÇÃO OBRIGATÓRIA dos métodos abstratos
    public acelerar(): string {
        return `${this.getInfo()} acelera suavemente`;
    }

    public frear(): string {
        return `${this.getInfo()} freia gradualmente`;
    }

    public getPortas(): number {
        return this.portas;
    }
}