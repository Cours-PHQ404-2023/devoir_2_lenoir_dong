from math import *
import numpy as np

def epsilon(liste_S_n) : 
    n = len(liste_S_n)

    triangle = np.zeros((n+1,n+1)) #on initialise le triangle de l'algorithme (la pointe sera en bas !!!)

    for k in range(n+1) : 
        for j in range(n+1) : 
            if k==0 :
                triangle[k][j] = 0 #première ligne de zéro
            elif k==1:
                if j<=n-1:
                    triangle[k][j]=liste_S_n[j] #deuxième ligne avec les terme de la suite
            else :
                if j<=n-k :
                    if triangle[k-1][j+1] - triangle[k-1][j] == 0 : 
                        return "Erreur de division par zéro" #cas particulier si il y a division par zéro
                    else : 
                        triangle[k][j] = triangle[k-2][j+1] + 1/(triangle[k-1][j+1] - triangle[k-1][j]) #on applique la formule de l'algorithme
    #print(triangle)
    return triangle[n][0]

#Sn = [4, 8/3, 3.467, 2.8952, 3.33968]
#Sn = [2.0, 1.5, 1, 1.118, 0.6840000000000002, 1.049, 0.5229999999999997, 0.8610000000000002, 0.42300000000000004, 0.718, 0.35599999999999987, 0.6289999999999996, 0.3069999999999995, 0.5520000000000005, 0.27000000000000046, 0.492, 0.24100000000000055, 0.44399999999999995]
#print(epsilon(Sn))
