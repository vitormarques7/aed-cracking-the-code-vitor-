-----

<p align="center">
  <img alt="upe" src="./img/upe-logo.png"/>
</p>

-----

# Lista 05 — Hashing, Árvores e Grafos

Disciplina dos cursos de Engenharia de Software e Licenciatura em Computação  
da Universidade de Pernambuco — Campus Garanhuns

-----

## 📌 Sobre a lista

Esta é a última lista prática da disciplina e tem como objetivo consolidar os principais conceitos estudados nas unidades finais do curso.

Diferentemente das listas anteriores, esta atividade utiliza problemas inspirados em entrevistas técnicas e processos seletivos da indústria de software. O foco está no desenvolvimento do raciocínio algorítmico, na escolha adequada de estruturas de dados e na construção de soluções corretas e eficientes.

Serão trabalhados os seguintes conceitos:

- Hash Maps
- Recursão
- Árvores
- Busca em Profundidade (DFS)
- Grafos
- Menor Caminho
- Análise de Complexidade

Todas as soluções serão validadas por **testes automatizados com pytest**. Além da correção funcional, algumas questões também possuem restrições de complexidade assintótica.

-----

## 🎯 Objetivos de aprendizagem

Ao finalizar esta lista, você deverá ser capaz de:

- Utilizar Hash Maps para resolver problemas de busca e agrupamento
- Percorrer árvores utilizando estratégias recursivas
- Resolver problemas clássicos envolvendo grafos
- Aplicar algoritmos de busca em profundidade
- Implementar algoritmos de menor caminho
- Analisar a eficiência de soluções em termos de tempo e espaço

-----

## 🧠 Regras importantes

|     | Regra                                                                          |
| --- | ------------------------------------------------------------------------------ |
| ❌   | Não modificar os testes                                                        |
| ❌   | Não alterar as estruturas de dados fornecidas                                  |
| ❌   | Não utilizar bibliotecas externas não especificadas na lista                   |
| ❌   | Não utilizar implementações prontas encontradas na internet                    |
| ✅   | Implementar todas as funções solicitadas respeitando suas assinaturas          |
| ✅   | O código deve passar em todos os testes automatizados                          |
| ✅   | O código deve seguir o padrão definido pelo linter (`Flake8`)                  |
| ⚠️   | Algumas questões possuem requisitos mínimos de eficiência                      |
| ⚠️   | Soluções corretas podem falhar caso ultrapassem a complexidade máxima esperada |

-----

## 📦 Entregáveis

<details>
  <summary><strong>📤 Como entregar</strong></summary><br />

### Passo a passo da entrega

1. Aceite a atividade no GitHub Classroom
2. Clone o repositório criado automaticamente
3. Desenvolva sua solução
4. Faça commits regularmente
5. Envie suas alterações para o GitHub

### ⚠️ Importante

- A atividade deve ser desenvolvida individualmente
- A correção será realizada automaticamente através dos testes disponibilizados
- O resultado final será obtido a partir da última versão enviada antes do prazo

</details>

-----

## ⚙️ Configuração do ambiente

<details>
  <summary><strong>🚀 Passo a passo</strong></summary><br />

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd aed-challenges-05
```

2. Crie o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
python3 -m pip install -r dev-requirements.txt
```

</details>

-----

## 🔄 Fluxo de desenvolvimento

<details>
  <summary><strong>🔧 Antes de começar</strong></summary><br />

Verifique se todos os testes executam corretamente:

```bash
python3 -m pytest
```

</details>

<details>
  <summary><strong>💻 Durante o desenvolvimento</strong></summary><br />

Execute os testes frequentemente:

```bash
python3 -m pytest
```

Ou execute apenas um desafio específico:

```bash
python3 -m pytest tests/test_group_anagrams.py
```

</details>

-----

## 🗂️ Estrutura da Lista

```
.
├── img
├── README.md
├── dev-requirements.txt
├── challenges
│   ├── challenge_group_anagrams.py
│   ├── challenge_has_cycle.py
│   ├── challenge_tree_height.py
│   ├── challenge_lowest_common_ancestor.py
│   └── challenge_shortest_path.py
│
├── data_structures
│   ├── node.py
│   ├── tree.py
│   └── graph_examples.py
│
└── tests
    ├── test_group_anagrams.py
    ├── test_has_cycle.py
    ├── test_tree_height.py
    ├── test_lowest_common_ancestor.py
    └── test_shortest_path.py
```

-----

## 🧪 Testes

Executar todos os testes:

```bash
python3 -m pytest
```

Modo detalhado:

```bash
python3 -m pytest -s -vv
```

Executar um único arquivo de testes:

```bash
python3 -m pytest tests/test_tree_height.py
```

-----

## 🎛️ Linter

Esta lista utiliza Flake8 para padronização do código. Execute:

```bash
python3 -m flake8
```

-----

## 📈 Complexidade Assintótica

Alguns desafios possuem limites máximos de complexidade. Os testes automatizados verificarão se sua solução atende aos requisitos mínimos de eficiência.

| Notação    | Interpretação |
| ---------- | ------------- |
| O(1)       | Constante     |
| O(log n)   | Logarítmica   |
| O(n)       | Linear        |
| O(n log n) | Linearítmica  |
| O(n²)      | Quadrática    |

> Uma solução funcional não necessariamente será considerada correta caso sua complexidade exceda a esperada para o problema.

-----

## 🧩 Exercícios

### 1 — Agrupando Anagramas

> Implemente em `challenges/challenge_group_anagrams.py`

Dada uma lista de palavras, agrupe todas as palavras que sejam anagramas entre si.

**Exemplo:**

Entrada:

```python
group_anagrams(["amor", "roma", "mora", "carro", "arroc"])
```

Saída:

```python
[
    ["amor", "roma", "mora"],
    ["carro", "arroc"]
]
```

-----

### 2 — Detectando Ciclos em Grafos

> Implemente em `challenges/challenge_has_cycle.py`

Determine se um grafo possui ciclos. Retorne `True` caso exista pelo menos um ciclo, ou `False` caso contrário.

-----

### 3 — Altura de uma Árvore

> Implemente em `challenges/challenge_tree_height.py`

Utilizando as classes fornecidas, implemente uma função que retorne a altura de uma árvore.

-----

### 4 — Menor Ancestral Comum

> Implemente em `challenges/challenge_lowest_common_ancestor.py`

Dados dois nós pertencentes a uma árvore, determine o menor ancestral comum entre eles.

-----

### 5 — Menor Caminho

> Implemente em `challenges/challenge_shortest_path.py`

Utilizando o algoritmo de Dijkstra, determine:

- o menor custo entre dois vértices;
- o caminho correspondente.

-----

## ⚠️ Observações finais

- Leia os testes com atenção antes de implementar
- Pense na complexidade antes de escrever qualquer código
- Nem toda solução correta será eficiente o suficiente
- Não altere arquivos dentro de `tests/`
- Não altere as estruturas de dados fornecidas

-----

## 📚 Referências

- *Entendendo Algoritmos* — Aditya Bhargava
- *Cracking the Coding Interview* — Gayle Laakmann McDowell
- Material da disciplina
