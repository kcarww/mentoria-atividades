/**
 * AULA: Herança e Polimorfismo em TypeScript
 * Arquivo principal da aula - executa os exemplos didáticos
 */

console.clear();

// Banner da aula
console.log('┌─'.repeat(40) + '┐');
console.log('│' + ' '.repeat(20) + 'AULA: ORIENTAÇÃO A OBJETOS' + ' '.repeat(20) + '│');
console.log('│' + ' '.repeat(18) + 'Herança e Polimorfismo em TypeScript' + ' '.repeat(18) + '│');
console.log('└─'.repeat(40) + '┘');
console.log();

// Função para pausar entre exemplos
function aguardar(segundos: number = 3): void {
    // Em ambiente real, usaria setTimeout, mas para aula é melhor sequencial
    console.log(`\n⏸️  Aguardando ${segundos} segundos...\n`);
}

// Exemplo 1: Herança básica
async function exemploHeranca(): Promise<void> {
    console.log('📖 EXEMPLO 1: HERANÇA BÁSICA');
    console.log('─'.repeat(50));
    
    try {
        console.log('Importando e executando exemplo de herança...\n');
        await import('./examples/1-heranca-basica/index');
    } catch (error) {
        console.error('❌ Erro no exemplo 1:', error);
    }
}

// Exemplo 2: Polimorfismo
async function exemploPolimorfismo(): Promise<void> {
    console.log('\n📖 EXEMPLO 2: POLIMORFISMO');
    console.log('─'.repeat(50));
    
    try {
        console.log('Importando e executando exemplo de polimorfismo...\n');
        await import('./examples/2-polimorfismo/index');
    } catch (error) {
        console.error('❌ Erro no exemplo 2:', error);
    }
}

// Execução sequencial para aula
async function executarAula(): Promise<void> {
    await exemploHeranca();
    
    aguardar(3);
    
    await exemploPolimorfismo();
    
    // Resumo final
    console.log('\n🎯 RESUMO DA AULA');
    console.log('═'.repeat(50));
    console.log('✅ CONCEITOS APRENDIDOS:');
    console.log('   • Herança com extends');
    console.log('   • Constructor pai com super()');
    console.log('   • Modificadores protected/private');
    console.log('   • Polimorfismo por sobrescrita');
    console.log('   • Classes abstratas');
    console.log('   • Métodos abstratos');
    console.log('   • Arrays polimórficos');
    console.log();
    console.log('🚀 PRÓXIMOS PASSOS:');
    console.log('   • Pratique criando suas próprias hierarquias');
    console.log('   • Experimente com interfaces');
    console.log('   • Explore padrões de design');
    console.log();
    console.log('📚 Obrigado por participar da aula! 👨‍🏫');
}

// Inicia a aula
executarAula().catch(error => {
    console.error('❌ Erro na execução da aula:', error);
});