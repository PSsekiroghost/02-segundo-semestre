idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Adulto")
elif idade >= 14:
    print("Juvenil")
elif idade >= 9:
    print("Infantil")
elif idade >= 0:  
    print("Mirim")
else:
    print("Idade inválida")  
