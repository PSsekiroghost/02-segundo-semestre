def primo(num):
  num = int(num) 
  if num < 2:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

num = input('digita um numero: ')
if primo(num):
  print('é um numero primo')
else:
  print('não é um numero primo')