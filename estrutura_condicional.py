#Programa para calcular pagamento de hora extra e bonus de funcionários.
horas_trabalhadas = float(input('Digite a quantidade de horas: '))
valor_hora = float(input('Digite o valor/hora: '))

if (horas_trabalhadas >= 100):
    bonus = 500.00
else:
    bonus = 0
        
salario = horas_trabalhadas*valor_hora+bonus
#2 jeitos de printar um valor numerico em uma frase como string
print ('Seu sálario é de : '+ str(salario))
print (f"Seu sálario é de {salario}")   