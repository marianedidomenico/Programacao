dias_trabalhados = int (input("Insira a quantidade de dias sem acidentes: "))
anos = dias_trabalhados //365
meses= (dias_trabalhados % 365) // 30
dias = (dias_trabalhados % 365) % 30

print (f"Estamos a ",acidente,"dias,",mes,"meses e ",ano,"anos sem acidentes")