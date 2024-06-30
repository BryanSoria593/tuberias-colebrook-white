import math
# d significa diametro
# e significa rugosidad
# h_l significa perdida de carga
# v significa velocidad
# l significa longitud
# g significa gravedad

def calcular_velocidad(d, e, h_l, v, l):
    g = 9.81
    # Calcular la velocidad del flujo en un conducto
    primer_factor = (-2 * math.sqrt(2 * g * d * h_l)) / math.sqrt(l)
    segundo_factor = math.log10((e / (3.7 * d)) + (2.51 * v * math.sqrt(l) / (d * math.sqrt(2 * g * d * h_l))))
    velocidad_flujo = primer_factor * segundo_factor
    return abs(round(velocidad_flujo, 4))

def perdida_friccion(H, z2, km, vel):
    g = 9.81
    resultado = H - z2 - km * vel**2 / (2 * g)
    return abs(round(resultado, 4))
