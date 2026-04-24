##duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira nota e peso 3 para a segunda nota.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = ((nota1 * 2) + (nota2 * 3)) / 5

print(f"A média ponderada é: {media:.2f}")