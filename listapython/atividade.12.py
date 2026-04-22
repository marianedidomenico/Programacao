salario = float(input("Insira seu salário:"))
aumento = salario * 0.15
salario_aumento = salario + aumento
imposto = salario_aumento * 0.08
salario_final = salario_aumento - imposto
print ("Seu salário bruto é: ",salario)
print ("Seu salário com aumento é: ",salario_aumento)
print ("Seu salário líquido é: ",salario_final)