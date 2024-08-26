def salvar_carro(ano, modelox, marca, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelox}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelox="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca":"Fiat", "modelox": "Palio", "ano": 1999, "placa": "ABC-1234"})