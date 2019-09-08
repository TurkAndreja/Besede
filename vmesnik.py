import bottle
from model import ZbirkaBesedil, Besedilo, Knjiga




def ali_je_seznam1_podseznam_seznama2(seznam1, seznam2):
    for mesto in range(3):
        for stvar in seznam1[mesto]:
            if stvar is "":
                pass
            elif stvar is not "" and stvar not in seznam2[mesto]:
                return False
            else:
                pass
    return True  





IME = "UVP"
DATOTEKA = "besedila.json"
zbirka = ZbirkaBesedil(IME, DATOTEKA)





@bottle.get('/')
def zacetna_stran(): 
    return bottle.template("domaca_stran.tpl")

@bottle.get("/dodaj/")
def dodaj():
    return bottle.template("dodaj.tpl")

@bottle.post("/dodano/")
def dodano():
    besedilo = bottle.request.forms.besedilo
    avtor = bottle.request.forms.avtor
    tema = bottle.request.forms.tema
    kljucne_besede = bottle.request.forms.kljucne_besede
    naslov = bottle.request.forms.naslov 
    stran = bottle.request.forms.stran
    leto_izida = bottle.request.forms.leto_izida
    zalozba = bottle.request.forms.zalozba


    if besedilo == "" or avtor == "" or tema == "" or kljucne_besede == "":
        bottle.redirect("/vse_dodaj/")

    zbirka.dodaj_besedilo(besedilo, avtor, tema, kljucne_besede, naslov, stran, leto_izida, zalozba)

    return bottle.template("dodano.tpl")

@bottle.get("/vse_dodaj/")
def vse_dodaj():
    return bottle.template("vse_dodaj.tpl")

@bottle.get("/isci/")
def isci():
    return bottle.template("isci.tpl")

@bottle.post("/najdeno/")
def najdeno():
    
    avtor = bottle.request.forms.avtor
    tema = bottle.request.forms.tema
    kljucne_besede = bottle.request.forms.kljucne_besede
    naslov = bottle.request.forms.naslov

    seznam = zbirka.isci(avtor, tema, kljucne_besede, naslov)

    if seznam == []:
        bottle.redirect("/nicesar/")

    return bottle.template("najdeno.tpl", seznam = seznam)

@bottle.get("/nakljucno/")
def nakljucno():
    besedilo = zbirka.izberi_nakljucno_besedilo()
    return bottle.template("presenecenje.tpl", besedilo = besedilo)

@bottle.get("/nicesar/")
def nicesar():
    return bottle.template("nicesar.tpl")










bottle.run(reloader=True, debug=True)