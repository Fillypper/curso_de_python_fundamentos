texto = input("Informe um text: ")
VOGAIS = "AEIOU"
opcao = -1

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

print()
print("Executa no final do laço")


for numero in range(0,51,5):
    print(numero, end=" ")

while opcao != 0:
    opcao = int(input("[1] para sacar \n[2]Extrato\n[0] Sair\n: "))

    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Exibindo o extrato...")