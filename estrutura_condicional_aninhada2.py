aluno = input('Digite seu nome: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
frequencia = float(input('Digite sua frequencia: '))
medianota = (nota1 + nota2 + nota3)/3

if medianota >=6 and frequencia >=75:
    status = "aprovado"
elif medianota >= 6 or frequencia >= 75:
    status = "recuperação"
else:
    status = "reprovado"
    
print(f"O aluno {aluno} está {status}")        