nomes1 = ["ana", "gabriel"]
print(nomes1)
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