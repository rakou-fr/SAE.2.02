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
    
def fermeture_transitive(M):
    n = M.shape[0]
    F = M.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                F[i, j] = F[i, j] or (F[i, k] and F[k, j])
    return F

def fc(M):
    F = fermeture_transitive(M)
    return np.all(F == True)    
    
# print(graph2(10, 0.5, 10, 100))
# print(graph(14, 12, 15))
M = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1]], dtype=bool)
print(fc(M))


import numpy as np

def graph_bool(n, p):
    """
    Génère une matrice d'adjacence booléenne n x n, avec proportion p de 1 (arêtes) et 1-p de 0.
    """
    total = n * n
    nb_ones = int(total * p)
    nb_zeros = total - nb_ones
    elements = np.array([1]*nb_ones + [0]*nb_zeros)
    np.random.shuffle(elements)
    M = elements.reshape((n, n)).astype(bool)

    np.fill_diagonal(M, 1)
    return M


def fc(M):
    F = fermeture_transitive(M)
    return np.all(F == True)

def test_stat_fc(n, essais=500):
    """
    Génère 'essais' matrices d'adjacence n x n avec 50% de 1 et teste la forte connexité.
    Retourne le pourcentage de graphes fortement connexes.
    """
    count = 0
    for _ in range(essais):
        M = graph_bool(n, p=0.5)
        if fc(M):
            count += 1
    pourcentage = 100 * count / essais
    return pourcentage


for n in range(2, 21):
    pct = test_stat_fc(n, essais=300)
    print(f"Pour n={n}, {pct:.1f}% de graphes fortement connexes")
    
print("\n ---------------------- \n")
    
    
def test_stat_fc2(n, essais=500):
    """
    Génère 'essais' matrices d'adjacence n x n avec 50% de 1 et teste la forte connexité.
    Retourne le pourcentage de graphes fortement connexes.
    """
    count = 0
    for _ in range(essais):
        M = graph_bool(n, p=1)
        if fc(M):
            count += 1
    pourcentage = 100 * count / essais
    return pourcentage


for n in range(2, 21):
    pct = test_stat_fc2(n, essais=300)
    print(f"Pour n={n}, {pct:.1f}% de graphes fortement connexes")
    
    
def seuil(n):
    p = 1
    precision=0.02
    while p >= 0:
        score = test_stat_fc(n)
        if score < 0.8:
            return round(p + precision, 3)
        p -= precision
    return 0.0
    

x=40
print("Seuil pour n=",x," :", seuil(x))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

