linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.sort()

print(linguagens)

linguagens.sort(reverse=True)

print(linguagens)

linguagens.sort(key=lambda x: len(x)) #ordenando de forma crescente "lambda é uma função anonima"

print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True) #ordenando de forma decrescente

print(linguagens)
