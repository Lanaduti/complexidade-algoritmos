"""
Bubble Sort — Complexidade O(n²)
Responsável: Pessoa 3

Ideia do algoritmo:
    1. Percorre a lista comparando cada elemento com o seu VIZINHO da direita.
    2. Se estiverem na ordem errada (o da esquerda é maior), troca os dois.
    3. Ao final de uma passada, o MAIOR elemento "borbulha" até o final da lista.
    4. Repete as passadas até a lista inteira estar ordenada.

Por que a complexidade média e de pior caso é O(n²)?
    - Existem DOIS laços, um dentro do outro.
    - O laço de fora faz até n-1 passadas.
    - O laço de dentro compara vizinhos: na 1ª passada faz n-1 comparações,
      na 2ª faz n-2, depois n-3, ..., até 1.
    - Total de comparações: (n-1) + (n-2) + ... + 1 = n(n-1)/2
    - n(n-1)/2 = (n² - n)/2. Em Big-O ignoramos constantes e termos menores,
      sobrando n². Logo, O(n²).
    - PIOR caso: lista em ordem decrescente (toda comparação gera troca).
    - Caso MÉDIO: lista embaralhada, também cerca de n²/2 comparações -> O(n²).
    - Na prática: se n dobra, o tempo fica cerca de 4x maior (2² = 4).

Otimização usada (parada antecipada):
    - Se uma passada inteira acontecer SEM nenhuma troca, a lista já está
      ordenada e o algoritmo para.
    - Com isso, o MELHOR caso (lista já ordenada) faz só 1 passada com
      n-1 comparações -> O(n).
"""

import random
import time


def bubble_sort(lista):
    """
    Ordena uma lista de números em ordem crescente usando Bubble Sort.

    Recebe:
        lista -> lista de números (desordenada ou não)

    Retorna:
        uma NOVA lista com os mesmos números em ordem crescente.
        A lista original não é alterada.
        Se a lista for vazia, retorna uma lista vazia.
    """
    # Faz uma cópia para não modificar a lista original de quem chamou a função.
    # (Assim a mesma lista pode ser reutilizada em outros testes.)
    resultado = lista[:]
    n = len(resultado)

    # Laço externo: cada volta é uma "passada" pela lista
    for passada in range(n - 1):
        houve_troca = False  # Controla a otimização de parada antecipada

        # Laço interno: compara vizinhos.
        # Os últimos 'passada' elementos já estão no lugar certo,
        # por isso o limite diminui a cada passada.
        for i in range(n - 1 - passada):
            # Se o elemento da esquerda é maior que o da direita, estão fora de ordem
            if resultado[i] > resultado[i + 1]:
                # Troca os dois vizinhos de lugar
                resultado[i], resultado[i + 1] = resultado[i + 1], resultado[i]
                houve_troca = True

        # Se nenhuma troca aconteceu nesta passada, a lista já está ordenada
        if not houve_troca:
            break

    return resultado


# ---------------------------------------------------------------------------
# Tudo abaixo só executa quando rodamos: python bubble_sort.py
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("BUBBLE SORT — O(n²)")
    print("=" * 60)

    # ---------------- Exemplo simples ----------------
    numeros = [42, 7, 19, 3, 88, 15]
    ordenada = bubble_sort(numeros)
    print(f"\nLista original: {numeros}")
    print(f"Lista ordenada: {ordenada}")

    # ---------------- Testes básicos ----------------
    assert bubble_sort([5, 2, 9, 1, 7]) == [1, 2, 5, 7, 9]      # desordenada
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]      # já ordenada (melhor caso)
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]      # invertida (pior caso)
    assert bubble_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]      # com repetidos
    assert bubble_sort([-4, 10, 0, -1]) == [-4, -1, 0, 10]      # com negativos
    assert bubble_sort([]) == []                                # lista vazia
    assert bubble_sort([7]) == [7]                              # um elemento
    original = [3, 2, 1]
    bubble_sort(original)
    assert original == [3, 2, 1]                                # original não é alterada
    print("\nTestes básicos: todos passaram!")

    # ---------------- Medição de tempo ----------------
    # Tamanhos pequenos, pois o crescimento é quadrático.
    # random.seed fixa os números sorteados, para os testes serem repetíveis.
    random.seed(42)
    print("\nTempo com listas embaralhadas (caso médio):")
    print(f"{'Elementos':>12} | {'Tempo (ms)':>12}")
    print("-" * 28)

    for tamanho in [250, 500, 1_000, 2_000]:
        lista_teste = random.sample(range(tamanho * 10), tamanho)  # números aleatórios sem repetição

        inicio = time.perf_counter()
        bubble_sort(lista_teste)
        fim = time.perf_counter()

        tempo_ms = (fim - inicio) * 1000
        print(f"{tamanho:>12} | {tempo_ms:>12.4f}")

    print("\nObserve: quando a quantidade de elementos dobra, o tempo fica")
    print("aproximadamente 4x maior. Isso é o crescimento quadrático O(n²).")
    print("(Os tempos são medições experimentais e variam de máquina para máquina.)")
