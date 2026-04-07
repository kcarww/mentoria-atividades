import { Animal } from './Animal';
import { Cachorro } from './Cachorro';
import { Gato } from './Gato';

console.log('=== EXEMPLO 1: HERANÇA E POLIMORFISMO ===\n');

// 1. CRIANDO OBJETOS
console.log('1. Criando animais:');
const rex = new Cachorro('Rex', 3, 'Labrador');
const mimi = new Gato('Mimi', 2, 'Branco');

console.log(`Cachorro: ${rex.getInfo()}, raça: ${rex.getRaca()}`);
console.log(`Gato: ${mimi.getInfo()}, cor: ${mimi.getCor()}\n`);

// 2. POLIMORFISMO EM AÇÃO
console.log('2. Polimorfismo - mesmo método, comportamentos diferentes:');
console.log(rex.falar());   // "Rex faz: Au au!"
console.log(mimi.falar());  // "Mimi faz: Miau!"
console.log();

// 3. MÉTODOS ESPECÍFICOS
console.log('3. Métodos específicos de cada classe:');
console.log(rex.brincar());  // método só do cachorro
console.log(mimi.dormir());  // método só do gato
console.log();

// 4. POLIMORFISMO COM ARRAY
console.log('4. Array polimórfico - tratando diferentes animais igual:');
const animais: Animal[] = [rex, mimi];

animais.forEach((animal, index) => {
    console.log(`Animal ${index + 1}: ${animal.falar()}`);
});

console.log('\n✅ Conceitos demonstrados:');
console.log('- Herança (extends)');
console.log('- Super constructor (super)');  
console.log('- Polimorfismo (override)');
console.log('- Modificador protected');