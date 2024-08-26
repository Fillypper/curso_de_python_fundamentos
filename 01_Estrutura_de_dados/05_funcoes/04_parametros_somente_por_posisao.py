# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       ----------     ----------     ----------
#           |           |                   |
#           |     Positional or keyword /   |
#           |                               - Keyword only *
#           -- Positional only

def criar_carro(modelo, ano, placa, /, marca, motor, combustível):
    print(modelo, ano, placa, marca, motor, combustível)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustível="Gasolina")

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustível="Gasolina") #errado por que não é apenas por posições(valores)
