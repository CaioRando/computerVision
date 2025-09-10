# Atividade 1: Manipulação Básica de Imagem com OpenCV (Trilha VC)

## Desafio 1: Respostas e Implementações

### Questões Teóricas (Q1 e Q2)

**1. Explique por que o OpenCV usa BGR ao invés de RGB.**

O OpenCV utiliza o formato **BGR** (Azul, Verde, Vermelho) por padrão, em vez do RGB, principalmente devido a **razões históricas e de retrocompatibilidade**. Quando o OpenCV foi desenvolvido, o formato BGR era comum em alguns sistemas legados de hardware e software, como a estrutura de cor `COLORREF` do Windows. Essa escolha foi mantida para **garantir a compatibilidade** com o código existente.

**2. O que representa o pixel [0, 0]? Onde ele está localizado na imagem?**

O pixel **`[0, 0]`** representa o pixel na **primeira linha (índice 0)** e **primeira coluna (índice 0)** da matriz da imagem. Em sistemas de coordenadas de imagem (como no OpenCV), este pixel está sempre localizado no **canto superior esquerdo** da imagem.

### Questões Práticas (Q3, Q4 e Q5)

O script `desafio1.py` implementa:

* **Q3 (Pixels dos Cantos):** O código acessa e imprime os valores BGR dos pixels nas quatro extremidades da imagem.
* **Q4 (Cor Média):** O código calcula o valor médio dos canais B, G e R em toda a imagem.
* **Q5 (Predominância de Cor):** O código usa os valores de cor média para determinar qual canal (Vermelho, Verde ou Azul) é o predominante.

---

## Desafio 2: Alteração e Comparação Visual

O script `desafio2.py` executa as seguintes tarefas:

1. **Leitura** da imagem original (`cv2.imread()`).
2. **Modificação de Pixel:** Altera a cor de um pixel específico (ex: nas coordenadas `(150, 200)`) para um valor BGR definido (Ciano).
3. **Salvamento:** Salva a imagem modificada como `images/zuky_modificado.jpeg` (`cv2.imwrite()`).
4. **Visualização:** Exibe a imagem original e a modificada em janelas separadas (`cv2.imshow()`) para comparação visual.

---
