a = 'otorrinolaringologo'
b = 'ringologootorrinola'
d = []
c = []

for x in a:  # ciclo para poner la cadena "a" en una lista
    d.append(x)
for f in b:  # ciclo para poner la cadena"b" en una lista
    c.append(f)
aux = 0
cont1 = 1
cont2 = 0
while cont1 < len(d):  # ordenar la lista d
    aux = d[cont1]
    while cont2 >= 0 and d[cont2] > aux:
        d[cont2+1] = d[cont2]
        d[cont2] = aux
        cont2 = cont2-1
    cont1 = cont1+1
    cont2 = cont1-1
aux = 0
cont1 = 1
cont2 = 0
while cont1 < len(c):  # ordena la lista c
    aux = c[cont1]
    while cont2 >= 0 and c[cont2] > aux:
        c[cont2 + 1] = c[cont2]
        c[cont2] = aux
        cont2 = cont2-1
    cont1 = cont1+1
    cont2 = cont1-1
#print d
#print c
if d == c:
    print 'son iguales'
else:
    print 'no son iguales'
