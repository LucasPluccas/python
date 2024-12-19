numero = int(input("Digite um número para a tabuada: "))
limite = int(input("Digite o limite máximo da tabuada: "))
contador = int(input("Digite o inicio da tabuada: "))
while contador <= limite:
    resultado = contador * numero
    print (f"{contador} x {numero} = {resultado}")
    contador += 1
    
    senha_correta = '123'
senha_digitada = ''

contador = 0
while senha_digitada != senha_correta:
    senha_digitada = input("Digite sua senha: ")
    if senha_digitada != senha_correta:
        contador += 1
        print (f"Tentativa {contador}, tente novamente!")
        

print ("Bem-vindo ao Sistema!")


opcao = ''
while opcao != '0':
    print ("1 - Nome do Aluno")
    print ("2 - Nota do Aluno")
    print ("3 - Situação do Aluno")
    print ("0 - Sair")
    opcao = input ("Digite uma opção: ")
    if opcao == '1':
        print ("Fernando Leonid")
        input ("digite enter para continuar...")
    elif opcao == '2':
        print ("7")
        input ("digite enter para continuar...")
    elif opcao  == '3':
        print ("Aprovado!")
        input ("digite enter para continuar...")
    elif opcao == '0':
        print ("Saindo do sistema...")
    else:
        print ("Opção errada, tente novamente!")
        
        nota = 9
preco = 4.5
nome_cliente = "Fernando Leonid"
pagou = True 

# array -> lista
produtos = ["teclado", "mouse", "monitor"]

contador = 0
while contador <= 2:
    print (produtos[contador])
    contador += 1