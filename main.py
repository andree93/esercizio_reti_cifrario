def main():
    modulo = int(input("Scegli aritmetica modulare: "))
    chiave = int(input("Scegli chiave: "))
    parola = input("Inserisci parola da cifrare: ")
    print("Aspetta un momento...")
    parola_cifrata = cifra(alfabeto_inglese, modulo, chiave, parola)
    print("La parola cifrata è: " + parola_cifrata)


alfabeto_inglese = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15,
                       "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}


def genera_cifrario(alfabeto_inglese, modulo, chiave):
    alfabeto_inglese_cifrato = [ list(alfabeto_inglese.keys())[((indice_lettera + chiave) % modulo)] for indice_lettera in list(alfabeto_inglese.values()) ]
    dizionario_alfabeto_inglese_cifrato = {}
    if (len(alfabeto_inglese) == len(alfabeto_inglese_cifrato)):
        dizionario_alfabeto_inglese_cifrato = {key: value for key, value in zip(list(alfabeto_inglese.keys()), alfabeto_inglese_cifrato)}
    else:
        print("le liste hanno dimensioni differenti!") #test
            
    return dizionario_alfabeto_inglese_cifrato



def cifra(alfabeto_inglese, modulo, chiave, parola ):
    dizionario_alfabeto_inglese_cifrato = genera_cifrario(alfabeto_inglese, modulo, chiave)
    parola_cifrata = [dizionario_alfabeto_inglese_cifrato[lettera.upper()] for lettera in parola.upper()]
    counter = 0
    for lettera in parola.upper():
        indice_c = (alfabeto_inglese[lettera] + chiave) % modulo
        print("Lettera: "+lettera + " "+"Numero: "+ str(alfabeto_inglese[lettera]) + " " + "Congruo a: " + str( indice_c ) + " " +str() + "Lettera: "+ parola_cifrata[counter] + " " + "(" + str(alfabeto_inglese[lettera]) + "+" + str(chiave) + " modulo " + str(modulo) + ")")
        counter = counter+1
    str_parola_cifrata = "".join(parola_cifrata)
    return  str_parola_cifrata


if __name__ == "__main__":
    main()