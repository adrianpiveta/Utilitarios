file = open("concurso.txt")
alternativas = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0}
acertos = 0

for valor in range(0,50):
    linha = file.readline()
    errado = True
    for alternativa in alternativas:
        if(linha[0] == alternativa):
            alternativas[alternativa] = alternativas[alternativa] + 1
        
    if linha[0] == linha[1]:
        errado = False
        acertos +=1
    if errado:
        print("ERREI a questão: ", (valor+1), ' era ', linha[0], ' e coloquei ', linha[1])
    
print("total de acertos: ", acertos)
print(alternativas)
