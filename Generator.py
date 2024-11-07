import numpy as np

def generator(finv, N=100):
    """Generador de una variable aleatoria X con función de distribución F.
    
    finv: Inversa de la función de distribución de X
    N: Número de valores a generar
    """
    
    np.random.seed(5)
    
    x = np.zeros(N)
    
    for i in range(N):
        U = np.random.uniform(0, 1)
        x[i] = finv(U)
        
    return x