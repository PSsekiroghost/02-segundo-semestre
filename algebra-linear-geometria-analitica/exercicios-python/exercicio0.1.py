nome = input('Insirar o seu nome: ')
print('Seja Bem-Vindo ao menu ', nome)
print('\n')

while True:
  print('Digita qual opção voce deseja: \n 1. Verificar se é par ou impar \n 2. Calcular a media\n 3. Sair\n')

  opcao = input('Digita o numero da opção desejada: ')
  if opcao == '1':
    num1 = int(input('Insira um numero: '))
    if num1 % 2 == 0:
      print('o numero é par')
      print('\n')
    else:
      print('o numero é impar')
      print('\n')

  elif opcao == '2':
    nota1 = float(input('Insira a nota 1: '))
    nota2 = float(input('Insira a nota 2: '))
    nota3 = float(input('Insira a nota 3: '))

    media = (nota1 + nota2 + nota3) / 3
    print('A media das notas são: ', media)
    print('\n')

  elif opcao == '3':
    print('Voce saiu do programa, espero que tenha gostado')
    break
  
  else:
    print('ocorreu algum poblema, tente novamente!')