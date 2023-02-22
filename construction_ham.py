from scipy import sparse
from scipy.sparse import kron
from scipy.sparse import identity
import numpy as np

S_x = 1/2*np.array([[0,1],[1,0]])
S_x = sparse.csr_matrix(S_x)

S_y = 1/2*np.array([[0,-1j],[1j,0]])
S_y = sparse.csr_matrix(S_y)

S_z = 1/2*np.array([[1,0],[0,-1]])
S_z = sparse.csr_matrix(S_z)

sigma_x = kron(S_x,identity(2))*kron(identity(2), S_x)
sigma_y = kron(S_y,identity(2))*kron(identity(2), S_y)
sigma_z = kron(S_z,identity(2))*kron(identity(2), S_z)
sigma   = sigma_x + sigma_y + sigma_z

def ham(J,N) :

    sum = 0

    for i in range(N):
        if i==0 : 
            mat = kron(sigma, identity(2**(N-2)))
        elif i==N-1 : 
            mat = kron(identity(2**(N-1)), S_x)*kron(S_x, identity(2**(N-1))) + kron(identity(2**(N-1)), S_y)*kron(S_y, identity(2**(N-1))) + kron(identity(2**(N-1)), S_z)*kron(S_z, identity(2**(N-1)))
        else : 
            mat = kron(identity(2**(i)), kron(sigma, identity(2**(N-i-2))))
        sum = sum + mat
    return J*sum.real

#res = ham(4,3)
#print(res)
