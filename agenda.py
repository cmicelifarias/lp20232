'''
Agenda de ECA

Na nossa agenda podemos:

i - inserir
r - remover
e - editar
s - sair

se na vc ofende alguem

'''



def inserir():
    a = input("Digite um nome: ")
    b = input ("Digite um telefone: ")
    global agenda
    #agenda_tel[a] = b
    global arquivo
    print(a+"-"+b)
    arquivo.write(a+"-"+b)

def editar():
    c = input("Qual registro vc quer editar: ")
    global agenda_tel
    '''
    if agenda_tel.get(c):
        print ("Registro encontrado")
        o = input("Digite o novo telefone")
        agenda_tel[c] = o
    else: print("Registro nao existe")
    '''
    arquivo.seek(c)
    linha = arquivo.readline()
    print(linha)

def remover():
    r = input ("Qual registro vc quer remover?")
    global agenda_tel

    if agenda_tel.get(r):
        agenda_tel.pop(r)
    else: print("Registro nao existe")

def sair():
    global saida 
    global arquivo
    saida = False
    arquivo.close()
    print("Ateh logo!")
    #break

saida = True
agenda_tel = {}
arquivo = open("arquivo.txt", "a")

while(saida):

    b = input("Diga o que vc quer fazer: ")
    if (b == "i"):
        inserir()
    elif (b == "e"):
        editar()
    elif (b == "r"):
        remover()
    elif (b == "s"): 
        sair()
    else: 
        print("Sabe escrever nao?")
    

