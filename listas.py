nomes = []
#Para criar listas basta abrir [] colchetes.
nomes1 = ["ana", "gabriel"]
#para colocar mais de um valor, separe por virgula.
print(f"lista original: {nomes1}")

nomes1.append ("Pedro")
#para adicionar pode-se usar o variavel.append ou ainda excluir e copiar por exemplo
print(f"lista adicionando nomes: {nomes1}")
#Pode-se usar um input para colher o novo nome do usuario e já acrescentando na lista
novo_nome = input("Digite um novo nome: ")
nomes1.append(novo_nome)
print(f"lista com nome adicionado pelo input: {nomes1}")

#Adicionar mais de um nome usando FOR como estrutura de repetição
for cont in range(3):
    novo_nome2 = input("Digite um novo nome: ")
    nomes1.append(novo_nome2)

print(f"lista de nomes adicionados usando o FOR como estrutura de repetição: {nomes1}")

#Adicionar mais de um nome usando FOR como estrutura de repetição com alguns detalhes nos parametros
for cont in range(1,4):#contador será do 1 até o 3
    novo_nome2 = input(f"Digite um novo nome{cont}: ")
    nomes1.append(novo_nome2)

print(f"lista de nomes adicionados usando o FOR como estrutura de repetição: {nomes1}")

#Cadastrando nomes na lista usando o WHILE como estrutura de repetição
resp = "sim"
while resp == "s":
    novo_nome3 = input("Digite um novo nome: ")
    nomes1.append(novo_nome3)
    resp = input("Deseja cadastrar um novo nome? [s/n]: ")

print(nomes1)
