def criar_carro(*, modelo, ano, placa, marca, motor, combustível):
    print(modelo, ano, placa, marca, motor, combustível)


criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustível="Gasolina")

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustível="Gasolina") #errado por não é apenas por keywords
