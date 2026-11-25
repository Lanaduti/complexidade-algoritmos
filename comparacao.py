"""
Comparação dos algoritmos
Responsável: Pessoa 3 (integração)

Este arquivo importa as funções dos três arquivos do projeto, executa
testes com diferentes quantidades de elementos, mede os tempos com
time.perf_counter() e mostra uma tabela no terminal.

Observação importante:
    Os tempos são MEDIÇÕES EXPERIMENTAIS. Eles variam conforme o computador,
    os programas abertos, etc. A notação Big-O é uma análise TEÓRICA: ela
    descreve como o número de operações cresce quando n cresce. As medições
    servem para OBSERVAR essa tendência na prática, não para prová-la.
"""

import random
import time

# Importa as funções dos três arquivos (precisam estar na mesma pasta)
from busca_linear import busca_linear
from busca_binaria import busca_binaria
from bubble_sort import bubble_sort


def medir_tempo(funcao, *argumentos):
    """
    Executa 'funcao' com os 'argumentos' informados e mede o tempo gasto.

    Retorna:
        (resultado da função, tempo em milissegundos)
    """
    inicio = time.perf_counter()
    resultado = funcao(*argumentos)
    fim = time.perf_counter()
    return resultado, (fim - inicio) * 1000


def imprimir_tabela(linhas):
    """Mostra os resultados no formato de tabela no terminal."""
    cabecalho = f"| {'Algoritmo':<14} | {'Quantidade de elementos':>23} | {'Tempo de execução':>17} | {'Complexidade':<12} |"
    separador = "-" * len(cabecalho)
    print(separador)
    print(cabecalho)
    print(separador)
    for algoritmo, quantidade, tempo_ms, complexidade in linhas:
        print(f"| {algoritmo:<14} | {quantidade:>23,} | {tempo_ms:>14.4f} ms | {complexidade:<12} |")
    print(separador)


def comparar_buscas():
    """
    Compara Busca Linear e Busca Binária usando os MESMOS números e o MESMO alvo.
    """
    print("\n1) BUSCAS — Busca Linear x Busca Binária")
    print("   As duas procuram o mesmo alvo, que NÃO existe na lista (pior caso).")
    print("   A ordenação da lista da busca binária é feita ANTES da medição.\n")

    linhas = []
    for tamanho in [1_000, 10_000, 100_000, 1_000_000]:
        # Gera os números de 0 a tamanho-1 e embaralha
        lista_desordenada = list(range(tamanho))
        random.shuffle(lista_desordenada)

        # Mesmos números, agora em ordem crescente (preparação, fora da medição).
        # sorted() é usado só para PREPARAR os dados; não faz parte da busca.
        lista_ordenada = sorted(lista_desordenada)

        # Alvo inexistente: força as duas buscas ao pior caso
        alvo = -1

        resultado_linear, tempo_linear = medir_tempo(busca_linear, lista_desordenada, alvo)
        resultado_binaria, tempo_binaria = medir_tempo(busca_binaria, lista_ordenada, alvo)

        # Confere se as duas buscas chegaram à mesma conclusão
        assert resultado_linear == -1 and resultado_binaria == -1

        linhas.append(("Busca Linear", tamanho, tempo_linear, "O(n)"))
        linhas.append(("Busca Binária", tamanho, tempo_binaria, "O(log n)"))

    imprimir_tabela(linhas)


def comparar_ordenacao():
    """
    Mede o Bubble Sort com quantidades menores de elementos,
    pois seu crescimento é quadrático.
    """
    print("\n2) ORDENAÇÃO — Bubble Sort")
    print("   Listas embaralhadas (caso médio), com tamanhos menores.\n")

    linhas = []
    for tamanho in [250, 500, 1_000, 2_000]:
        lista = list(range(tamanho))
        random.shuffle(lista)

        lista_ordenada, tempo = medir_tempo(bubble_sort, lista)

        # Confere se a ordenação ficou correta
        assert lista_ordenada == list(range(tamanho))

        linhas.append(("Bubble Sort", tamanho, tempo, "O(n²)"))

    imprimir_tabela(linhas)


def testes_basicos():
    """Testes rápidos para confirmar que os três arquivos foram integrados corretamente."""
    lista = [42, 7, 19, 3, 88, 15]
    ordenada = bubble_sort(lista)

    assert ordenada == [3, 7, 15, 19, 42, 88]
    assert busca_linear(lista, 19) == 2
    assert busca_binaria(ordenada, 19) == 3
    assert busca_linear(lista, 100) == -1
    assert busca_binaria(ordenada, 100) == -1
    assert busca_linear([], 1) == -1
    assert busca_binaria([], 1) == -1
    assert bubble_sort([]) == []
    print("Testes de integração: todos passaram! (os três arquivos foram importados)")


if __name__ == "__main__":
    # Fixa a "semente" dos números aleatórios para os testes serem repetíveis
    random.seed(42)

    print("=" * 80)
    print("COMPARAÇÃO DE ALGORITMOS — COMPLEXIDADE NA PRÁTICA")
    print("=" * 80)

    testes_basicos()
    comparar_buscas()
    comparar_ordenacao()

    print("\nCOMO LER OS RESULTADOS:")
    print("- Busca Linear: lista 10x maior -> tempo cerca de 10x maior (O(n)).")
    print("- Busca Binária: lista 1000x maior -> tempo quase igual (O(log n)).")
    print("- Bubble Sort: lista 2x maior -> tempo cerca de 4x maior (O(n²)).")
    print("\nAtenção: os tempos são medições experimentais e mudam de um computador")
    print("para outro. A notação Big-O é uma análise teórica do crescimento.")
