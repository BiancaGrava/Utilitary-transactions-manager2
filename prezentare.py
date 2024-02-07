import business
import domeniu
import infrastructura
import validare

def read_intreg(mesaj):
    '''
    se asigura ca numarul  citit este intreg
    :param mesaj: string
    :return: numar intreg
    '''
    while True:
        try:
            return int(input(mesaj))
        except ValueError:
            print("introduceti un numar intreg")


def gaseste_sol(tip,mesaj):
    '''
    citeste un numar v=intreg si valid dpdv logic
    :param tip: cheie pentru validare
    :param mesaj: string, prompt
    :return: intreg valid
    '''
    while True:
        nr=read_intreg(mesaj)
        try:
            validare.valideaza_int(nr,tip)
            return nr
        except ValueError:
            print("suboptiunea nu se afla in submeniu. va rugam sa introduceti o suboptiune valida!")

def read_float(mesaj):
    '''
    se asigura ca numarul  citit este intreg
    :param mesaj: string
    :return: numar intreg
    '''
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("introduceti un numar rational")

def read_tip(mesaj):
    '''
        se asigura ca un numar dat se afla intr un interval dorit
        :param mesaj: string
        :param lim_inf: int
        :param lim_sup: int
        :return: numar intreg
        '''
    while True:
        tip=input(mesaj)
        if tip not in ["Altele", "Mancare", "Telefon", "Intretinere", "Apa"]:
            print("tip invalid. introduceti un tip valid!")
        else:
            return tip

def citire_index_valid(cheltuieli):
    '''
    citeste un index valid din buget
    :param cheltuieli: buget
    :return: index valid=int
    '''
    while True:
        try:
            t=read_intreg("introduceti indexul cheltuielii spre modificare: ")
            s=domeniu.get_suma(cheltuieli[t])
            return t
        except IndexError:
            print("index invalid!\n")


def ui_adauga_cheltuiala(buget,params):
    zi=int(params[0].strip())
    suma = float(params[1].strip())
    tip = params[2].strip()
    buget=business.creeaza_cheltuiala_si_adauga_la_buget(buget,zi,suma,tip)
    return buget

def adaugare(cheltuieli):
    while True:
        try:
            params = citire_parametrii_valizi()
            cheltuieli = ui_adauga_cheltuiala(cheltuieli, params)
            return cheltuieli
        except ValueError:
            print("cheltuiala exista deja!\n")


def ui_adauga_modifica_cheltuiala(index,cheltuieli,cheltuiala1):
   '''
   aceasta functie modifica cheltuiala daca aceasta exista in lista
    :param evidenta: lista
    :param index: int
    '''
   cheltuieli[index]=business.modificare_intre_cheltuieli(cheltuieli[index],cheltuiala1)
   chelt=cheltuieli[:]
   return chelt


def citire_parametrii_valizi():
    while True:
        t = input("introduceti ziua, suma si tipul cheltuielii in aceasta ordine: ")
        t = t.strip()
        params = t.split(" ")
        try:
            validare.valideaza_params(params)
            return params
        except Exception:
            print("Instructiune necunoscuta. Introduceti un intreg, un float si un string pentru zi, suma si tip!")

#def meniu_adaugari(cheltuieli,history):



#def meniu_stergere(cheltuieli):


#def meniu_cautare(cheltuieli):


#def meniu_rapoarte(cheltuieli):


#def meniu_filtrare(cheltuieli):


def interfata():

    '''
    interfata cu utilizatorul
    '''

    cheltuieli=[]
    history=[]
    while True:
        ui=gaseste_sol(0,"Introduceti optiunea dorita din variantele:\n"
                         "0. Iesire din program\n"
                         "1. Adauga cheltuiala\n"
                         "2. Stergere\n"
                         "3. Cautari\n"
                         "4. Rapoarte\n"
                         "5. Filtrare\n"
                         "6. Undo\n")
        #cnd=cnd.strip()
        #parts=cnd.split(" ")
        #print (parts)
        #ui=int(parts[0])
        #params=parts[2:]

        if ui==1:
            while True:
                s = gaseste_sol(1, "introduceti o suboptiune din submeniul ADAUGARE:\n"
                                   "0. INTOARCERE LA MENIU\n"
                                   "1. Adauga cheltuiala\n"
                                   "2. Actualizeaza cheltuiala\n")
                # validare.valideaza_int(s,1)
                if s == 1:
                    cheltuieli = adaugare(cheltuieli)
                    business.printeaza_elem_bugetului(cheltuieli)
                    history.append(cheltuieli[:])
                elif s == 2:
                    business.printeaza_elem_bugetului(cheltuieli)
                    if cheltuieli == []:
                        print("va rugam sa introduceti elemente in lista inainte de a incerca sa le modificati!")
                    else:
                        index = citire_index_valid(cheltuieli)
                        params = citire_parametrii_valizi()
                        cheltuieli = ui_adauga_modifica_cheltuiala(index, cheltuieli, params)
                        history.append(cheltuieli[:])
                        business.printeaza_elem_bugetului(cheltuieli)
                elif s == 0:
                    break

        elif ui==2:
            while True:
                s = gaseste_sol(2, "introduceti o suboptiune din submeniul STERGERE:\n"
                                   "0. INTOARCERE LA MENIU\n"
                                   "1. Sterge cheltuialile pentru ziua data\n"
                                   "2. Sterge cheltuialile pentru intervalul de timp dat\n"
                                   "3. Sterge cheltuialile pentru un tip dat\n")
                # validare.valideaza_int(s,2)
                if cheltuieli == []:
                    print("lista este goala. va rugam introduceti elemente in lista pentru a le putea sterge!\n")
                    break
                else:
                    if s == 1:
                        business.printeaza_elem_bugetului(cheltuieli)
                        zi = read_intreg("introduceti ziua pentru stergere: ")
                        validare.valid_int(zi, 1, 31, "dati o zi a lunii. adica un numar de la 1 la 31: ")
                        cheltuieli = business.stergere_dupa_zi(cheltuieli, zi)
                        business.printeaza_elem_bugetului(cheltuieli)
                        history.append(cheltuieli[:])
                    elif s == 2:
                        business.printeaza_elem_bugetului(cheltuieli)
                        zi1 = read_intreg("introduceti ziua de inceput pentru stergere: ")
                        zi2 = read_intreg("introduceti ziua de final pentru stergere: ")
                        cheltuieli = business.stergere_dupa_timp(cheltuieli, zi1, zi2)
                        business.printeaza_elem_bugetului(cheltuieli)
                        history.append(cheltuieli[:])
                    elif s == 3:
                        business.printeaza_elem_bugetului(cheltuieli)
                        tip = read_tip("introduceti tipul pentru stergere: ")
                        cheltuieli = business.stergere_dupa_tip(cheltuieli, tip)
                        business.printeaza_elem_bugetului(cheltuieli)
                        history.append(cheltuieli[:])
                    elif s == 0:
                        break
        elif ui==3:
            while True:
                s = gaseste_sol(3, "introduceti o suboptiune din submeniul CAUTARI:\n"
                                   "0. INTOARCERE LA MENIU\n"
                                   "1. Tipareste toate cheltuielile mai mari decat o suma data\n"
                                   "2. Tipareste toate cheltuielile efectuate inainte de o zi si mai mari decat o suma data\n"
                                   "3. Tipareste toate cheltuielile de un anumit tip\n")
                # validare.valideaza_int(s,3)
                if cheltuieli == []:
                    print("lista este goala. va rugam introduceti elemente in lista pentru a le putea cauta!\n")
                    break
                else:
                    # chelt=[]
                    if s == 1:
                        suma = read_intreg("introduceti suma pentru cautare: ")
                        chelt = business.cautare_suma(cheltuieli, suma)
                        business.printeaza_elem_bugetului(chelt)

                    elif s == 2:
                        zi = read_intreg("introduceti ziua pentru cautare: ")
                        suma = read_intreg("introduceti suma pentru cautare: ")
                        chelt = business.cautare_zi_suma(cheltuieli, zi, suma)
                        business.printeaza_elem_bugetului(chelt)

                    elif s == 3:
                        tip = read_tip("introduceti tipul pentru stergere: ")
                        validare.valid_tip(tip, "introduceti un tip valid!\n")
                        chelt = business.cautare_tip(cheltuieli, tip)
                        business.printeaza_elem_bugetului(chelt)
                    elif s == 0:
                        break
        elif ui==4:
            while True:
                s = gaseste_sol(4, "introduceti o suboptiune din submeniul RAPOARTE:\n"
                                   "0. INTOARCERE LA MENIU\n"
                                   "1. Tipareste suma totala pentru un tip de cheltuiala\n"
                                   "2. Gaseste ziua in care suma cheltuita e maxima\n"
                                   "3. Tipareste toate cheltuielile ce au o anumita suma\n"
                                   "4. Tipareste toate cheltuielile sortate dupa tip\n")
                # s=validare.valideaza_int(s,4)
                if cheltuieli == []:
                    print("lista este goala. va rugam introduceti elemente in lista pentru a putea efectua rapoarte!\n")
                    break
                else:
                    # chelt=[]
                    if s == 1:
                        tip = read_tip("introduceti tipul pentru raport: ")
                        validare.valid_tip(tip, "introduceti un tip valid!\n")
                        suma = business.rapoarte_tot_tip(cheltuieli, tip)
                        print("suma ceruta este: ", suma,"\n")
                    elif s == 2:
                        zi = business.smax(cheltuieli)
                        print("ziua in care suma cheltuita e maxima este: ", zi)
                    elif s == 3:
                        suma = read_float("introduceti suma pentru tiparit: ")
                        chelt = business.raport_suma(cheltuieli, suma)
                        business.printeaza_elem_bugetului(chelt)
                    elif s == 4:
                        chelt=business.sorteaza_tip(cheltuieli)
                        business.printeaza_elem_bugetului(chelt)
                    elif s == 0:
                        break
        elif ui==5:
            while True:
                s = gaseste_sol(5, "introduceti o suboptiune din submeniul FILTRARE:\n"
                                   "0. INTOARCERE LA MENIU\n"
                                   "1.Elimina toate cheltuielile de un anumit tip\n"
                                   "2. Elimina toate cheltuielile mai mici decat o suma data\n")
                if cheltuieli == []:
                    print("lista este goala. va rugam introduceti elemente in lista pentru a putea efectua filtrari!\n")
                    break
                else:
                    if s == 1:
                        tip = read_tip("introduceti un tip pentru filtrare: ")
                        chelt = business.filtrare_tip(cheltuieli, tip)
                        business.printeaza_elem_bugetului(chelt)
                    elif s == 2:
                        suma = read_float("introduceti o suma pentru filtrare: ")
                        chelt = business.filtrare_suma(cheltuieli, suma)
                        business.printeaza_elem_bugetului(chelt)
                    elif s == 0:
                        break
        elif ui==6:
            if history == []:
                print("nu ati efectuat operatii asupra bugetului. nu putem efectua UNDO\n")
                #break
            else:
                cheltuieli=business.undo(history)
                business.printeaza_elem_bugetului(cheltuieli)
        elif ui==0:
            exit()

