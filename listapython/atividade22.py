moeda1cent = int(input("Quantidade de moedas de 1 centavo: "))
moeda5cent = int(input("Quantidade de moedas de 5 centavos: "))
moeda10cent = int(input("Quantidade de moedas de 10 centavos: "))
moeda25cent = int(input("Quantidade de moedas de 25 centavos: "))
moeda50cent = int(input("Quantidade de moedas de 50 centavos: "))
moeda1real = int(input("Quantidade de moedas de 1 real: "))

total = (moeda1cent * 0.01) + (moeda5cent * 0.05) + (moeda10cent * 0.10) + (moeda25cent * 0.25) + (moeda50cent * 0.50) + (moeda1real * 1.00)

print ("O valor total de moedas é: ",total)