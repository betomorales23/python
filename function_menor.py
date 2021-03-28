# calculando el numero menor

def num_menor(a,b,c):
    if a > b and c > b:
        menor = b
    elif b > a and c > a:
        menor = a
    elif a > c and b > c:
        menor = c
    return menor

print("El menor es: " + str(num_menor(10,5,8)))
