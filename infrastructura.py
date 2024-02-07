import domeniu

def adauga_cheltuiala_la_buget(buget,cheltuiala):
    for chelt in buget:
        if domeniu.equal_cheltuiala(chelt,cheltuiala):
            raise ValueError("cheltuiala exista deja!\n")
    buget.append(cheltuiala)
    return buget

#def copiaza_o_lista(lista):
    #cpy=[]
    #for el in lista:
     #   cpy.append(el[:])
    #return lista

def concateneaza_sortate(cheltuieli1,cheltuieli2,cheltuieli3,cheltuieli4,cheltuieli5):
    cheltuieli=[]
    for i in range(len(cheltuieli1)):
        cheltuieli.append(cheltuieli1[i])
    for i in range(len(cheltuieli2)):
        cheltuieli.append(cheltuieli2[i])
    for i in range(len(cheltuieli3)):
        cheltuieli.append(cheltuieli3[i])
    for i in range(len(cheltuieli4)):
        cheltuieli.append(cheltuieli4[i])
    for i in range(len(cheltuieli5)):
        cheltuieli.append(cheltuieli5[i])
    return cheltuieli

def undo(history):
    '''
    Anuleaza ultima operatie
    :param history:
    :return:
    '''
    history.pop(len(history)-1)
    if history==[]:
        print("inaintea ultimei operatii lista era goala\n")
        return []
    else:
        return history[len(history)-1]

