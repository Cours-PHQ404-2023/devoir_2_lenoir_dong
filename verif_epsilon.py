from epsilon_alg import epsilon
import numpy as np
from math import *

serie_4 = [4, 8/3, 52/15, 304/105]
serie_5 = serie_4 + [1052/315]
serie_6 = serie_5 + [10312/3465]
serie_7 = serie_6 + [147916/45045] #les quelques séries que l'on veut tester

series = [serie_4, serie_5, serie_6, serie_7]

res = []

for serie in series :
    print(epsilon(serie)) # ne donne une approximation convenable que pour un nombre de termes impairs dans la liste
