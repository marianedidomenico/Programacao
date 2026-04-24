##alário base e o volume de vendas, aplicando uma taxa de 4% de comissão
salario_fixo = float(input("Digite o salário fixo: R$ "))
vendas = float(input("Digite o valor das vendas: R$ "))

comissao = vendas * 0.04
salario_final = salario_fixo + comissao

print(f"Comissão: R$ {comissao:.2f}")
print(f"Salário Final: R$ {salario_final:.2f}")