num1 = float(input('digita o primeiro numero: '))
num2 = float(input('digita o segundo numero: '))

operacao = input('digita a operacao desejada +, -, *, /: ')

if operacao == '+':
  print(num1 + num2)
elif operacao == '-':
  print(num1 - num2)
elif operacao == '*':
  print(num1 * num2)
elif operacao == '/':
  print(num1 / num2)
else:
  print('Operação invalida, coloque apenas as operações +, -, *, /')