import random

name = 'Fernanda'
question = 'Sere Millonaria?'
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
  answer = 'Pregunta luego'
elif random_number == 6:
  answer = 'Mejor no te lo digo ahora'
elif random_number == 7:
  answer = 'Mis fuentes dicen que no'
elif random_number == 8:
  answer = 'El panorama no se ve muy bueno'
elif random_number == 9:
  answer = 'Muy dificil'

print(name+' Pregunta: '+question)
print("Magic 8-Ball's responde: "+answer)
