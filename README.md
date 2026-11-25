# Complexidade de Algoritmos na Prática

Trabalho da disciplina **Estruturas de Dados 2** — Unipê (Centro Universitário de João Pessoa)  
**Professor:** Edkallenn (Ed)  
**Tema:** Tema 3 — Complexidade de Algoritmos

## Integrantes

- **Alana Kelly** — Busca Linear (`busca_linear.py`)
- **Jayane Ellen** — Busca Binária (`busca_binaria.py`)
- **Leandra Gleyce** — Bubble Sort e comparação (`bubble_sort.py`, `comparacao.py`)

## Repositório

[https://github.com/Lanaduti/complexidade-algoritmos](https://github.com/Lanaduti/complexidade-algoritmos)

## Vídeo de apresentação

Link do vídeo: 

## Sobre o projeto

O projeto demonstra, por meio de códigos em Python, como a quantidade de dados influencia o desempenho de três algoritmos com complexidades diferentes.

| Algoritmo | Arquivo | Função | Retorno | Complexidade |
|---|---|---|---|---|
| Busca Linear | `busca_linear.py` | `busca_linear(lista, alvo)` | Posição do alvo ou `-1` | O(n) |
| Busca Binária | `busca_binaria.py` | `busca_binaria(lista_ordenada, alvo)` | Posição do alvo ou `-1` | O(log n) |
| Bubble Sort | `bubble_sort.py` | `bubble_sort(lista)` | Nova lista ordenada (crescente) | O(n²) |

### Busca Linear

Percorre a lista elemento por elemento até encontrar o valor procurado. No pior caso, verifica todos os `n` elementos, apresentando complexidade O(n).

### Busca Binária

Exige que a lista esteja ordenada. A cada etapa, descarta metade dos elementos, reduzindo o espaço de busca e apresentando complexidade O(log n).

### Bubble Sort

Compara elementos vizinhos e realiza trocas quando estão fora de ordem. Utiliza dois laços de repetição aninhados, gerando aproximadamente `n²/2` comparações. Com a parada antecipada quando não ocorrem trocas, seu melhor caso é O(n).

O arquivo `comparacao.py` importa as três funções, executa os algoritmos com diferentes quantidades de elementos e apresenta uma tabela com os tempos de execução.

Os tempos apresentados são medições experimentais e podem variar de acordo com o computador utilizado. Já a notação Big-O representa uma análise teórica do crescimento do número de operações.

## Estrutura do projeto

```text
complexidade-algoritmos/
├── busca_linear.py     # Busca Linear, exemplos, testes e medição de tempo
├── busca_binaria.py    # Busca Binária, exemplos, testes e medição de tempo
├── bubble_sort.py      # Bubble Sort, exemplos, testes e medição de tempo
├── comparacao.py       # Comparação dos três algoritmos
├── README.md           # Documentação do projeto
└── .gitignore          # Arquivos ignorados pelo Git
```

## Requisitos

- Python 3
- Não utiliza bibliotecas externas. São utilizadas apenas as bibliotecas `time` e `random`, disponíveis na instalação padrão do Python.

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/Lanaduti/complexidade-algoritmos
```

### 2. Acessar a pasta do projeto

```bash
cd complexidade-algoritmos
```

### 3. Executar os arquivos

```bash
python busca_linear.py
python busca_binaria.py
python bubble_sort.py
python comparacao.py
```

No Windows, caso o comando `python` não funcione, utilize `py` no lugar dele.

Cada arquivo individual apresenta um exemplo, executa testes básicos e mede o tempo de execução com listas de diferentes tamanhos. O arquivo `comparacao.py` apresenta uma tabela comparativa dos três algoritmos.