from math import *
import numpy as np
from epsilon_alg import epsilon

energie_0 = [-1.5, -0.75, -2, -1.868, -2.802, -2.855, -3.651, -3.797, -4.515, -4.718, -5.387, -5.629]
energie_1 = [0.5, 0.75, -1, -0.75, -2.118, -1.806, -3.128, -2.936, -4.092, -4, -5.031, -5] #valeurs des énergies pour N=2:13

energie_0_sur_N = []
diff_energ      = []

for k in range(2,14) :
    energie_0_sur_N.append(energie_0[k-2]/k)
    diff_energ.append(energie_1[k-2] - energie_0[k-2])

energie_0_sur_N_pair   = []
energie_0_sur_N_impair = []
diff_energ_pair        = []
diff_energ_impair      = []

for k in range(2,14) : 
    if k%2==0 :
            energie_0_sur_N_pair.append(energie_0_sur_N[k-2])
            diff_energ_pair.append(diff_energ[k-2])
    else :

        energie_0_sur_N_impair.append(energie_0_sur_N[k-2])
        diff_energ_impair.append(diff_energ[k-2])


print(diff_energ)
#print(epsilon(energie_0_sur_N))
#print(epsilon(energie_0_sur_N_pair))
#print(epsilon(energie_0_sur_N_impair))

print(epsilon(diff_energ))
#print(epsilon(diff_energ_pair))
#print(epsilon(diff_energ_impair))
