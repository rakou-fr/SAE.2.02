import numpy as np

def graph(n, a, b):
    """
    entrée : n int, taille M n*n : a et b int, poids intervalles a ==> b
    sortie : return matrice
    
    génère une matrice de taille n*n, avec 50% de coef inf. et 50% de coef de poids 
    entier avec une intervalle de [a, b]
    """
    
    if (type(a) == int and type(b) == int and type(n) == int and n > 0 and a <= b):
        total_elements = n * n
        motier = total_elements // 2

        valeurs = np.random.randint(a, b + 1, motier)

        elements = np.concatenate((np.full(motier, float('inf')), valeurs))
        
        if total_elements % 2 != 0:
            elements = np.append(elements, np.random.randint(a, b + 1))

        np.random.shuffle(elements)
        matrice = elements.reshape((n, n))
        matrice = matrice.astype("float64")

        return matrice
    else:
        return False

def graph2(n, p, a, b):
    """
    entrée : n int, taille M n*n, p float (proportion de flèches),
            a et b int, poids intervalles a ==> b pour les flèches
    sortie : return matrice
    
    génère une matrice de taille n*n, avec une proportion p de flèches (valeurs entre a et b)
    et le reste des éléments avec des infinis.
    """
    
    if (type(a) == int and type(b) == int and type(n) == int and type(p) == float and 0 <= p <= 1 and n > 0 and a <= b):
        total_elements = n * n
        
        numero_listes = int(np.random.binomial(total_elements, p))
        
        liste_valeurs = np.random.randint(a, b + 1, numero_listes)
        
        elements = np.concatenate((np.full(total_elements - numero_listes, float('inf')), liste_valeurs))
        
        np.random.shuffle(elements)
        
        matrice = elements.reshape((n, n))
        
        matrice = matrice.astype("float64")
        
        return matrice
    else:
        return False
    
# print(graph2(10, 0.5, 10, 100))
# print(graph(14, 12, 15))
