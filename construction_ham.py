from scipy.sparse import kron
import numpy as np

S_x = 1/2*np.array([[0,1],[1,0]])
S_y = 1/2*np.array([[0,-1j],[1j,0]])
S_z = 1/2*np.array([[1,0],[0,-1]])

identity = np.array([[1,0],[0,1]])

def ham(J,N) :
    sum = 0

    sigma_x = []
    sigma_y = []
    sigma_z = []

    for i in range(N):
        if i==0:
            sigma_x.append(S_x)
            sigma_y.append(S_y)
            sigma_z.append(S_z)
        else :
            sigma_x.append(identity)
            sigma_y.append(identity)
            sigma_z.append(identity)
        for j in range(1,N):
            if j==i:
                sigma_x[i] = kron(sigma_x[i], S_x)
                sigma_y[i] = kron(sigma_y[i], S_y)
                sigma_z[i] = kron(sigma_z[i], S_z)
            else : 
                sigma_x[i] = kron(sigma_x[i], identity)
                sigma_y[i] = kron(sigma_y[i], identity)
                sigma_z[i] = kron(sigma_z[i], identity) 

    sigma_x2 = sigma_x.copy()
    sigma_y2 = sigma_y.copy()
    sigma_z2 = sigma_z.copy()

    for i in range(N) :
        if i==N-1 :
            sigma_x2[i] = sigma_x[0]
            sigma_y2[i] = sigma_y[0]
            sigma_z2[i] = sigma_z[0] 
        else :
            sigma_x2[i] = sigma_x[i+1]
            sigma_y2[i] = sigma_y[i+1]
            sigma_z2[i] = sigma_z[i+1]  

    for i in range(N) :
        sum = sum + sigma_x[i]*sigma_x2[i] + sigma_y[i]*sigma_y2[i] + sigma_z[i]*sigma_z2[i]

    sum = sum.toarray()
    sum = sum.real

    return J*sum

res = ham(4,3)
print(res)
