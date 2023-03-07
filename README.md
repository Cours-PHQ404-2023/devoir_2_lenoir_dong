# devoir_2_lenoir_dong
Les fichiers de ce second devoir sont organisés comme suit. Le rapport principal se nomme PHQ404_Devoir_2.pdf 

Il y a ensuite plusieurs fichiers python à éxecuter dans l'environnement détaillé par le fichier pyproject.toml

Le fichier construction_ham.py est le premier ficher, celui à éxecuter pour obtenir la construction du hamiltonien pour le système à N spins. 

Le fichier calcul_energ.py permet ensuite de calculer les deux niveaux de plus basses énergies, en utilisant la fonction décrite dans le fichier de construction du hamiltonien. Les résultats de ce calcul sont stockés dans le fichier calcul_energ_data.txt

Le fichier epsilon_alg.py décrit ensuite l'algorithme epsilon.

Le fichier verif_epsilon.py permet ensuite de vérifier cet algorithme, en utilisant les premières valeurs du développement en série de l'arctangente en zéro, pour obtenir une approximation de pi. 

Enfin, le fichier extrapolation.py permet d'utiliser l'algorithme epsilon pour extrapoler les valeurs limites de E_0/N et E_1-E_0, dont les premiers termes sont obtenus à partir du calcul des énergies précédemment effectué.
