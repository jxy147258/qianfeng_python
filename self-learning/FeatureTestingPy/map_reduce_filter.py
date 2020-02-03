def normalize(name):
    f=name[0].upper()
    s=name[1:].lower()
    return f+s

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
