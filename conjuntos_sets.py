usuarios = {"Ana", "Maria"}
print(usuarios)
usuarios.add("Lucas")
print(usuarios)

usuario_digitado = input("Digite seu usuario: ")
if usuario_digitado in usuarios:
    print("Usuário cadastrado")
else:
    print("Usuário não cadastrado")
    
novos_usuarios = {"João", "Maria", "Marcos", "Patricia"}
print(f"Novos usuários cadastrados: {novos_usuarios}")

todos_usuarios = usuarios.union(novos_usuarios)
print(f"Todos os usuários cadastrados {todos_usuarios}")

usuarios_comuns = usuarios.intersection(novos_usuarios)
print(f"interseção: {usuarios_comuns}")
#Interseção é usado para saber os nomes em comum em mais de uma SET

conjunto_exemplo = {1, 2, 3, 4}
print(conjunto_exemplo)
conjunto_exemplo.add(5)
print(conjunto_exemplo)
conjunto_exemplo.remove(2)
conjunto_exemplo.discard(4)
print(conjunto_exemplo)