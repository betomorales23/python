def fibonacci(tope):
    num1 = 0
    num2 = 1
    serie_fibo = 0
    lista = []
    while tope > serie_fibo:
        lista.append(serie_fibo)
        serie_fibo += num2
        num2 = num1
        num1 = serie_fibo
    return lista
   
inicio = int(input("Ingrese el tope de la secuencia fibonacci: "))
print(fibonacci(inicio))

