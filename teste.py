import domeniu
import infrastructura
import validare
import business

def test_creeaza_cheltuiala():
    zi=12
    suma=13.5
    tip="Altele"
    epsilon=0.0000000001
    cheltuiala=domeniu.creeaza_cheltuiala(zi,suma,tip)
    assert(abs(domeniu.get_suma(cheltuiala)-suma)<epsilon)
    assert (domeniu.get_zi(cheltuiala) == zi)
    assert (domeniu.get_tip(cheltuiala) == tip)

def test_valideaza_cheltuiala():
    zi_valida = 12
    suma_valida = 13.5
    tip_valid = "Altele"
    cheltuiala_valida = domeniu.creeaza_cheltuiala(zi_valida, suma_valida, tip_valid)
    validare.valideaza_cheltuiala(cheltuiala_valida)
    zi_invalida = 32
    suma_invalida = -13.5
    tip_invalid = "altele"
    cheltuiala_invalida = domeniu.creeaza_cheltuiala(zi_invalida, suma_invalida, tip_invalid)
    validare.valideaza_cheltuiala(cheltuiala_valida)
    try:
        validare.valideaza_cheltuiala(cheltuiala_invalida)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="zi invalida!\nsuma invalida!\ntip invalid!\n")

def test_adauga_cheltuiala_la_buget():
    assert(infrastructura.adauga_cheltuiala_la_buget([],[14,300.0,"Intretinere"])==[[14,300.0,"Intretinere"]])
    assert(infrastructura.adauga_cheltuiala_la_buget([[12, 13.5, "Altele"],[11,14.0,"Telefon"]],[14,300.0,"Intretinere"])==[[12, 13.5, "Altele"],[11,14.0,"Telefon"],[14,300.0,"Intretinere"]])

def test_equal_cheltuiala():
    assert([11,300.0,"Telefon"])

def test_undo():
    assert business.undo([[1,2,3],[2,3,4],[3,4,5]])==[2,3,4]
test_undo()