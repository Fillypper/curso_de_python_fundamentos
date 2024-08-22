contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

resultado = contatos.setdefault("nome", "Giovanna")

print(resultado)

contatos.setdefault("idade", 28)

print(contatos)