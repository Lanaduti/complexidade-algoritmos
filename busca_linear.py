"""
Busca Linear — Complexidade O(n)
Responsável: Pessoa 1

Ideia do algoritmo:
    Percorrer a lista do primeiro ao último elemento, comparando cada um
    com o valor procurado (alvo). Se encontrar, devolve a posição. Se chegar
    ao fim sem encontrar, informa que o valor não existe na lista.

Por que a complexidade é O(n)?
    - "n" é a quantidade de elementos da lista.
    - No PIOR caso (o alvo está na última posição ou não existe), o laço
      precisa olhar TODOS os n elementos, fazendo n comparações.
    - Se a lista dobrar de tamanho, o número de comparações no pior caso
      também dobra. O crescimento é proporcional a n, por isso O(n).
    - MELHOR caso: o alvo está na primeira posição -> 1 comparação -> O(1).
    - Caso MÉDIO: em média, olhamos metade da lista (n/2). Na notação Big-O
      ignoramos constantes, então continua sendo O(n).

A lista NÃO precisa estar ordenada.
"""

import time


def busca_linear(lista, alvo):
    """
    Procura 'alvo' dentro de 'lista', elemento por elemento.

    Recebe:
        lista -> lista de números (ordenada ou não)
        alvo  -> número que será procurado

    Retorna:
        a posição (índice) do alvo na lista, se ele existir;
        -1, se o alvo não for encontrado (inclusive quando a lista é vazia).
    """
    # Percorre todas as posições da lista: 0, 1, 2, ..., n-1
    # Este laço é o que define a complexidade: ele pode rodar até n vezes.
    for posicao in range(len(lista)):
        # Compara o elemento atual com o valor procurado
        if lista[posicao] == alvo:
            return posicao  # Encontrou: devolve a posição e para a busca

    # Se o laço terminou, nenhum elemento era igual ao alvo
    return -1


# ---------------------------------------------------------------------------
# Tudo abaixo só executa quando rodamos: python busca_linear.py
# Quando outro arquivo faz "from busca_linear import busca_linear",
# este bloco NÃO é executado.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("BUSCA LINEAR — O(n)")
    print("=" * 60)

    # ---------------- Exemplo simples ----------------
    numeros = [42, 7, 19, 3, 88, 15]
    print(f"\nLista: {numeros}")

    resultado = busca_linear(numeros, 88)
    print(f"Procurando 88 -> posição {resultado}")

    resultado = busca_linear(numeros, 100)
    if resultado == -1:
        print("Procurando 100 -> não encontrado")

    # ---------------- Testes básicos ----------------
    # 'assert' gera um erro se a condição for falsa.
    # Se todos passarem, o programa segue normalmente.
    assert busca_linear([42, 7, 19, 3], 42) == 0   # primeiro elemento (melhor caso)
    assert busca_linear([42, 7, 19, 3], 3) == 3    # último elemento
    assert busca_linear([42, 7, 19, 3], 19) == 2   # elemento no meio
    assert busca_linear([42, 7, 19, 3], 99) == -1  # elemento inexistente
    assert busca_linear([], 5) == -1               # lista vazia
    assert busca_linear([5, 5, 5], 5) == 0         # repetidos: devolve a 1ª ocorrência
    print("\nTestes básicos: todos passaram!")

    # ---------------- Medição de tempo ----------------
    # Procuramos um valor que NÃO existe (-1) para forçar o pior caso:
    # o algoritmo precisa percorrer a lista inteira.
    print("\nTempo no pior caso (alvo inexistente):")
    print(f"{'Elementos':>12} | {'Tempo (ms)':>12}")
    print("-" * 28)

    for tamanho in [1_000, 10_000, 100_000, 1_000_000]:
        lista_teste = list(range(tamanho))  # [0, 1, 2, ..., tamanho-1]

        inicio = time.perf_counter()
        busca_linear(lista_teste, -1)
        fim = time.perf_counter()

        tempo_ms = (fim - inicio) * 1000
        print(f"{tamanho:>12} | {tempo_ms:>12.4f}")

    print("\nObserve: quando a lista fica 10x maior, o tempo fica")
    print("aproximadamente 10x maior. Isso é o crescimento linear O(n).")
    print("(Os tempos são medições experimentais e variam de máquina para máquina.)")
