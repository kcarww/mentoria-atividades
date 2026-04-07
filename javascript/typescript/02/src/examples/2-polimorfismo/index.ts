import { Veiculo } from './Veiculo';
import { Carro } from './Carro';
import { Moto } from './Moto';

console.log('=== EXEMPLO 2: POLIMORFISMO COM CLASSES ABSTRATAS ===\n');

// 1. CRIANDO OBJETOS
console.log('1. Criando veículos:');
const civic = new Carro('Honda', 'Civic', 4);
const cb600 = new Moto('Honda', 'CB600', 600);

console.log(`Carro: ${civic.getInfo()}, ${civic.getPortas()} portas`);
console.log(`Moto: ${cb600.getInfo()}, ${cb600.getCilindradas()}cc\n`);

// 2. POLIMORFISMO - MESMOS MÉTODOS, COMPORTAMENTOS DIFERENTES
console.log('2. Polimorfismo - acelerar:');
console.log(civic.acelerar());  // "acelera suavemente"
console.log(cb600.acelerar());  // "acelera rapidamente"
console.log();

console.log('3. Polimorfismo - frear:');
console.log(civic.frear());     // "freia gradualmente"  
console.log(cb600.frear());     // "freia bruscamente"
console.log();

// 4. ARRAY POLIMÓRFICO
console.log('4. Array polimórfico:');
const veiculos: Veiculo[] = [civic, cb600];

console.log('Testando aceleração de todos os veículos:');
veiculos.forEach((veiculo, index) => {
    console.log(`${index + 1}. ${veiculo.acelerar()}`);
});

console.log('\n✅ Conceitos demonstrados:');
console.log('- Classe abstrata (abstract class)');
console.log('- Método abstrato (abstract method)');
console.log('- Implementação obrigatória');
console.log('- Polimorfismo puro');
console.log('- Array polimórfico');

// 5. TENTATIVA DE INSTANCIAR CLASSE ABSTRATA (erro!)
console.log('\n❌ Não é possível fazer: new Veiculo()');
console.log('✅ Apenas: new Carro() ou new Moto()');