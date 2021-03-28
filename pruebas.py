import requests

def validar_cripto(validar):
   criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
   if validar in criptos:
       return True
   else:
       return False

def validar_valor(cant1):
    if cant1 > 0:
        return True
    else:
        return False

cont = 0
acum = 0
tope = int(input("Cuantos registros va a ingresar: "))
while cont < tope:
    cripto = input("Ingrese la criptomoneda(BTC,BCC,LTC,ETH,ETC,XRP) #"+ str(cont+1)+": ")
    if validar_cripto(cripto):
        
        cant = float(input("Ingrese la cantidad que posee: "))
        url = 'https://api.binance.com/api/v3/ticker/price?symbol='+cripto+'USDT'
        res = requests.get(url)
        json = res.jason()
        valor = float(jason['price'])
        if validar_valor(cant):
            acum = acum + (cant * valor)
            cont += 1
        else:
            print("Ingrese los valores correctos!")
    else:
        print("Moneda incorrecta, ingrese nuevamente")

print("La cantidad en USD que posee es de: " + str(acum))

            






    

