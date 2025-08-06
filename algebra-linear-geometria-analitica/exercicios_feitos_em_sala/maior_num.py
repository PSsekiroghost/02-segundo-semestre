def maior(num1, num2):
    if num1 == num2:
        print("Os números têm o mesmo valor.")
    else:
        maior_num = max(num1, num2)
        print(f"O maior número é: {maior_num}")

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

maior(num1, num2)