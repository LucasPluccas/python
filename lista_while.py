nomes1 = ["Ana", "Gabriel"]
print(nomes1)

#Cadastrando nomes na lista usando o WHILE como estrutura de repetição
resp = "s"
while resp == "s":
    novo_nome2 = input("Digite um novo nome: ")
    nomes1.append(novo_nome2)
    resp = input("Deseja cadastrar um novo nome? [s/n]: ")
print(nomes1)

print(nomes1 [2])

#Pesquisando se um nome já consta na lista

nome_pesquisado = input("Digite um nome para pesquisar: ")
if nome_pesquisado in nomes1:
    print("Nome cadastrado")
else:
    print("Nome não consta na lista")
