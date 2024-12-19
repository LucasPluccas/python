nome_aluno = input('Digite o nome do aluno: ')

nota_caso = int(input('Digite a nota do estudo de caso: '))
nota_portfolio = int(input ('Digite a nota do portfolio: '))

media_aluno = int((nota_caso + nota_portfolio)) / 2

if media_aluno >= 5:
    situacao = 'Aprovada'
else:
    situacao = 'Reprovada'

print(f"A aluna {nome_aluno} tem a média {media_aluno} e está {situacao}")


# Uma empresa quer calcular o salário de seus 
# funcionários com base em sua carga horária 
# semanal e o valor da hora de trabalho. 
# Além disso, a empresa oferece um bônus 
# de 10% para aqueles funcionários que 
# trabalharem mais de 40 horas por semana, 
# 20% para quem trabalhar mais de 100 horas
# e 30% para quem trabalha mais de 200 horas


carga_horaria = int(input('Digite sua carga horária: '))
valor_hora = float(input('Digite seu valor hora: '))

salario = carga_horaria * valor_hora

if carga_horaria > 200:
    salario = salario * 1.30
elif carga_horaria > 100:
    salario = salario * 1.20
elif carga_horaria > 40:
    salario = salario * 1.10

print (f'Seu salário é: {salario}')


# Um vendedor recebe uma comissão por suas vendas. 
# Dependendo do valor da venda, a comissão varia. 
# A comissão é calculada da seguinte forma:
# - 5% para vendas de até R$1.000,00
# - 7.5% para vendas entre R$1.000,01 e R$5.000,00
# - 10% para vendas entre R$5.000,01 e R$10.000,00
# - 15% para vendas acima de R$10.000,00
# Escreva um programa em Python que calcule a 
# comissão do vendedor, dado o valor da venda e o 
# nome do vendedor.

nomevendedor = input('Olá, vendedor. digite seu nome: ')
valorVenda = float(input((f'Olá, {nomevendedor}. Para calcular o valor de sua comissão, digite aqui o valor do produto: ')))

if valorVenda <= 1000.00:
    comissao = valorVenda * 0.05
elif valorVenda <= 5000.00:
    comissao = valorVenda * 0.075
elif valorVenda <= 10000.00:
    comissao = valorVenda * 0.10
else:
    comissao = valorVenda * 0.15


print (f"{nomevendedor}, sua venda no valor de R${valorVenda} terá uma comissão de R${comissao}")