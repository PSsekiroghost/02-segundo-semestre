agenda = {} 

def adicionar_telefone():
  nome = input('digite o seu nome: ')
  telefone = input('digita o seu telefone: ')
  if telefone in agenda.values(): 
    print('telefone ja cadastrado!')
  else:
    agenda[telefone] = nome 
    print('telefone cadastrado com sucesso')

def remover_telefone():
  telefone = input('digita o telefone que deseja remover: ')
  if telefone in agenda:
    del agenda[telefone]
    print('telefone removido com sucesso')
  else:
    print('telefone não encontrado')

def verificar_telefone(
    
):
  telefone = input('digita o telefone que deseja verificar: ')
  if telefone in agenda:
    print(f'telefone encontrado: {agenda[telefone]} - {telefone}')
  else:
    print('telefone não encontrado')

def mostrar_agenda():
  print('agenda de contatos: ')
  if not agenda:
    print('agenda vazia')
  else:
    for nome, telefone in agenda.items():
      print(f'{nome} - {telefone}')

while True:
  print('Digita qual opção voce deseja: ')
  print('1. Adicionar telefone') 
  print('2. Remover telefone')
  print('3. Verificar telefone')
  print('4. Mostrar agenda')
  print('5. Sair')
  opcao = input('Escolha uma das opções: ')

  if opcao == '1':
    adicionar_telefone()
  elif opcao == '2':
    remover_telefone()
  elif opcao == '3':
    verificar_telefone()
  elif opcao == '4':
    mostrar_agenda()
  elif opcao == '5':
    print('Saindo do programa...')
    break
  else:
    print('Opção invalida, tente novamente!')