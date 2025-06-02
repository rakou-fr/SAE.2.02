import numpy as np
import random
import matplotlib.pyplot as plt

def pp(M, s):
    N=M
    n=len(N)
    couleur={}
    for i in range(n):
        couleur[i]='blanc'
    couleur[s]='vert'
    pile=[s]
    parcours=[s]
    while pile != []: #Tant que la pile n'est pas vide
        i = pile[-1]    # on prend le dernier sommet i
        succ=[]         # on creer la liste de ses successeur
        for j in range(n):  
            if (M[i,j]>=1 and couleur[j]=='blanc'):
                succ.append(j)
        if succ != []: # si il y en a
            v = succ[0]     #on prend le preier
            couleur[v] = 'vert' #on le colorie en vert
            parcours.append(v)  #on l'empile dans le parcours resultat
            pile.append(v)      #on l'empile
        else:   #sinon
            pile.pop()  #on sort i de la pile
    return parcours

print("Exercice 21")
M=np.array([[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,0,1,0,0],[0,1,0,0,0]])
def pl(M,s) :
    n= len(M)
    Couleur = {}
    for i in range (n):
        Couleur[i]='blanc'
        Couleur[s]='vert'
        file=[s]
        Parcours=[s]
        while file !=[]:
            i=file[0]
            for j in range (n):
                if M[file[0]][j]>= 1: 
                    file.append(j)
                    Couleur[j]='vert'
                    Parcours.append(j)
                    file.pop(0)
                    return(Parcours)

M=np.array([[0,0,1,1,0,0,0],[1,0,0,0,1,0,0],[0,1,0,1,0,0,0],[0,0,0,0,1,0,1],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0],[0,1,0,0,0,0,0]])

Resultat = pl(M ,0)
print("Résultat :", Resultat)


def dijkstra2(M, s0, s1):
    n = len(M)
    dist = {i: np.inf for i in range(n)}
    pred = {i: None for i in range(n)}
    dist[s0] = 0
    A = set()
    while s1 not in A:
        s = min((i for i in range(n) if i not in A), key=lambda x: dist[x], default=None)
        if s is None or dist[s] == np.inf:
            return "Sommet non joignable à d par un chemin dans le graphe G."
        A.add(s)
        for t in range(n):
            if M[s][t] > 0 and t not in A:
                if dist[s] + M[s][t] < dist[t]:
                    dist[t] = dist[s] + M[s][t]
                    pred[t] = s
    chemin = []
    courant = s1
    while courant is not None:
        chemin.append(courant)
        courant = pred[courant]
    chemin = chemin[::-1]

    return dist[s1], chemin


M=np.array([[0,0,1,1,0,0,0],[1,0,0,0,1,0,0],[0,1,0,1,0,0,0],[0,0,0,0,1,0,1],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0],[0,1,0,0,0,0,0]])       
print("Ex 24")
resultat = pp(M, 0)
print("resultat :", resultat)

print("Test 1 : ")
dist, chemin = dijkstra2(M, 1, 3)
print(dist, chemin)




import numpy as np

def dijkstraVV2(M, depart):
    n = len(M)
    dist = {i: np.inf for i in range(n)}
    pred = {i: None for i in range(n)}
    dist[depart] = 0
    A = set()
    # Algorithme de Dijkstra classique
    while len(A) < n:
        # Cherche le sommet non traité avec la plus petite distance
        s = min((i for i in range(n) if i not in A), key=lambda x: dist[x], default=None)
        if s is None or dist[s] == np.inf:
            break  # Plus de sommets accessibles
        A.add(s)
        for t in range(n):
            if M[s][t] > 0 and t not in A:
                if dist[s] + M[s][t] < dist[t]:
                    dist[t] = dist[s] + M[s][t]
                    pred[t] = s

    # Construction des chemins pour chaque sommet
    ListeChemin = {}
    for arrivee in range(n):
        if dist[arrivee] == np.inf: # Si la distance est infini alors 
            ListeChemin[f"{depart} → {arrivee}"] = "Sommet non joignable"
            continue # ignore la contruction du chemin pour les sommets non joignables
        chemin = []
        courant = arrivee
        while courant is not None:
            chemin.append(courant)
            courant = pred[courant]
        chemin = chemin[::-1]
        chemin_str = ' → '.join(str(i) for i in chemin)
        ListeChemin[chemin_str] = dist[arrivee]
    return ListeChemin

#Exemple d'utilisation
M = np.array([
    [0,0,1,1,0,0,0],
    [1,0,0,0,1,0,0],
    [0,1,0,1,0,0,0],
    [0,0,0,0,1,0,1],
    [0,0,0,0,0,1,0],
    [0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0]
])

resultat = dijkstraVV2(M, 0)
for chemin, distance in resultat.items():
    print(f"Chemin : {chemin} | Distance : {distance}")

    

graphe = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', -1),
    ('C', 'D', 2),
    ('D', 'B', 1)
]



def bellman_fordPP(M, s0):
    print("test bellmanford PP")
    ordre = pp(M, s0)
    n = len(M)
    dist = [float('inf')] * n
    pred = [None] * n
    dist[s0] = 0
    pred[s0] = s0
    F = []
    for x in ordre:
        for y in range(n):
            if M[x][y] != 0:
                F.append((x, y, M[x][y]))
    modification = True
    iteration = 0   
    while modification and iteration < n:
        modification = False
        for (x, y, z) in F:
            if dist[x] + z < dist[y]:
                dist[y] = dist[x] + z
                pred[y] = x
                modification = True
        iteration += 1

    if iteration == n:
        return (None, None, "Cycle négatif détecté !")
    
    chemins = {}
    conteur = 0
    for v in range(n):
        if dist[v] == float('inf'):
            chemins[v] = None
        else:
            chemin = []
            current = v
            while current != s0:
                chemin.append(current)
                current = pred[current]
                conteur +=1
            chemin.append(s0)
            chemins[v] = (dist[v], list(reversed(chemin)), conteur)
            conteur = 0
    return (chemins)

def pl2(M, s):
    n = len(M)
    Couleur = {i: 'blanc' for i in range(n)}
    Couleur[s] = 'vert'
    file = [s]
    Parcours = [s]
    while file:
        i = file.pop(0)
        for j in range(n):
            if M[i][j] >= 1 and Couleur[j] == 'blanc':
                file.append(j)
                Couleur[j] = 'vert'
                Parcours.append(j)
    return Parcours

def bellman_fordPL(M, s0):
    print("test bellmanford PL")
    ordre = pl2(M, s0)
    n = len(M)
    dist = [float('inf')] * n
    pred = [None] * n
    dist[s0] = 0
    pred[s0] = s0
    F = []
    for x in ordre:
        for y in range(n):
            if M[x][y] != 0:
                F.append((x, y, M[x][y]))
    modification = True
    iteration = 0   
    while modification and iteration < n:
        modification = False
        for (x, y, z) in F:
            if dist[x] + z < dist[y]:
                dist[y] = dist[x] + z
                pred[y] = x
                modification = True
        iteration += 1

    if iteration == n:
        return (None, None, "Cycle négatif détecté !")
    
    chemins = {}
    conteur = 0
    for v in range(n):
        if dist[v] == float('inf'):
            chemins[v] = None
        else:
            chemin = []
            current = v
            while current != s0:
                chemin.append(current)
                current = pred[current]
                conteur+=1
            chemin.append(s0)
            chemins[v] = (dist[v], list(reversed(chemin)), conteur)
            conteur=0
    return (chemins)

def bellman_ford(M, s0):
    print("test bellmanford oui")
    liste = []
    for i in range(len(M)):
        liste.append(i)
    random.shuffle(liste)
    n = len(M)
    dist = [float('inf')] * n
    pred = [None] * n
    dist[s0] = 0
    pred[s0] = s0
    F = []
    for x in liste:
        for y in range(n):
            if M[x][y] != 0:
                F.append((x, y, M[x][y]))
    modification = True
    iteration = 0   
    while modification and iteration < n:
        modification = False
        for (x, y, z) in F:
            if dist[x] + z < dist[y]:
                dist[y] = dist[x] + z
                pred[y] = x
                modification = True 
        iteration += 1

    if iteration == n:
        return (None, None, "Cycle négatif détecté !")
    
    chemins = {}
    conteur = 0
    for v in range(n):
        if dist[v] == float('inf'):
            chemins[v] = None
        else:
            chemin = []
            current = v
            while current != s0:
                chemin.append(current)
                current = pred[current]
                conteur += 1
            chemin.append(s0)
            chemins[v] = (dist[v], list(reversed(chemin)), conteur)
            conteur = 0
    return (chemins)

M = np.array([
    [0,0,1,1,0,0,0],
    [1,0,0,0,1,0,0],
    [0,1,0,1,0,0,0],
    [0,0,0,0,1,0,1],
    [0,0,0,0,0,1,0],
    [0,0,0,0,1,0,0],
    [0,1,0,0,0,1,0]
])

M2 = np.array([
    [0,0,2,2,0,0,0],
    [2,0,0,0,2,0,0],
    [0,2,0,2,0,0,0],
    [0,0,0,0,2,0,2],
    [0,0,0,0,0,2,0],
    [0,0,0,0,2,0,0],
    [0,2,0,0,0,0,0]
])
resultat = bellman_fordPP(M2, 3)
resultat2 = bellman_fordPL(M2, 3)
resultat3 = bellman_ford(M2, 3)
print()
print("test bellmanford")
print(resultat)
print()
print(resultat2)
print()
print(resultat3)
print()

M=np.array([[0,0,1,1,0,0,0],[1,0,0,0,1,0,0],[0,1,0,1,0,0,0],[0,0,0,0,1,0,1],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0],[0,1,0,0,0,0,0]])       
print("Ex 24")
resultat = pl(M, 0)
print("resultat :", resultat)

def MatAlea(n):
    matrice = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(random.randint(0, 9))
        matrice.append(ligne)

    return matrice


#import math
from timeit import default_timer

def TempsDij(n):
    M = MatAlea(n)
    debut = default_timer()
    resultat = dijkstraVV2(M, 0)
    time=default_timer() - debut
    print(time,"s")
    print(M)
    return time
    
def TempsBF(n):
    M = MatAlea(n)
    debut = default_timer()
    resultat = dijkstraVV2(M, 0)
    time=default_timer() - debut
    print(time,"s")
    print(M) 
    return time

timeDij=TempsDij(5)
timeBF=TempsBF(5)

x = np.linspace(2, 200)
plt.figure()
plt.plot(x, TempsDij(x), 'red')
plt.plot(x, TempsBF(x), 'blue')
plt.show

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
    pct = test_stat_fc(n, essais=300)
    print(f"Pour n={n}, {pct:.1f}% de graphes fortement connexes")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







