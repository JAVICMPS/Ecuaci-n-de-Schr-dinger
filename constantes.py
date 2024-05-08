import numpy as np

N = 1000
T = 10000
n_ciclos = 250
landa = 0.8

#Paso de la posicion
h = 0.01

#Paso del tiempo
s_0 = 0.001

# Parametro s_tilde reescalada
s = s_0 / h**2

#Parametro k_tilde

k = 2*np.pi*n_ciclos/N

# Vector de posiciones

x = np.linspace(0, N * h, N + 1)