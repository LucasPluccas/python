cliente = {"nome": "lucas", "cidade": "Taboão da Serra", "ano_nasc": 1993, 
"ativo": False}
print(cliente)
print(cliente["nome"])
del cliente["ano_nasc"]
print(cliente)

if "ano_nasc" in cliente:
    print(f"O cliente nasceu em: {cliente['ano_nasc']}")
else:
    print("Não existe a chave ano_nac")

print("Lista de valores: ")
for valor in cliente.values():
    print(valor)
print("Lista de chaves: ")
for chave in cliente.items():
    print(chave)
