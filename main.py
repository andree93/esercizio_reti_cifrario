import string
ALFABETO_INGLESE = {}
MODULO = 26


def main():
    global ALFABETO_INGLESE
    ALFABETO_INGLESE = genera_alfabeto()
    chiave = int(input("Scegli chiave: "))
    parola = input("Inserisci parola da cifrare: ")
    parola_cifrata = cifra(ALFABETO_INGLESE, MODULO, chiave, parola)
    print("La parola cifrata è: " + parola_cifrata)


def genera_alfabeto():
    return {lettera:numero for numero, lettera in enumerate(list(string.ascii_uppercase))}



def genera_cifrario(alfabeto_inglese, modulo, chiave):
    alfabeto_inglese_cifrato = [ list(alfabeto_inglese.keys())[((indice_lettera + chiave) % modulo)] for indice_lettera in list(alfabeto_inglese.values()) ]
    dizionario_alfabeto_inglese_cifrato = {key: value for key, value in zip(list(alfabeto_inglese.keys()), alfabeto_inglese_cifrato)}
            
    return dizionario_alfabeto_inglese_cifrato



def cifra(alfabeto_inglese, modulo, chiave, parola ):
    dizionario_alfabeto_inglese_cifrato = genera_cifrario(alfabeto_inglese, modulo, chiave)
    parola_cifrata = [dizionario_alfabeto_inglese_cifrato[lettera.upper()] for lettera in parola.upper()]
    counter = 0
    str_parola_cifrata = "".join(parola_cifrata)
    for lettera in parola.upper():
        indice_c = (alfabeto_inglese[lettera] + chiave) % modulo
        stringa_messaggio = f"Lettera originale: {lettera} - Numero corrispondente: {alfabeto_inglese[lettera]} - Congruo: {indice_c} - Lettera corrispondente: {parola_cifrata[counter]} - ({alfabeto_inglese[lettera]} + {chiave} modulo {modulo})"
        print(stringa_messaggio)
        counter = counter+1
    return  str_parola_cifrata


if __name__ == "__main__":
    main()