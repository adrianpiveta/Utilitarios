import csv
import openpyxl

from pandas._libs.algos import take_1d_bool_object

with open('dados_industriais_escrito.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["Pressao", "Temperatura", "Umidade"])
def ordena(nomes):
    for x in range(0, len(nomes), 1):
        anterior = nomes[x]
        j = x - 1
        nomes[-1] = anterior
        while(float(anterior[-1]) > float(nomes[j][-1])):
            nomes[j+1] = nomes[j]
            j -= 1
        nomes[j+1] = anterior
    return nomes

def to_csv(dados):
    wb = openpyxl.Workbook()
    wb.save('Classificacaop.xls')
    with open(, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nome', 'Nota'])
        for dado in dados:
            nome_escrita=""
            for nome in dado[0]:
                nome_escrita += nome + " "
            writer.writerow([nome_escrita, dado[-1]])


def resultadoAux():
    notas =[]
    nomes = []
    dict_nome={}
    arquivo_ordenacao = {}
    arquivo = open("prefeitura2.txt", encoding='utf-8')
    for linha in arquivo.readlines():
        linha = linha.split(' ')
        try:
            if(float(linha[-9]) >= 00.00):
                notas.append(linha[-9])
                nNome = [linha[1:len(linha)-9], float(linha[-9])]
                nomes.append(nNome)
                dict_nome[str(linha[1:len(linha)-9])] = linha[-9]
                json ={'nome': str(linha[1:len(linha)-9]),
                       'nota': float(linha[-9])}
                arquivo_ordenacao+=json
        except:
            pass
    #print(len(notas))
    to_csv(ordena(nomes))
    #print(dict_nome)



def resultado():
    erros = 0
    acertos = 0
    notas =[]
    registro =0
    nomes = []
    arquivo = open("prefeitura3.txt", encoding='utf-8')
    for linha in arquivo.readlines():
        linha = linha.split(' ')
        print(str(len(linha)-10))
        try:
            registro += 1
            if(float(linha[-11]) <= 99.00 and float(linha[-11]) >=10.00 ):
                notas.append(linha[-11])
                nNome = [[linha[1:(len(linha)-11)]], linha[-11]]
                nomes.append(nNome)

                acertos+=1
        except:
            erros+=1
    #print(erros)
    #print(acertos)
    print(len(notas))
    print(nomes)
    print('Qiantidade de registros ', registro)

resultadoAux()
