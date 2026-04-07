/**
 * Classe abstrata Veiculo - demonstra polimorfismo
 * Classes abstratas não podem ser instanciadas diretamente
 */
export abstract class Veiculo {
    protected marca: string;
    protected modelo: string;

    constructor(marca: string, modelo: string) {
        this.marca = marca;
        this.modelo = modelo;
    }

    // Método concreto - todos os veículos têm
    public getInfo(): string {
        return `${this.marca} ${this.modelo}`;
    }

    // Método abstrato - DEVE ser implementado pelas classes filhas
    public abstract acelerar(): string;
    public abstract frear(): string;
}