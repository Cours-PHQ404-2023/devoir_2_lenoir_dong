from math import *
import numpy as np
from epsilon_alg import epsilon
import matplotlib.pyplot as plt
import numpy as np

energie_0 = [-1.5, -0.75, -2, -1.868, -2.802, -2.855, -3.651, -3.797, -4.515, -4.718, -5.387, -5.629, -6.263, -6.533, -7.142, -7.433, -8.022, -8.33, -8.904]
energie_1 = [0.5, 0.75, -1, -0.75, -2.118, -1.806, -3.128, -2.936, -4.092, -4, -5.031, -5, -5.956, -5.981, -6.872, -6.941, -7.781, -7.886, -8.686] #valeurs des énergies pour N=2:20

energie_0_sur_N = []
diff_energ      = []

for k in range(2,21) :
    energie_0_sur_N.append(energie_0[k-2]/k)
    diff_energ.append(energie_1[k-2] - energie_0[k-2]) #on crée les liste E_0/N et E_1-E_0

energie_0_sur_N_pair   = []
energie_0_sur_N_impair = []
diff_energ_pair        = []
diff_energ_impair      = []

for k in range(2,21) : 
    if k%2==0 :
            energie_0_sur_N_pair.append(energie_0_sur_N[k-2])
            diff_energ_pair.append(diff_energ[k-2]) 
    else :
        energie_0_sur_N_impair.append(energie_0_sur_N[k-2])
        diff_energ_impair.append(diff_energ[k-2]) #on crée les mêmes listes avec les termes pairs ou impairs

print(epsilon(energie_0_sur_N))
print(epsilon(energie_0_sur_N_pair))
print(epsilon(energie_0_sur_N_impair))

print(epsilon(diff_energ))
print(epsilon(diff_energ_pair))
print(epsilon(diff_energ_impair))

n = np.linspace(2,21,19)
n_pair = np.arange(2,21,2)
n_impair = np.arange(3,21,2)

plt.figure()
plt.plot(n, energie_0_sur_N)
plt.plot(n, epsilon(energie_0_sur_N)*np.ones(19),label='Epsilon')
plt.xlabel('N')
plt.ylabel('E')
plt.legend()
plt.title('Convergence de E_0/N')
plt.savefig('Figures/E0_sur_N.png')
plt.show()

plt.figure()
plt.plot(n_pair, energie_0_sur_N_pair)
plt.plot(n_pair, epsilon(energie_0_sur_N_pair)*np.ones(len(energie_0_sur_N_pair)),label='Epsilon n pair')
plt.xlabel('N')
plt.ylabel('E')
plt.legend()
plt.title('Convergence de E_0/N avec n pair')
plt.savefig('Figures/E0_sur_N_pair.png')
plt.show()

plt.figure()
plt.plot(n_impair, energie_0_sur_N_impair)
plt.plot(n_impair, epsilon(energie_0_sur_N_impair)*np.ones(len(energie_0_sur_N_impair)),label='Epsilon n impair')
plt.xlabel('N')
plt.ylabel('E')
plt.legend()
plt.title('Convergence de E_0/N avec n impair')
plt.savefig('Figures/E0_sur_N_impair.png')
plt.show()

#plt.figure()
#plt.plot(n, diff_energ)
#plt.plot(n, epsilon(diff_energ)*np.ones(19),label='Epsilon')
#plt.xlabel('N')
#plt.ylabel('E')
#plt.legend()
#plt.title('Convergence de la différence d énergie')
#plt.savefig('Figures/diff_energ.png')
#plt.show() ne fonctionne pas avec tous les points

plt.figure()
plt.plot(n_pair, diff_energ_pair)
plt.plot(n_pair, epsilon(diff_energ_pair)*np.ones(len(diff_energ_pair)),label='Epsilon n pair')
plt.xlabel('N')
plt.ylabel('E')
plt.legend()
plt.title('Convergence de la différence d énergie avec n pair')
plt.savefig('Figures/diff_energ_pair.png')
plt.show()

plt.figure()
plt.plot(n_impair, diff_energ_impair)
plt.plot(n_impair, epsilon(diff_energ_impair)*np.ones(len(diff_energ_impair)),label='Epsilon n impair')
plt.xlabel('N')
plt.ylabel('E')
plt.legend()
plt.title('Convergence de la différence d énergie avec n impair')
plt.savefig('Figures/diff_energ_impair.png')
plt.show() #on crée toutes les figures souhaitées
