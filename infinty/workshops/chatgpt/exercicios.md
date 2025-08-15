# 1. Processamento de listas
### Objetivo: praticar loops, list comprehensions e sets.
*Tarefa: implemente encontrar_duplicados(nums: list[int]) → list[int], retornando valores duplicados sem repetir e ordenados.*
*Critérios de aceitação: [1,2,2,3,3,3] → [2,3]; [] → []; [5] → []; mantém apenas ints.*

# 2. Strings e limpeza de dados
### Objetivo: normalizar entrada e validar formato simples.
*Tarefa: escreva normalizar_email(email: str) que: remove espaços, baixa para minúsculas, valida que contém “@” e domínio com “.”; retorna o email normalizado.
Critérios de aceitação: “ JoAo@Exemplo.COM ” → “joao@exemplo.com”; “joao@exemplo” → erro; “@dominio.com” → erro.
Dica: strip, lower e validações com condições simples (sem regex obrigatória).*

# 3. Validação de entrada e tratamento de erros
### Objetivo: reforçar try/except e mensagens claras.
*Tarefa: crie a função to_int(valor: str) que converte string para int; em caso de erro, levanta ValueError com mensagem “valor inválido: ...”.
Critérios de aceitação: aceita “42” e “ 7 ”; falha com “4.2”, “abc” e vazios; testes rápidos no bloco main demonstrando casos.
Dica: usar str.strip e int() com try/except.*

# 4. Docstring, type hints e testes básicos
### Objetivo: padronizar código com documentação e testes.
*Tarefa: para a função media(nums: list[float]) → float, adicionar docstring no padrão Google ou NumPy, type hints e escrever 4 testes com assert no bloco main.
Critérios de aceitação: lida com lista não vazia; lista vazia levanta ValueError; docstring explica parâmetros, retorno e erros.
Dica: definir critérios de aceitação no prompt para o ChatGPT e pedir exemplos.*

# 5. Refatoração leve
### Objetivo: melhorar legibilidade sem mudar comportamento.
*Tarefa: dado o código abaixo, refatore para reduzir complexidade, extrair funções auxiliares e adicionar type hints:*
```
def resumo(notas):
s = 0
m = 0
for n in notas:
s += n
if len(notas) > 0:
m = s/len(notas)
return {'soma': s, 'media': m}
```
*Critérios de aceitação: mantém chaves do dict; lista vazia levanta ValueError; type hints e docstring incluídos; cobertura de 2-3 testes no main.
Dica: validar entrada antes de calcular; extrair calcular_media(nums).*


# 6. Pequeno CLI interativo
### Objetivo: juntar validação, loop e funções.
*Tarefa: construa um mini app de lista de tarefas em memória com opções: adicionar, listar, remover por índice e sair.
Critérios de aceitação: menu em loop; valida entradas (índice válido); funções separadas para cada ação; não usar libs externas.*

# 7. Entrada/saída simples de arquivo
### Objetivo: praticar leitura e escrita de arquivos com segurança.
*Tarefa: implemente salvar_lista(caminho: str, itens: list[str]) que grava um item por linha; e carregar_lista(caminho: str) que retorna a lista sem quebras de linha, ignorando linhas vazias.
Critérios de aceitação: usa with open(..., encoding='utf-8'); trata FileNotFoundError em carregar_lista com mensagem clara; testes no main criam um arquivo temporário, salvam e recarregam.
Dica: no prompt, peça exemplos de uso e limpeza (os.remove) ao final.*


# Projeto final - Controle de Gastos Pessoais em CLI
## Objetivo: em duplas ou trios, criar um aplicativo de linha de comando para registrar despesas e gerar um resumo simples. Sem bibliotecas externas, sem POO. Use apenas funções, listas, dicionários, condicionais e laços, com persistência em arquivo texto.
* Escopo mínimo obrigatório*
* Menu em loop com opções: adicionar despesa, listar despesas, filtrar por categoria, total por categoria, total geral, salvar em arquivo, carregar do arquivo e sair.
* Estrutura de despesa: título (str), valor (float > 0), categoria (str), data opcional (str no formato AAAA-MM-DD; validar formato simples).
* Validação de entrada: campos obrigatórios, valores numéricos, categorias não vazias, formato de data simples.
* Persistência em arquivo .csv simples (uma despesa por linha no formato título;valor;categoria;data).
* Mensagens claras de erro e sucesso; o programa não deve encerrar ao encontrar uma entrada inválida.

## Critérios de aceitação
* O programa inicia sem arquivo prévio e permite adicionar e listar despesas.
* Listagem mostra índice, título, valor com duas casas, categoria e data (se houver).
* Filtros por categoria funcionam mesmo com categorias inexistentes (retornam lista vazia, sem erro).
* Totais por categoria e total geral corretos, com arredondamento a 2 casas.
* Salvar e carregar preservam todos os campos e ignoram linhas malformadas com aviso.
* Código organizado em funções puras (ex.: adicionar_despesa, listar_despesas, filtrar_por_categoria, total_por_categoria, total_geral, salvar_arquivo, carregar_arquivo) e bloco main com o loop do menu.

## Organização da dupla/trio
* Líder de Prompt: escreve e itera os prompts para gerar/ajustar funções; registra os melhores prompts e decisões.
* Programador(a): integra o código, organiza o menu e validações, garante consistência de nomes e fluxo.
* Testador(a)/Escriba (em trios; em duplas alternem): cria casos de teste manuais (valores inválidos, categorias diferentes, arquivo inexistente), roda o app e anota bugs/ajustes.
* Rotação a cada sprint de 10 minutos para que todos experimentem os papéis.

## Plano de execução (40 minutos)
* Sprint 1 (10 min): Esqueleto do menu e tipos de dados. Saída: loop do menu com opções e lista em memória.
* Sprint 2 (10 min): Implementar adicionar_despesa (com validação), listar_despesas e filtrar_por_categoria.
* Sprint 3 (10 min): Implementar total_por_categoria e total_geral; formatar valores monetários.
* Sprint 4 (10 min): Implementar salvar_arquivo/carregar_arquivo, tratar erros (FileNotFoundError, linhas malformadas), polir mensagens e revisar docstrings.

### Checklist mínimo de qualidade
*O programa não quebra com entradas inválidas; totais e filtros corretos; arquivo gerado é legível; funções pequenas e nomeadas claramente; existe um caminho feliz completo (adicionar → listar → filtrar → totalizar → salvar → carregar → listar).*

### Entregáveis
*Um único arquivo .py executável, um arquivo de exemplo gerado pelo app (despesas.csv) e um README curto (.txt) com instruções de execução, funcionalidades, exemplos de uso e principais prompts utilizados.*
