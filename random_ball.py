import random

continuar = 'S'
name = input("Ingrese su nombre: ")
while continuar == 'S' or continuar == 's':

  question = input('Ingrese su pregunta: ')
  answer = ''
  random_number = random.randint(1,9)
  if random_number == 1:
    answer = 'Si - Definitivamente'
  elif random_number == 2:
    answer = 'Esta decidido!'
  elif random_number == 3:
    answer = 'Sin duda alguna'
  elif random_number == 4:
    answer = 'Intenta de nuevo mi amigo'
  elif random_number == 5:
    answer = 'Mejor no respondo'
  elif random_number == 6:
    answer = 'En tus sueños'
  elif random_number == 7:
    answer = 'Mis fuentes dicen que no'
  elif random_number == 8:
    answer = 'El panorama no se ve muy bueno'
  elif random_number == 9:
    answer = 'Está Jodido'
  print(name+' Pregunta: '+question)
  print("Magic 8-Ball's responde: "+answer)
  print("")
  continuar = input("Si desea continuar, presione 'S' o 's', caso contrario N para salir: ")

