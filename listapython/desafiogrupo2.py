##2. O Desafio da Escada (Saúde) Contexto: Um atleta quer subir 10 lances de escada e contar em voz alta a cada lance completado para manter o ritmo.
## fazer um codigo que conte ate 10 e em casa numero meça os btm para manter o ritmo e analisar a média depois.

##Inicio da soma dos batimentos. 
soma_batimentos = 0

for i in range(1, 11): ##Falar sobre cada lance, repetindo até o lance 10##
    batimento = int(input(f"Você está no {i}º lance! Insira seus batimentos: "))
    soma_batimentos += batimento ##somando os batimentos adicionados a cada lance##

media = soma_batimentos / 10 ##media de btms

print("A média dos seus batimentos cárdiacos durante o seu exercício foi: ",media)  ##informar o a media de batimentos 

##informar se a média de batimentos esta boa##
if media >=175:
    print("Seus batimentos cardíacos estão a cima do esperado! Você deve ir ao cardiologista.")
elif media <=80:
    print("Seus batimentos estão abaixo do esperado! Você está com incompetência cardíaca. Consulte um cardiologista!")
else: media >140 and media <170
print ("A sua média de batimentos está boa! Você está saúdavel.")