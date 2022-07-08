# Documentation
Une mini bibiliothèque python qui résout des problèmes Multi critères (supporte actuellement la méthode Electre uniquement).
Pour plus de solvers, réferrez vous à [Développement](#developpement).
## Comment utiliser
L'app a comme fichier d'entrée /app.py, ce dernier contient le code final à réaliser, toutes les opérations se font dans le fichier config.py et les fichiers des solvers.
Le fichier config.py contient le paramétrage nécessaire pour faire fonctionner l'app

# Solvers
Un solver est une classe qui doit impérativement contenir une méthode solve(), cette dernière prend les données d'une analyse et (sous format csv) et génére une solution en se basant sur un algorithme de résolution.
## Configuration
La première étape à réaliser est de configurer l'app, cette étape ne se fait pas directement depuis le fichier d'entré.
La première étape est d'aller dans le fichier /config.py dont le paramètre le plus important est le dictionnaire settings:

Le dictionnaire settings doit contenir (obligatoirement):
- **algorithm**: La classe du solver à utiliser 

```python
# From the config.py file
from algorithms.Electre.Electre import ElectreSolver

algorithm = ElectreSolver # Ou votre Solver
```

- **data**: Un dictionnaire sous ce format ou si vous utilisez un fichier csv (méthode recommandé):

```python
# In the config.py file

data = {
    "value 1": {"criteria 1": 2, "criteria 2": 5},
    "value 2": {"criteria 1": 4, "criteria 2": 3},
}

# Ou si vous avez un fichier csv 
data = Loader("path to csv").get_data()
```

- **poids**: Un dictionnaire sous ce format:

```python
# In the config.py file

poids = {
    "criteria 1": 2,
    "criteria 2": 4,
}

# Ou si vous avez un fichier csv
poids = Loader("path to csv").get_poids()
```

Puis, il faut tout sauvegarder dans le dictionnaire settings:

```python
# In the config.py file

settings = {
    "algorithm": algorithm,
    "data": data,
    "poids": poids
}

```

## Fichier CSV
L'app a été conçue pour fonctionner avec des fichiers csv, donc, c'est la méthode recommandée pour utiliser l'app.
Les attributs clé sont: 
- **\_\_algorithm_criteria_name\_\_**: (obligatoire) Les noms des critères, pour une bonne lisibilité, il est recommandé de le mettre en première ligne.
- **\_\_algorithm_poids\_\_**: (optionelle) Les poids des critères, si omise, les critère auront tous un poids identique.
- **\_\_algorithm_criteria_type\_\_**: (optionelle) Le type du critère (maximisation ou minimisation), prend en charge deux valeurs: "max" ou "min", si omise la valeur par défaut est "max"

```csv
__algorithm_criteria_name__, crit1, crit2
__algorithm_poids__, 6, 4
__algorithm_criteria_type__, max, min
proj 1, 1, 3 
proj 3, 1, 2
proj 4, 1, 1 
proj 5, 1, 3
proj 2, 5, 7
```

## Solution
Il est recommandé d'utiliser le fichier configuration.
Après avoir initialisé le dictionnaire settings, ce dernier sera utilisé dans la classe solution qui résoudra le problème en question, avec les paramètres renseignés dans le dictionnaire settings. À partir du code il est possible d'avoir le résultat juste de cette manière:
```python
# Depuis /app.py
from config import Solution

Solution().get() # Pour obtenir la solution.
```

## DominationGraph
La classe DominationGraph (chemin depuis la racine: "/tools/Graph.py").
Dans le cas où la classe fait une comparaison deux à deux, qui donne la liste des élément et les élélments qu'ils surclassent. c'est à dire tout solveur qui donne un résultat final du type:

```python

resultat_final = [
    [element1, element2], # Pour dire l'élément 1 surclasse l'élément 2
    [element1, element3], 
    [element2, element3]
]
```

Un graphe matérialisant cette méthode peut être obtenu de la sorte (il repose sur les deux bibliothèques [Networkx](https://networkx.org/) et [Matplotlib](https://matplotlib.org/))

```python

from tools.Graph import DominationGraph

DominationGraph(
    resultat_final
).show()
```

# Méthodes disponibles
## ELECTRE I
Multi criteria problem resolution using the ELECTRE I Method.
La classe du solver est "ElectreSolver" (chemin depuis la racine: "/algorithms/Electre/Electre.py")
### Graph
La méthode ELECTRE I est compatible avec la méthode DominationGraph.
```python


from tools.Graph import DominationGraph

DominationGraph(
    resultat_final
).show()
```

# Developpement
L'application est extensible et vous permet de rajouter vos propres solvers.
La création d'un Solver se fait en héritant de la classe Solver (chemin depuis la racine: "/algorithms/prototypes.py").
Il est préférable de créer un dossier (que l'on appellera pour la suite "custom").
On y mettrera nos solvers. 


```python
# From the config.py file
from algorithms.prototypes import Solver

class CustomSolver(Solver):
    def solve(self):
        return []
```

L'objectif étant que la méthode solve renvoie le résultat après traitement.