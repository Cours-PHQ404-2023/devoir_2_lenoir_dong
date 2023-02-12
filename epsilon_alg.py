from math import *
import numpy as np

def epsilon(liste_S_n) : 
    n = len(liste_S_n)

    triangle = np.zeros((n+1,n+1))

    for k in range(n+1) : 
        for j in range(n+1) : 
            if k==0 :
                triangle[k][j] = 0
            elif k==1:
                if j<=n-1:
                    triangle[k][j]=liste_S_n[j]
            else :
                if j<=n-k :
                    triangle[k][j] = triangle[k-2][j+1] + 1/(triangle[k-1][j+1] - triangle[k-1][j])
    return triangle[n][0]

Sn = [4, 8/3, 3.467, 2.8952]

#print(epsilon(Sn))
