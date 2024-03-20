def inizializza_file():
    f1 = open("dati.txt", "r")
    id = str(len(f1.readlines()))
    f1.close()
    if (id == "0"):
        contenuto = "id,nome,cognome,eta\n"
        f1 = open("dati.txt", "w")
        f1.write(contenuto)
        f1.close()
def inserisci_righe():
    f1 = open("dati.txt", "r")
    id = str(len(f1.readlines()))
    f1.close()
    nome = input("inserisci nome: ")
    cognome = input("inserisci cognome: ")
    eta = input("inserisci eta: ")
    f1 = open("dati.txt", "a")
    f1.write(id + "," + nome + "," + cognome + ","+ eta + "\n")
    f1.close()
def cerca_id():
    f1 = open("dati.txt", "r")
    id_linea = input("inserisci id da cercare: ")
    for linea in f1:
        if linea.startswith(id_linea):
            trovato = linea
            break
        else:
            trovato = "non trovato"
    print (trovato)
    f1.close()
#def modifica_nome():
def modifica_nome(id_linea, nuovo_nome):
    f1 = open("dati.txt", "r")
    lines = f1.readlines()
    f1.close()
    #id_linea = input("inserisci id: ")
    #nuovo_nome = input("inserisci il nuovo nome: ")
    for index, linea in enumerate(lines):
        if linea.startswith(id_linea):
            linea2 = linea.split(",")
            linea2[1] = nuovo_nome
            lines[index] = ",".join(linea2)
            file_a = open("dati.txt", "w")
            file_a.writelines(lines)
            file_a.close()
            break
#id_linea = input("inserisci id: ")
#nuovo_nome = input("inserisci il nuovo nome: ")
#modifica_nome(id_linea, nuovo_nome)
modifica_nome("1", "tom")