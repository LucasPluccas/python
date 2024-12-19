senha = input("Digite sua senha: ")
while senha != "lucas1210":
    print("Senha incorreta")
    senha = input("Digite sua senha: ")

print("Bem vindo ao sistema")


numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))
numero4 = int(input('Digite um número: '))
numero5 = int(input('Digite um número: '))

numeros = [numero1, numero2, numero3, numero4, numero5]

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")
        