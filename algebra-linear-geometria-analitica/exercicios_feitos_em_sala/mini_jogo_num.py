from random import randint
num_random = randint(1, 50)

print('adivinha o numero de 1 a 50')

palpite = None
while palpite != num_random:
  try:
    tent_palpite = int(input('tente adivinha o numero: '))
    palpite = int(tent_palpite)

    if palpite == num_random:
      print('voce acertou o numero')
    elif palpite > num_random:
      print('tente um numero menor')
    else:
      print('tente um numero maior')
  except ValueError:
    print('numero invalido, coloque um numero inteiro')