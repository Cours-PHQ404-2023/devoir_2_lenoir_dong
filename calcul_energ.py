from construction_ham import ham
from math import *
from scipy import linalg
import numpy as np

J=1

f = open('calcul_energ_data.txt','w')

def energ(N) : 
    H = ham(J,N)

    eig_val = linalg.eig(H)[0].real


    for k in range(len(eig_val)) : 
        eig_val[k] = int(1000*eig_val[k])/1000 #on arrondit
        if abs(eig_val[k]-int(eig_val[k])) < 0.01 :
            eig_val[k] = int(eig_val[k])
        elif abs(eig_val[k]-(int(eig_val[k])+1)) < 0.01 :
            eig_val[k] = int(eig_val[k])+1
        elif abs(eig_val[k]-(int(eig_val[k])-1)) < 0.01 :
            eig_val[k] = int(eig_val[k])-1         #on associe toutes les valeurs proches des entiers aux entiers associés

    #print(eig_val)

    eig_val = set(eig_val)
    min1 = sorted(eig_val)[0]
    min2 = sorted(eig_val)[1]

    return min1, min2

for n in range(2,13) :  
    energies = energ(n)
    f.write(str(n)+' : E_0 = '+str(energies[0])+' et E_1 = '+str(energies[1])+'\n')
    
