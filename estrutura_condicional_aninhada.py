anos_experiencia = int(input('Digite quantos anos de expêriencia você tem: '))

if anos_experiencia == 0:
    nivel = "Estagiário"
    #elif é else if como se fosse SENÃO SE:
elif anos_experiencia <= 3:
    nivel = "Júnior"
elif anos_experiencia > 3 <= 5:
    nivel = "Pleno" 
elif anos_experiencia >= 8:
    nivel = "Senior"    

print(f"Com base em seu tempo de experiência, vocé é um desenvolvedor {nivel}")
    
           