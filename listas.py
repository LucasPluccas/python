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

