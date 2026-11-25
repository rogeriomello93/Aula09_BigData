def dobrado(x):
    d = x * 2
    return d

def triplo(y):
    t = y * 3
    return t

def quad(z):
    q = z * z
    return q


num = float(input('Digite um numero: '))

resultado = dobrado(num)
resultado1 = triplo(num)
resultado2 = quad(num)

print(f'O dobro do numero é:{resultado}')
print(f'O triplo do numero é:{resultado1}')
print(f'O triplo do numero é:{resultado2}')