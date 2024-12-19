nome = input('Digite seu nome :')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
if (media >= 7.0):
    passou = "sim" 
else:
    passou = "nao"

print( f"Com base em suas notas, você {passou} passou!")    
        