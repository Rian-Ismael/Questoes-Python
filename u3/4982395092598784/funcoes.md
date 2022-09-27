1. O que é uma função?
Função é um 'pacote de código', com nome próprio, com uma função - funcionalidade - específica, executada quando é invocada.

2. O que é uma função pura?
É dita pura se a função produzir a mesma saída, sem que haja algo 'fora' que a altere/modifique - não haja efeito colateral -. Ela produz a mesma saída sempre que processa a mesma entrada.

3. O que são efeitos colaterais?
Quando uma função ler dados de entrada, escreva dados na saída ou altere dados da memoria é dita como colateral, há um efeito colateral.

4. O que é uma expressão de invocação de funções em Python?
Invocação de uma função é a execução dela, ela é feita através de expressões de invocação: um nome seguido de um par de parênteses contendo uma sequência de argumentos - os parênteses são chamados de operador de invocação -.

5. Explique o que é transparência referencial?
É uma expressão que se puder ser substituída por seu valor sem alteraro comportamento do programa - programa tem os mesmos efeitos e saídas para as mesmas entradas-. Um trecho de código de um programa é referencialmente transparente se ele tem valor associado e se esse trecho de código pode ser substituído pelo respectivo valor associado, sem que isso afete o efeito observável.

6. Dê a sintaxe de definição de funções de Python.
def nome_função(parâmentro/s):
    indentação

7. O que são parâmetros formais?
parâmetros formais são os parâmetros dado a função em sua criação:

def exemplo(parâmetros_formais):

por outro lado, se invocamos a função tal nome passa a ser 'chamada' de argumento, exemplo:

add = exemplo(argumento)

8. Como se usa e para quê serve o comando `return`?
ele retorna um determinado valor que deve ser retornado pela função; afunção é encerrada após ser executada pelo interpretador.
