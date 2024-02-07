import domeniu
import prezentare

def valideaza_cheltuiala(cheltuiala):
    '''
    functie care verifica daca ziua cheltuielii este de la 1 la 31, suma este pozitiva si tipul este dintre cele corecte
    :preconditii cheltuiala: o cheltuiala
    :postconditii: -
    :raises: Exception cu mesajul:string
        "zi invalida!\n" daca zi<1 sau zi>31
        "suma invalida!\n" daca suma<=0
        "tip invalid!\n" daca tipul nu este printre "Altele","Mancare","Telefon","Intretinere","Apa"
    '''
    erori=""
    zi=domeniu.get_zi(cheltuiala)
    if zi<1 or zi>31:
        erori+="zi invalida!\n"
    if domeniu.get_suma(cheltuiala)<=0:
        erori+="suma invalida!\n"
    if domeniu.get_tip(cheltuiala) not in ["Altele","Mancare","Telefon","Intretinere","Apa"]:
        erori+="tip invalid!\n"
    if len(erori)>0:
        raise ValueError(erori)

def valideaza_poz(cheltuieli,index):

    if index<=len(cheltuieli):
        return index-1

def valideaza_params(params):
    erori=""
    zi_str = params[0].strip()
    suma_str = params[1].strip()
    tip = params[2].strip()
    try:
        zi=int(zi_str)
    except ValueError:
        erori += "zi invalida!\n"
    try:
        suma = float(suma_str)
    except ValueError:
        erori += "suma invalida!\n"
    if len(erori)>0:
        raise Exception(erori)
    else:
        if zi<1 or zi>31:
            erori+="zi invalida!\n"
        if suma<=0:
            erori+="suma invalida!\n"
        if tip not in ["Altele","Mancare","Telefon","Intretinere","Apa"]:
            erori+="tip invalid!\n"
        if len(erori)>0:
            raise Exception(erori)

def valid_int( var ,lim_inf, lim_sup,mesaj):
        '''
        se asigura ca un numar dat se afla intr un interval dorit
        :param mesaj: string
        :param lim_inf: int
        :param lim_sup: int
        :return: numar intreg
        '''
        while True:
            if var>=lim_inf and var<=lim_sup:
                return var
            else:
                print(mesaj)


def valid_tip(tip, mesaj):
    '''
    se asigura ca un numar dat se afla intr un interval dorit
    :param mesaj: string
    :param lim_inf: int
    :param lim_sup: int
    :return: numar intreg
    '''
    while True:
        if tip  not in ["Altele","Mancare","Telefon","Intretinere","Apa"]:
            print(mesaj)

        else:
            return tip

def valid_string(mesaj):
    '''
        citeste un tip de cheltuiala
        '''
    mesaj.strip()
    if len(mesaj!=0):
        return mesaj
    else:
        print(mesaj+"nu ati introdus caractere!\n")

def valideaza_int(nr,tip):
    if tip==0:
        if nr<0 or nr>6:
            raise ValueError("optiunea nu exista in meniu. incercati sa introduceti o valoare de la 0 la 6")
    elif tip==1 or tip==5:
        if nr<0 or nr>2:
            raise ValueError("suboptiunea nu exista in submeniu. incercati sa introduceti una din valorile 1 si 2")
    elif tip==2 or tip==3:
        if nr<0 or nr>3:
            raise ValueError("suboptiunea nu exista in submeniu. incercati sa introduceti o valoare de la 1 la 3")
    elif tip==4:
        if nr<0 or nr>4:
            raise ValueError("suboptiunea nu exista in submeniu. incercati sa introduceti o valoare de la 1 la 4")