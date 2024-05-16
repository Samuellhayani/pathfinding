# python-pathfinding

Recherche d'itinéraire, en Python

## Introduction

La recherche d'itinéraire est un problème très classique en informatique - recherche d'un itinéraire de A à B, de la meilleure allocation de trajets pour une livraison, des meilleures correspondances de train, du plus court chemin, du déplacement d'un personnage dans un jeu vidéo ...

On se propose ici d'étudier deux cas particuliers: trouver son chemin dans un labyrinthe parfait, et puis sur un terrain "ouvert" sans propriétes particulières. On fera un peu d'algo, et un peu de visualisation.

## Rendu

Le rendu se fait en trois partie:

1. `maze.py` qui contiendra votre algo (ou vos algos) de pathfinding. Ce fichier sera utilisé pour des tests automatisés, et vous pourrez voir votre note en éxécutant le grader.
2. Une commande pour lancer la visualisation d'un labyrinthe, par exemple `python visualisation.py data/perfect-small.txt`. Pas de format imposé.
3. Un fichier `rendu.md` qui contiendra:
   1. Des instructiosn pour lancer votre programme de visualisation, et un "manuel" explicatif s'il y a des fonctionnalités particulières ("appuyez sur `d` pour faire avancer le pion!") 
   2. Si vous avez essayé plusieurs algos, une petite explication sur ce qui fonctionne bien, ou pas, dans quel cas, etc
   3. Si vous êtes bloqués, quelques remarques sur "j'arrive à faire X mais pas Y, je pense que le problème c'est Z"

Le rendu se fait bien sûr sur Github. Pensez à faire des commits fréquents, et à pusher votre code.

```shell
# avant de commit, on vérifie que le grader fonctionne...
python grader.py
# ...

# et on commit
git add maze.py
git commit -m"labyrinthe: algo naïf"
git push
```

> :warning: Caveat emptor: Ce sujet n'est pas parfait, il y a peut-être des coquilles, et il y aura peut-être des corrections à appliquer
> au fur et à mesure, notamment dans les fichiers tests. Merci de votre compréhension.

## Notation

Les projets sont individuels. Il n'est pas interdit de communiquer - au contraire! Néanmoins, il vous est demander de ne pas copier-coller (ou recopier) du code directement.

Pour la note, les points seront attribués de la manière suivante:

- **50%** sur le fait "que ca marche", c'est à dire que les tests automatisés passent. Il n'est pas nécessaire que _tous_ les tests passent pour avoir 100% des points, il y a quelques tests "bonus"
- **30%** sur la visualisation. Vous avez beaucoup de latitude, mais le résultat devra donner toutes les informations requises, et être compréhensible rapidement. Points bonus pour une finition soignée, des "petits plus" ou pour les visualisations les plus ambitieuses.
- **20%** sur la qualité du code (simple, concis, bonnes structures de données, bonne structuration en fonctions et/ou classes), la lisibilité, les commentaires (suffisamment, mais pas trop non plus)

Globalement, rappelez-vous: il faut que ca fonctionne. Mieux vaut une visualisation incomplète, ou un peu moche, qu'une visualisation qui ne fonctionne pas du tout.

Enfin: il y a sans doute déjà une implémentation qui marche, quelque part sur internet. Cette implémentation n'intéresse pas le correcteur - c'est la vôtre qui compte. Et les étudiants des Mines ont en générales de bonnes ou très bonnes notes quand ils "font le job", quels que soient les résultats des tests auto.


## Première partie - le labyrinthe parfait

Vous allez commencer par résoudre un labyrinthe "parfait", c'est à dire où chaque "case" est atteignable depuis n'importe quelle case, et ce, de manière unique. En gros, le labyrinthe ne contient pas de "boucle" ni de cellule inacessible. Plus d'infos sur les labyrinthes sur [Wikipedia](https://fr.wikipedia.org/wiki/Mod%C3%A9lisation_math%C3%A9matique_d%27un_labyrinthe).

Une façon triviale, quoique non-optimale, de sortir d'un labyrinthe parfait est de poser la main sur un mur et le suivre, jusqu'à la sortie. On l'explique parfois comme "toujours tourner à droite" (ou à gauche, au choix), mais attention, c'est une manière incomplète de décrire le fonctionnement. Il y a souvent un mur à main droite, donc on ne peut pas "tourner" à droite, il faut avancer ... et plusieurs autres cas.

Les exemples de labyrinthes sont dans le dossier "data", par exemple [data/perfect-example.txt](data/perfect-example.txt).

Ils sont représentés de la manière suivante ():

```
#######
#     #
# ### #
# # # #
# # # #
s   # e
#######
```

- ` ` indique un chemin
- `#` indique un mur
- `s` le point de départ ("start")
- `e` le point de sortie attendu ("end")
- Pour cette partie, tous les labyrinthes sont parfaits.
- Pour cette partie, tous les labyrinthes sont valides, c'est à dire qu'on peut les résoudre.

Ci-dessus, un labyrinthe de 7x7. On considère que la case en haut à gauche à les coordonnées (0, 0). Sur cet exemple, on aura donc:

- `s` avec les coordonnées (0, 5)
- `e` avec les coordonnés (6, 5)


Le but est de produire un chemin de `s` vers `e`, et de le stocker dans un fichier. Le chemin indique les positions successives pour sortir.

Règles de résolution:

- On ne peut pas traverser un mur `#`
- On doit rester sur un `chemin`
- On ne peut se déplacer que verticalement ou horizontalement, pas en diagonale
- Le fichier contient toutes les positions successives pour arriver à la fin, avec les points `s` et `e` inclus
- Pas de numpy / matplotlib / etc etc, juste du Python pur.
- La résolution doit se faire en moins de 1 seconde

Un exemple de chemin valide pour le labyrinthe ci-dessus:

```
(0, 5)
(1, 5)
(1, 4)
(1, 3)
(1, 2)
(1, 1)
(2, 1)
(3, 1)
(4, 1)
(5, 1)
(5, 2)
(5, 3)
(5, 4)
(5, 5)
(6, 5)
```

Pour lancer le programme, il faudra remplir le fichier `maze.py`. Une fois n'est pas coutume, vous pouvez écrire des fonctions mais aussi du code en dehors des fonctions. Pour lancer le programme, l'utilisateur devra pouvoir taper dans son terminal:

```
python maze.py FICHIER_LABYRINTHE FICHIER_SOLUTION
```

Où:

- `FICHIER_LABYRINTHE` désigne un fichier contenant un labyrinthe
- `FICHIER_SOLUTION` désigne le fichier dans lequel écrire la solution

Par exemple pour résoudre le labyrinthe `perfect-small.txt` et mettre la soluton dans `perfect-small-solution.txt`

```
python maze.py data/perfect-small.txt perfect-small-solution.txt
```

Vous pouvez utiliser **n'importe quel algorithme** de votre choix pour résoudre le labyrinthe. Attention toutefois:
- Tourner toujours à gauche semble "trivial" pour un humain avec un crayon dans la main, mais n'est pas nécessairement le plus facile à implémenter.
- Pour les plus gros labyrinthes, ainsi que pour les labyrinthes non parfaits, il faudra faire autre chose.
- Documentez l'algorithme que vous avez choisi dans `.md`!

Avec ce premier algorithme, vous devriez être capable de résoudre les labyrinthes suivants, dans le dossier `data`:
- `perfect-example.txt`
- `perfect-example-reversed.txt`
- `perfect-small.txt`
- `perfect-small-middle.txt`
- `perfect-rectangle.txt`
- `perfect-big.txt`

Il est possible que le labyrinthe plus gros, `perfect-huge.txt` prenne beaucoup plus longtemps à résoudre - c'est une question bonus à la fin. De même, il n'est pas demandé de trouver le chemin le plus court dans le labyrinthe.

**Indices:**

- Pour lancer un programme avec des arguments genre `python monprogramme.py x y z`, regardez comment fonctionne `sys.argv`, voire le module `argparse`
- Attention à la représentation du labyrinthe dans votre programme. En effet, le fichier se lit "ligne par ligne". Donc vous allez lire tous les `x` pour `y=0`, puis tous les `x` pour `y=1`, etc. Faites bien attention à stocker les coordonnées sous la forme (y, x) plutôt que (x, y).
- Si vous suivez l'algorithme "toujours à gauche", attention aux cul-de-sac.
- Si vous arrivez à résoudre les "petits" labyrinthes mais que `perfect-big.txt` prend plus que 1 second, c'est qu'il y a un problème avec votre code. Réferrez-vous à l'[annexe 1 sur le profiling](#annexe-1---profiling)
- N'oubliez pas de lancer les tests...


## Interlude graphique


Vous devez maintennat implémenter une visualisation qui permet de:
- Sélectionner un labyrinthe de taille raisonnable (< 100 cases)
- L'afficher
- Afficher la solution

Vous pouvez utiliser ce que vous voulez en python pour l'affichage - du texte, pygame, Python Arcade, matplotlib (oh, les jolies [colormap](https://matplotlib.org/stable/tutorials/colors/colormaps.html)), de la 3D, des animations...

Pour la sélection du labyrinthe, ca peut se résumer à passer un argument à un programme en ligne de commande.

Dans `rendu.md`, vous devez:
- Lister les dépendances nécessaires pour faire tourner votre code (`pip install pygame matplotlib`)
  - Vous pouvez aussi vous renseigner sur `pip freeze` et `requirements.txt` si vous le souhaitez
- Expliquer comment lancer la visualisation et l'utiliser

L'attendu est que la visualisation soit:
1. Correcte
2. Compréhensible (si possible sans explications supplémentaires)


## Deuxième partie - cas général (pas parfait, en tout cas)

Dans le cas d'un parcours "non parfait", ou d'un "décor" en général, l'algorithme "poser sa main sur le mur" ne fonctionne pas. Notamment, s'il manque des murs, ou s'il y a des îlots. Par exemple:


```
    #    
         
    e   #
         
    #### 
    ##   
      s# 
```

Dans cas, il faut utiliser un autre algorithme - un algo de "pathfinding" classique. Il existe plein d'algos, à vous de trouver le vôtre. On peut citer les grands classiques: Lee, A*, Dijkstra - mais il en existe bien d'autres. Certains sont plus performants que d'autres, certains donnent "le plus court chemin", etc.

A vous de réfléchir un peu et choisir un algorithme dans la liste.

Implémentez le dans `pathfinding.py`, avec le même mode d'utilisation que `maze.py` .

Bien sûr, vous allez réutiliser des morceaux de codes venant de la première partie. Pensez à introduire un module (fichier python) contenant des fonctions ou des classes communes.

Vous devriez pouvoir résoudre:
- `data/pathfinding-example.txt`
- `data/pathfinding-medium.txt`
- `data/perfect-big.txt` ... eh oui, on devrait pouvoir résoudre _aussi_ des labyrinthes parfaits!


Il est possible que votre résolution soit trop lente pour résoudre raisonnablement `pathfinding-huge.txt` (le test vous laisse 2 secondes pour le résoudre). Si vous avez des problèmes de performance, c'est à dire que le code met trop longtemps à s'exécuter, réferrez-vous à l'[Annexe 1](#annexe-1).


## Questions bonus

Quelques questions bonus pour ceux qui sont passionnés.
Notez qu'il y a des tests auto dans le grader, mais ils sont notés sur 0, donc ils n'impactent pas
la note finale directement.

### Plus court chemin dans le labyrinthe

Vu ce que vous avez appris ci-dessus, pouvez-vous trouver le plus court chemin dans un labyrinthe?

Faites passez le test "shortest path", qui demande le plus court chemin dans `data/perfect-big.txt`. Est-ce que l'algorithme utiliser *garantit* le plus court chemin, ou est-ce une approximation? Détaillez dans `rendu.md`.

### And now, a _HUGE_ maze

Pour des points bonus, vous pouvez essayer de résoudre le labyrinthe `perfect-huge.txt` en moins de 5 secondes... 
Il va falloir profilier (cf Annexe 1), et être inventif sur les algos.
Moi-même je n'ai pas poussé jusqu'au bout, mais ca à l'air assez difficile. Pas garanti que ca soit possible, surtout sur des ordis milieu de gamme / pas hyper puissantes.
Ce qui compte pour avoir des points en plus, c'est la démarche, ainsi que l'explication, plus que le résultat. Détaillez dans `rendu.md`, et conservez les réalisations intermédiaires.

> :warning: Attention! Si vous profilez votre code et que vous l'améliorez, pensez à le sauvegarder dans un autre fichier (`pathfinding-unoptimized.py` ou similaire)
> et à expliquer ce que vous avez trouvé comme problème, et comment vous l'avez résolu, dans `rendu.md`!


## Annexe 1 - Profiling

Dans un exercice, le code est trop lent pour les tests. Il va vous falloir comprendre pourquoi. On peut le faire avec le module `cProfile` de Python ([documentation en Anglais](https://docs.python.org/3.10/library/profile.html#module-cProfile)):

```python
import cProfile
cProfile.run('ma_fonction(truc, machin, bidule')
```

Vous aurez une sortie du genre:

```
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.080    0.080   10.313   10.313 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:186(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
      491    0.000    0.000    0.003    0.000 codecs.py:319(decode)
  5497854    1.171    0.000    1.171    0.000 maze.py:17(move)
   524466    0.093    0.000    0.093    0.000 maze.py:23(gauche)
  2184029    0.387    0.000    0.387    0.000 maze.py:34(droite)
  1848833    3.504    0.000    4.039    0.000 maze.py:4(neighbors)
        1    4.194    4.194   10.234   10.234 maze.py:45(main)
        1    0.033    0.033    0.033    0.033 maze.py:51(<listcomp>)
      491    0.002    0.000    0.002    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000   10.313   10.313 {built-in method builtins.exec}
  3699669    0.268    0.000    0.268    0.000 {built-in method builtins.len}
        2    0.002    0.001    0.002    0.001 {built-in method io.open}
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
  5645995    0.397    0.000    0.397    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.003    0.003    0.006    0.006 {method 'readlines' of '_io._IOBase' objects}
     2001    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
  1848833    0.178    0.000    0.178    0.000 {method 'write' of '_io.TextIOWrapper' objects}
```

Dans laquelle vous trouverez le nom de vos fonctions (il est donc intéressant de faire des fonctions qui font une seule chose, pour mieux comprendre). Dans l'exemple ci-dessus:

```
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  5497854    1.171    0.000    1.171    0.000 maze.py:17(move)
   524466    0.093    0.000    0.093    0.000 maze.py:23(gauche)
  2184029    0.387    0.000    0.387    0.000 maze.py:34(droite)
  1848833    3.504    0.000    4.039    0.000 maze.py:4(neighbors)
        1    4.194    4.194   10.234   10.234 maze.py:45(main)
```

On voit que:
- Par exemple, la fonction `move` est appellée 5_497_852 fois (`ncalls`), et qu'au total ca prendre 1.171 secondes (`tottime`).
- La fonction `neighbors` est appellée 1_848_833 fois et prendre 3.504 secondes.

Il est donc intéressant de s'attaquer à la fonction `neighbors`, de la simplifier pour la rendre plus rapide, voire même de trouver comment faire sans ou l'appeler moins souvent.
