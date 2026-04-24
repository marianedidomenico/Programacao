##calcule duas variações de peso com base em um valor inicial: um aumento de 15% (caso a pessoa engorde) e uma redução de 20% (caso ela emagreça)

peso = float(input("Peso: "))
opcao = input("Deseja ver cenário de [A]umento ou [R]edução? ").upper()

if opcao == 'A':
    print(f"Novo peso (+15%): {peso * 1.15:.2f}kg")
elif opcao == 'R':
    print(f"Novo peso (-20%): {peso * 0.8:.2f}kg")