# Least Recently Used (LRU)

Least Recently Used (LRU) é um algoritmo de substituição de página usado em sistemas operacionais e bancos de dados para gerenciar a memória cache. O objetivo é remover a página que foi menos utilizada recentemente para liberar espaço para novas páginas.

O algoritmo funciona mantendo uma lista de páginas na ordem em que elas foram usadas. Quando a memória cache atinge sua capacidade máxima e é necessário inserir uma nova página, a página na posição mais antiga da lista é removida. Desta forma, as páginas mais recentemente usadas são mantidas na memória cache e as menos recentes são descartadas.

O LRU é eficiente porque assume que as páginas que foram usadas recentemente provavelmente serão usadas novamente em um futuro próximo. Além disso, ele é fácil de implementar e possui uma complexidade temporal O(1) para operações de inserção e remoção.

Em resumo, o algoritmo LRU é uma estratégia eficiente para gerenciar a memória cache, ajudando a maximizar o desempenho e evitar desperdício de espaço de armazenamento.

Neste exemplo, usamos a função lru_cache da biblioteca functools para cachear os resultados da função fibonacci. A função lru_cache aceita um argumento maxsize que especifica o tamanho máximo da cache. Quando a cache atinge sua capacidade máxima, o algoritmo LRU é usado para remover as entradas menos recentemente usadas. No nosso exemplo, definimos maxsize=None para permitir que a cache cresça indefinidamente.

Ao executar a função fibonacci(10), vemos que a saída é 55, que é o décimo número na sequência de Fibonacci. O resultado é calculado rapidamente porque os valores intermediários são armazenados na cache, evitando a recomputação.

Existe um limite máximo para o número n que um computador pode usar neste exemplo, pois a função fibonacci usa recursão e cada chamada da função adiciona uma entrada à pilha de chamadas. Se n for muito grande, a pilha de chamadas pode atingir seu limite e causar um erro de pilha cheia (stack overflow).

O tamanho máximo da pilha depende da quantidade de memória disponível no sistema, bem como da implementação da linguagem de programação. Em geral, o tamanho máximo da pilha é de alguns megabytes, o que significa que o valor máximo de n que um computador pode usar depende da complexidade da função fibonacci.

Como a função fibonacci usa a fórmula fibonacci(n) = fibonacci(n-1) + fibonacci(n-2), o tamanho da pilha aumenta exponencialmente com o aumento de n. Em geral, o valor máximo de n que um computador pode usar sem sofrer um erro de pilha cheia é de cerca de 1000 a 1500, dependendo da configuração do sistema.

Para calcular valores maiores de n, é necessário usar outras abordagem, como a programação dinâmica ou a utilização de matrizes para calcular a sequência de Fibonacci.
