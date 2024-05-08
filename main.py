import numpy as np
import os
import funciones as f
import constantes as cte
import animacion

phi = f.calc_phi()
alpha = f.calc_alpha()
b = np.zeros((cte.N, cte.T+1),complex)
beta = np.zeros((cte.N, cte.T+1),complex)
xi = np.zeros((cte.N+1, cte.T+1),complex)
norma = np.zeros((cte.N + 1, cte.T))
potencial = f.potencial()

print('Potencial = ', potencial)
print('Phi = ', phi)
print('Alpha = ', alpha)
print('Diagonal', f.diagonal())
for n in range(cte.T):
    b = f.calc_b(b, phi, n)
    beta = f.calc_beta(alpha, b, beta, n)
    xi = f.calc_xi(xi, alpha, beta, n)
    phi = f.phi_sig(phi, xi, n)
    norma = f.norma(norma, phi, n)
    norma_total = f.calc_norma_total(phi, n)


    print(n, norma_total)

if not os.path.exists('Results'):
    os.makedirs('Results')

probabilidad = norma / norma_total
V = np.real(potencial)
animacion.make_anim(probabilidad, cte.x, 'Results')







