import math

def calcular_factor_friction(d, epsilon, nr):
    resultado = (0.25)/((math.log10((1/(3.7*(d/epsilon)))+(5.74/nr**0.9))))**2    
    return abs(round(resultado, 4))


def colebrook_white(epsilon, d, xi, nr, f):    
    resultado = -2 * math.log10((epsilon / (3.7 * d)) + (2.51 * xi) / (nr * math.sqrt(f)))
    return abs(round(resultado, 4))

def derivada_colebrook_white(epsilon, d, xi, nr):
    resultado = (-2 / math.log(10)) * ((2.51 / nr) / ((epsilon / (3.7 * d)) + ((2.51 * xi) / nr)))
    return abs(round(resultado, 4))

def calcular_xi(xi, fxi, dfxi):
    resultado = xi - ( fxi - xi / dfxi -1 )
    return abs(round(resultado, 4))

def calcular_factor_friction_i(xi):
    resultado = 1 / (xi ** 2)
    return abs(round(resultado, 4))