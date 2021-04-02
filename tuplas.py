def sumaTiempo(tup1):
    sum = 0
    for i in range(len(tup1)):
        sum = sum + tup1[i]
    return sum

t1 = int(input("Ingrese el primer tiempo: "))
t2 = int(input("Ingrese el segundo tiempo: "))
d = t1,t2
lis = ["Humberto",38,1982]
lis = tuple(lis)
print(sumaTiempo(d))
print("Imprime:--> ",d.count(5))
print(type(d))
print(type(lis))


