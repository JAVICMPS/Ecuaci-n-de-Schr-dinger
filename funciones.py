import numpy as np
import constantes as cte

def potencial():
    potencial = cte.landa * cte.k ** 2
    V = np.zeros(cte.N+1)
    for j in range(cte.N+1):
        if j <= 3/5 * cte.N and j>= 2/5 * cte.N:
            V[j] = potencial


    return V


def calc_phi():
    phi = np.zeros((cte.N+1, cte.T+1),complex)
    phi[0][0] = 0
    phi[cte.N][0] = 0
    for i in range(1, cte.N+1):
        phi[i][0] = np.exp(1j*cte.k*i)*np.exp(-(8*(4*i-cte.N)**2)/cte.N**2)

    return phi

def diagonal():
    A = np.zeros((cte.N+1),complex)
    V = potencial()
    for i in range(cte.N+1):
        A[i] = -2 + 2j/cte.s - V[i]

    return A

def calc_alpha():
    alpha = np.zeros((cte.N), complex)
    A = diagonal()
    for j in range(cte.N-1, 1, -1):
        gamma = 1 / (A[j] + alpha[j])
        alpha[j-1] = -gamma

    return alpha

def calc_b(b, phi, n):

    for j in range(cte.N):
            b[j][n] = 4*1j*phi[j][n]/cte.s

    return b

def calc_beta(alpha, b, beta, n):
    A = diagonal()
    for j in range(cte.N-1, 1, -1):
        gamma = 1 / (A[j] + alpha[j])
        beta[j-1][n] = gamma*(b[j][n] - beta[j][n])

    return beta


def calc_xi(xi, alpha, beta, n):

    for j in range(cte.N):
        xi[j+1][n] = alpha[j]*xi[j][n] + beta[j][n]

    return xi

def phi_sig(phi_ant, xi, n):

    for j in range(cte.N+1):
        phi_ant[j][n+1] = xi[j][n] - phi_ant[j][n]

    return phi_ant


def norma(norma, phi, n):
    for j in range(cte.N + 1):
        norma[j, n] = abs(phi[j, n]) ** 2
    return norma
def calc_norma_total(phi, n):
    norma_total = 0
    for j in range(cte.N+1):
        norma_total = norma_total + abs(phi[j][n])**2

    return norma_total










