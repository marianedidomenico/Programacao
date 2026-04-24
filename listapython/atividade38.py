##porcentagem sobre despesas

ano_nasc = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))

anos = ano_atual - ano_nasc
meses = anos * 12
semanas = anos * 52
dias = anos * 365

print(f"Idade em anos: {anos}")
print(f"Idade em meses: {meses}")
print(f"Idade em semanas: {semanas}")
print(f"Idade em dias: {dias}")

