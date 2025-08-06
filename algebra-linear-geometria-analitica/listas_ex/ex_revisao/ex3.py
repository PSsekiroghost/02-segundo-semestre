nota1 = float(input('digita a primeira nota: '))
nota2 = float(input('digita a segunda nota: '))
nota3 = float(input('digita a terceira nota: '))

media = nota1 + nota2 + nota3 / 3
print('A media do aluno é: ', media)

if media >= 7:
  print('Aluno Aprovado')
elif media >= 5 and media < 7:
  print("Aluno em Recuperação")
else:
  print('Aluno reprovado')