print(" Olá, esse programa calcula qual sua idade no ano desejado ")

anonascimento = int( input("Qual ano de seu nascimento ? "))
if anonascimento < 0:
    print(" Por favor, ninguém nasceu em ano negativo, insira uma data valida ")
    exit()
anodesejado = int( input("Qual ano deseja saber sua idade? "))



anofinal = anodesejado - anonascimento

print( "Em "+str(anodesejado)+" Voce tinha exatos "+str(anofinal)+" anos de idade")
