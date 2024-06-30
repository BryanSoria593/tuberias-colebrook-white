def calcular_nr(velocidad, diametro, densidad, viscosidad):
    nr = ( velocidad * diametro * densidad ) / viscosidad
    return round(nr, 4)

def calcular_rugosidad_relativa(epsilon, diametro):
    rugosidad = epsilon / diametro
    return round(rugosidad, 4)

def calcular_friccion(nr):
    nr = 64 / nr
    return round(nr, 4)

def calcular_hl(f, l, v, d):
    g = 9.81
    hl = f * (l / d) * (v ** 2) / (2 * g)
    return round(hl, 4)

def calcular_hf(hl, sum_hm):
    hf = hl + sum_hm
    return round(hf, 4)

def calcular_h(z2, hf):
    h = z2 + hf
    return round(h, 4)

def calcular_p(p,q,h):
    g = 9.81
    resultado_p = p * g * q * h
    return round(resultado_p, 4)