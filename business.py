import business
import domeniu
import validare
import infrastructura

def creeaza_cheltuiala_si_adauga_la_buget(buget,zi,suma,tip):
    cheltuiala=domeniu.creeaza_cheltuiala(zi,suma,tip)
    validare.valideaza_cheltuiala(cheltuiala)
    buget=infrastructura.adauga_cheltuiala_la_buget(buget,cheltuiala)
    return buget

def modificare_intre_cheltuieli(cheltuiala1,cheltuiala2):
    """
    functie care modifica suma si tipul din cheltuiala1 cu suma si tipul din cheltuaiala 2
    :param cheltuiala1: lista
    :param cheltuiala2: lista
    """
    cheltuiala1=[]
    zi=domeniu.get_zi(cheltuiala2)
    suma=domeniu.get_suma(cheltuiala2)
    tip= domeniu.get_tip(cheltuiala2)
    cheltuiala=domeniu.creeaza_cheltuiala(zi,suma,tip)
    cheltuiala1=cheltuiala[:]
    return cheltuiala1

def stergere_dupa_zi(cheltuieli,zi):
    '''
        Sterge toate cheltuielile pentru o zi data
        :param cheltuieli: lista
        :param zi: int
        :return: lista
        '''
    ok = 0
    for i in range(0, len(cheltuieli)):
        if ok == 1:
            i -= 1
        if domeniu.get_zi(cheltuieli[i]) == zi:
            cheltuieli.pop(i)
            ok = 1
    return cheltuieli

def stergere_dupa_timp(cheltuieli,zi1,zi2):
    '''
        Sterge toate cheltuielile pentru un interval de timp dat, descris intre ziua 1 si ziua 2
        :param cheltuieli: lista
        :param zi1: int
        :param zi2: int
        :return: lista dorita
        '''
    ok = 0
    for i in range(0, len(cheltuieli)):
        if ok == 1:
            i -= 1
        if domeniu.get_zi(cheltuieli[i]) >= zi1 and domeniu.get_zi(cheltuieli[i]) <= zi2:
            cheltuieli.pop(i)
            ok = 1
    return cheltuieli

def stergere_dupa_tip(cheltuieli,tip):
    '''
        Sterge toate cheltuielile pentru un tip dat
        :param cheltuieli: lista
        :param tip: string
        :return: lista dorita
        '''
    ok = 0
    for i in range(0, len(cheltuieli)):
        if ok == 1:
            i -= 1
        if domeniu.get_tip(cheltuieli[i]) == tip:
            cheltuieli.pop(i)
            ok = 1
    return cheltuieli

def cautare_suma(cheltuieli,suma):
    '''
                elimina toate elementele din lista care sunt mai mici sau egale cu o suma data
                :param cheltuieli: lista
                :param suma: float
                :return: o lista
                '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_suma(cheltuieli[i]) > suma:
            chelt.append(cheltuieli[i])
    return chelt

def cautare_zi_suma(cheltuieli,zi,suma):
    '''
                   elimina toate elementele din lista care sunt mai mici decat o suma data si efectuate inainte de o zi data
                   :param cheltuieli: lista
                   :param zi: int
                   :param zi: float
                   :return: o lista
                   '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_zi(cheltuieli[i]) < zi and domeniu.get_suma(cheltuieli[i]) > suma:
            chelt.append(cheltuieli[i])
    return chelt

def cautare_tip(cheltuieli,tip):
    '''
            gaseste cheltuielile care sunt de un anumit tip
            :param cheltuieli: lista
            :param tip: tip
            :return: lista dorita
            '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_tip(cheltuieli[i]) == tip:
            chelt.append(cheltuieli[i])
    return chelt

def rapoarte_tot_tip(cheltuieli,tip):
    '''
        tipareste suma totala de un anumit tip din cheltuieli
        :param cheltuieli: lista
        :param tip: tip
        :return: suma totala, tipaqrita
        '''
    sumtot = 0.0
    for i in range(0, len(cheltuieli)):
        if domeniu.get_tip(cheltuieli[i]) == tip:
            sumtot += cheltuieli[i][1]
    return sumtot

def smax(cheltuieli):
    '''
        tipareste suma totala de un anumit tip din cheltuieli
        :param cheltuieli: lista
        :param tip: tip
        :return: suma totala, tipaqrita
        '''
    ls=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sumtot = 0.0
    for i in range(0, len(cheltuieli)):
        ls[domeniu.get_zi(cheltuieli[i])-1]=ls[domeniu.get_zi(cheltuieli[i])-1]+domeniu.get_suma(cheltuieli[i])
        if ls[domeniu.get_zi(cheltuieli[i])-1]>sumtot:
            sumtot=ls[domeniu.get_zi(cheltuieli[i])-1]
            sm=domeniu.get_zi(cheltuieli[i])
    return sm

def raport_suma(cheltuieli,suma):
    '''
                    elimina toate elementele din lista care sunt mai mici sau egale cu o suma data
                    :param cheltuieli: lista
                    :param suma: float
                    :return: o lista
                    '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_suma(cheltuieli[i]) == suma:
            chelt.append(cheltuieli[i])
    return chelt

def sorteaza_tip(cheltuieli):
    cheltuieli1=cautare_tip(cheltuieli,"Altele")
    cheltuieli4=cautare_tip(cheltuieli,"Mancare")
    cheltuieli5 = cautare_tip(cheltuieli, "Telefon")
    cheltuieli3 = cautare_tip(cheltuieli, "Intretinere")
    cheltuieli2 = cautare_tip(cheltuieli, "Apa")
    chelt=infrastructura.concateneaza_sortate(cheltuieli1,cheltuieli2,cheltuieli3,cheltuieli4,cheltuieli5)
    return chelt

def filtrare_tip(cheltuieli,tip):
    '''
            elimina toate elementele din lista care sunt de un anumit tip
            :param cheltuieli: lista
            :param tip: string
            :return: o noua lista, modificata
            '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_tip(cheltuieli[i]) != tip:
            chelt.append(cheltuieli[i])
    return chelt

def filtrare_suma(cheltuieli,suma):
    '''
            elimina toate elementele din lista care sunt mai mici decat o suma data
            :param cheltuieli: lista
            :param suma: float
            :return: o lista, tiparita
            '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_suma(cheltuieli[i]) >= suma:
            chelt.append(cheltuieli[i])
    return chelt

def undo(history):
    history.pop(len(history) - 1)
    if history == []:
        print("bugetul nu continea cheltuieli inainte de efectuarea ultimei operatii\n")
        cheltuieli = []
    else:
        cheltuieli = history[len(history) - 1]
    return cheltuieli

def printeaza_elem_bugetului(buget):
    if buget==[]:
        print("nu exista elemente la buget")
    else:
        for cheltuieli in buget:
            print(domeniu.get_zi(cheltuieli)," ",domeniu.get_suma(cheltuieli)," ",domeniu.get_tip(cheltuieli))
    print('\n')