# Exploration algorithmique d'un problème

## Introduction

Le projet "Exploration algorithmique d'un problème" a pour objectif d'explorer et de comparer deux algorithmes classiques utilisés pour résoudre le problème du plus court chemin dans un graphe pondéré : **Dijkstra** et **Bellman-Ford**. L'analyse sera axée sur la comparaison des performances des algorithmes en termes de rapidité, complexité, efficacité, ainsi que sur le traitement des cas d'erreur (poids négatifs, cycles négatifs).

## Objectifs

- Comparer les algorithmes de **Dijkstra** et **Bellman-Ford** dans des cas pratiques.
- Analyser les différences de **rapidité** et de **complexité** entre les deux algorithmes.
- Étudier les **cas d'erreurs** (gestion des poids négatifs et cycles négatifs).
- Évaluer l'**efficacité** des algorithmes sur différents types de graphes.

## Algorithmes Comparés

### Dijkstra

L'algorithme de Dijkstra trouve le plus court chemin d'un sommet source à tous les autres sommets dans un graphe avec des poids **positifs**. Il utilise une structure de données de type tas binaire (ou tas de Fibonacci) pour améliorer son efficacité.

#### Complexité :
- Temps : **O(E log V)**, où **E** est le nombre d'arêtes et **V** le nombre de sommets.
- Espace : **O(V)**.

### Bellman-Ford

L'algorithme de Bellman-Ford, contrairement à Dijkstra, peut gérer les graphes avec des **poids négatifs**. Il effectue des relaxations successives sur toutes les arêtes du graphe et peut détecter les **cycles de poids négatifs**.

#### Complexité :
- Temps : **O(V * E)**, où **E** est le nombre d'arêtes et **V** le nombre de sommets.
- Espace : **O(V)**.

## Cas Pratiques

### 1. Graphes avec des poids positifs

Dans un graphe avec des poids positifs, les deux algorithmes doivent donner des résultats identiques en termes de chemin le plus court. Cependant, leurs performances diffèrent selon la taille du graphe.

### 2. Graphes avec des poids négatifs

Bellman-Ford peut traiter des graphes avec des poids négatifs, ce qui n'est pas le cas de Dijkstra. Si Dijkstra est appliqué à un graphe avec des poids négatifs, il produira des résultats incorrects.

### 3. Cas d'erreurs et exceptions

- **Dijkstra** : Si le graphe contient des poids négatifs, l'algorithme échouera ou produira des résultats erronés.
- **Bellman-Ford** : Il peut détecter les cycles de poids négatifs, ce qui permet de signaler les erreurs lorsque ces cycles sont présents dans le graphe.

## Comparaison

| Critère                  | Dijkstra                    | Bellman-Ford                |
|--------------------------|-----------------------------|-----------------------------|
| **Cas d'utilisation**     | Poids positifs uniquement   | Poids négatifs autorisés    |
| **Complexité temporelle** | O(E log V)                  | O(V * E)                    |
| **Complexité spatiale**   | O(V)                        | O(V)                        |
| **Gestion des erreurs**   | Échoue sur poids négatifs   | Détecte les cycles négatifs |
| **Rapidité**              | Plus rapide pour les grands graphes sans poids négatifs | Moins rapide sur des graphes denses |
| **Efficacité**            | Plus efficace sur les graphes denses et avec des poids positifs | Plus efficace pour les graphes avec des poids négatifs |

## Exemple d'Exécution

### Préparation du graphe

Voici un exemple de graphe pour tester les algorithmes :

```python
graph = {
    0: [(1, 2), (2, 4)],
    1: [(2, 1), (3, 7)],
    2: [(3, 3)],
    3: []
}
