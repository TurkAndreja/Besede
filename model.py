import json
import random

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


class ZbirkaBesedil:

    def __init__(self, ime, datoteka):
        self.ime = ime
        self.datoteka = datoteka
        #self.besedila = [] #seznam objektov razreda Besedilo
        #self.stevilo = len(self.besedila)
        self.iz_jsona_nalozi_atribute()

    def dodaj_besedilo(self, besedilo, avtor, tema, kljucne_besede, naslov, stran, leto, zalozba):
        self. iz_jsona_nalozi_atribute()
        #tema = dodana_tema.s
        besedilo = Besedilo(besedilo, avtor.split(", "), tema.split(", "), kljucne_besede.split(", "), Knjiga(naslov, stran, leto, zalozba))
        self.besedila.append(besedilo)
        self.shrani_zbirko_v_json_slovar()

    def iz_jsona_nalozi_atribute(self):
        with open(self.datoteka) as datoteka:
            slovar = json.load(datoteka)
            self.stevilo = len(slovar.get("besedila"))
            self.besedila = [Besedilo.iz_slovarja_v_objekt_besedilo(besedilo) for besedilo in slovar["besedila"] ]

    def shrani_zbirko_v_json_slovar(self):
        slovar = {
            "besedila": [besedilo.iz_objekta_besedilo_v_slovar() for besedilo in self.besedila],
        }
        with open(self.datoteka, "w") as datoteka:
            return json.dump(slovar, datoteka, ensure_ascii = False, indent = 4)

    def isci(self, avtor, tema, kljucne_besede, naslov):

        seznam = []

        model = Besedilo("", avtor.split(", "), tema.split(", "), kljucne_besede.split(", "), Knjiga(naslov))
        atributi_modela = [model.avtor, model.tema, model.kljucne_besede]

        self.iz_jsona_nalozi_atribute()
        for slovar in self.besedila:
            atributi_slovarja = [slovar.avtor, slovar.tema, slovar.kljucne_besede]
            
            if not ali_je_seznam1_podseznam_seznama2(atributi_modela, atributi_slovarja):
                continue
            else:
                if (model.knjiga.naslov is not slovar.knjiga.naslov) and (model.knjiga.naslov is not None):
                    pass
                else:
                    seznam.append(slovar)

        self.shrani_zbirko_v_json_slovar()
                
        return seznam

    def izberi_nakljucno_besedilo(self):
        return random.choice(self.besedila)



class Besedilo:
    
    def __init__(self, besedilo, avtor, tema, kljucne_besede, knjiga):
        self.besedilo = besedilo
        self.avtor = avtor
        self.tema = tema
        self.kljucne_besede = kljucne_besede
        self.knjiga = knjiga #nek malo bolj poln slovar

    @staticmethod
    def iz_slovarja_v_objekt_besedilo(slovar):
        return Besedilo(
            besedilo = slovar["besedilo"],
            avtor = slovar["avtor"],
            tema = slovar["tema"],
            kljucne_besede = slovar["kljucne_besede"],
            knjiga = Knjiga.iz_slovarja_v_objekt_knjiga(slovar["knjiga"]),
        )

    def iz_objekta_besedilo_v_slovar(self):
        return {
            "besedilo": self.besedilo,
            "avtor": self.avtor,
            "tema": self.tema,
            "kljucne_besede": self.kljucne_besede,
            "knjiga": self.knjiga.iz_objekta_knjiga_v_slovar(),
        }


class Knjiga:

    def __init__(self, naslov = None, stran = None, leto_izida = None, zalozba = None):
        self.naslov = None if naslov == "" else naslov
        self.stran = None if stran == "" else stran
        self.leto_izida = None if leto_izida == "" else leto_izida
        self.zalozba = None if zalozba == "" else zalozba

    @staticmethod
    def iz_slovarja_v_objekt_knjiga(slovar):
        return Knjiga(
            slovar.get("naslov"),
            slovar.get("stran"),
            slovar.get("leto_izida"),
            slovar.get("zalozba"),
        )

    def iz_objekta_knjiga_v_slovar(self):
        return {
            "naslov": self.naslov,
            "stran": self.stran,
            "leto_izida": self.leto_izida,
            "zalozba": self.zalozba
        }