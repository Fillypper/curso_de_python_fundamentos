# .center = centraliza o texto dois argumentos (numero de espaços que vai ocupar, caractere que você quer colocar nesse espaço *opcional, caso não passe o segundo parametro ele fica com espaços)
#.join = passado o caractere em "" ex "."join(variavel iteravel)

nome = "Luiz Fillypper"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "         Olá mundo!           "
print(texto)

print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")


menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print(".".join(menu))