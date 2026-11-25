"""
Busca Binária — Complexidade O(log n)
Responsável: Pessoa 2

Ideia do algoritmo:
    Funciona SOMENTE em listas ORDENADAS (em ordem crescente).
    1. Olha o elemento do meio da parte da lista que ainda está sendo analisada.
    2. Se for o alvo, terminou.
    3. Se o alvo for MAIOR que o elemento do meio, descarta a metade esquerda.
    4. Se o alvo for MENOR, descarta a metade direita.
    5. Repete até encontrar o alvo ou até não sobrar nenhum elemento.

Por que a complexidade é O(log n)?
    - A cada repetição, a quantidade de elementos que ainda podem conter o
      alvo cai pela METADE: n -> n/2 -> n/4 -> n/8 -> ... -> 1.
    - A pergunta é: "quantas vezes consigo dividir n por 2 até chegar em 1?"
      A resposta é log2(n).
    - Exemplo: 1.000.000 de elementos -> no máximo cerca de 20 comparações,
      pois 2^20 = 1.048.576.
    - Se a lista dobrar de tamanho, é necessária apenas UMA comparação a mais.
    - MELHOR caso: o alvo está exatamente no meio -> O(1).
    - PIOR caso (alvo não existe ou é achado no último passo) -> O(log n).

IMPORTANTE:
    Esta função NÃO ordena a lista. Ela supõe que a lista já chegou ordenada.
    Se a ordenação fosse feita aqui dentro, o custo da ordenação (que é maior
    que O(log n)) seria somado ao da busca e atrapalharia a análise.
"""

import time


def busca_binaria(lista_ordenada, alvo):
    """
    Procura 'alvo' dentro de 'lista_ordenada' dividindo a busca ao meio.

    Recebe:
        lista_ordenada -> lista de números em ordem CRESCENTE
        alvo           -> número que será procurado

    Retorna:
        a posição (índice) do alvo na lista, se ele existir;
        -1, se o alvo não for encontrado (inclusive quando a lista é vazia).
    """
    # 'inicio' e 'fim' marcam o trecho da lista que ainda pode conter o alvo.
    # No começo, o trecho é a lista inteira.
    inicio = 0
    fim = len(lista_ordenada) - 1  # Se a lista for vazia, fim = -1 e o laço nem começa

    # Enquanto o trecho tiver pelo menos um elemento
    while inicio <= fim:
        # Posição do meio do trecho atual ('//' é divisão inteira)
        meio = (inicio + fim) // 2

        if lista_ordenada[meio] == alvo:
            return meio  # Encontrou o alvo
        elif lista_ordenada[meio] < alvo:
            # O alvo é maior: ele só pode estar à DIREITA do meio.
            # Descartamos a metade esquerda (incluindo o meio).
            inicio = meio + 1
        else:
            # O alvo é menor: ele só pode estar à ESQUERDA do meio.
            # Descartamos a metade direita (incluindo o meio).
            fim = meio - 1

    # O trecho ficou vazio: o alvo não está na lista
    return -1


# ---------------------------------------------------------------------------
# Tudo abaixo só executa quando rodamos: python busca_binaria.py
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("BUSCA BINÁRIA — O(log n)")
    print("=" * 60)

    # ---------------- Exemplo simples ----------------
    numeros = [3, 7, 15, 19, 42, 88]  # Já está ordenada
    print(f"\nLista ordenada: {numeros}")

    resultado = busca_binaria(numeros, 42)
    print(f"Procurando 42 -> posição {resultado}")

    resultado = busca_binaria(numeros, 100)
    if resultado == -1:
        print("Procurando 100 -> não encontrado")

    # ---------------- Testes básicos ----------------
    assert busca_binaria([3, 7, 15, 19, 42], 15) == 2   # elemento do meio (melhor caso)
    assert busca_binaria([3, 7, 15, 19, 42], 3) == 0    # primeiro elemento
    assert busca_binaria([3, 7, 15, 19, 42], 42) == 4   # último elemento
    assert busca_binaria([3, 7, 15, 19, 42], 10) == -1  # inexistente (entre valores)
    assert busca_binaria([3, 7, 15, 19, 42], 1) == -1   # inexistente (menor que todos)
    assert busca_binaria([3, 7, 15, 19, 42], 99) == -1  # inexistente (maior que todos)
    assert busca_binaria([], 5) == -1                   # lista vazia
    assert busca_binaria([8], 8) == 0                   # lista com um elemento
    # Teste com lista ordenada grande: todos os elementos devem ser encontrados
    grande = list(range(0, 2000, 2))  # [0, 2, 4, ..., 1998]
    for i, valor in enumerate(grande):
        assert busca_binaria(grande, valor) == i
    print("\nTestes básicos: todos passaram!")

    # ---------------- Medição de tempo ----------------
    # list(range(n)) já gera uma lista ordenada, então não há custo de ordenação.
    # Procuramos -1 (inexistente) para forçar o pior caso.
    print("\nTempo no pior caso (alvo inexistente):")
    print(f"{'Elementos':>12} | {'Tempo (ms)':>12}")
    print("-" * 28)

    for tamanho in [1_000, 10_000, 100_000, 1_000_000]:
        lista_teste = list(range(tamanho))  # Criada ANTES da medição

        inicio = time.perf_counter()
        busca_binaria(lista_teste, -1)
        fim = time.perf_counter()

        tempo_ms = (fim - inicio) * 1000
        print(f"{tamanho:>12} | {tempo_ms:>12.4f}")

    print("\nObserve: mesmo com a lista 1000x maior, o tempo quase não muda.")
    print("Isso é o crescimento logarítmico O(log n).")
    print("(Os tempos são medições experimentais e variam de máquina para máquina.)")
