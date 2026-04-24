##porcentagem sobre despesas
salario = 1200.00
c1 = 200.00
c2 = 120.00

# Cálculo com multa de 2%
total_contas = (c1 * 1.02) + (c2 * 1.02)
restante = salario - total_contas

print(f"Total das contas com multa: R$ {total_contas}")
print(f"Restará do salário do João: R$ {restante}")
