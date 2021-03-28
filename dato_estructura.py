#ejemplos de estructura de datos en listas

#creamos lista
cripto = []
cant = []
cot = []
i = 0
endpoint = int(input("Ingrese cuantos registros desea ingresar: "))
while i < endpoint:
    cripto.append(input("Ingrese el nombre de la criptomoneda: "))
    cant.append(int(input("Ingrese la cantidad que posee: ")))
    cot.append(float(input("Ingrese el valor de mercado de la moneda: ")))
    i += 1
i = 0
while i < endpoint:
    print("Criptomoneda: "+cripto[i]+" Cantidad: "+str(cant[i])+" Valor: "+str(cot[i]))
    i += 1

print(cripto[::-1])


