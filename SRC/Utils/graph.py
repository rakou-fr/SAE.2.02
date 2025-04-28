import numpy as np

def graph(n, a, b):
    """
    entrée : n int, taille M n*n : a et b int, poids intervalles a ==> b
    sortie : return matrice
    
    génère une matrice de taille n*n, avec 50% de coef inf. et 50% de coef de poids 
    entier avec une intervalle de [a, b]
    """
    total_elements = n * n
    half = total_elements // 2

    values = np.random.randint(a, b + 1, half)

    elements = np.concatenate((np.full(half, float('inf')), values))
    
    if total_elements % 2 != 0:
        elements = np.append(elements, np.random.randint(a, b + 1))

    np.random.shuffle(elements)
    matrice = elements.reshape((n, n))
    matrice = matrice.astype("float64")

    return matrice

print(graph(12, 10, 15))
