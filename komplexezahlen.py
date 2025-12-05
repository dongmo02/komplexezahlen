from math import *

# Umwandlung eines Winkels in eine Pi-Darstellung
def winkel_zu_bogenmass(winkel):
    if winkel < 180:
        winkel = int(winkel)
        teiler = 180 // winkel
        ergebnis = "π" + "/" + str(teiler)
    else:
        teiler = winkel // 180
        teiler = int(teiler)
        ergebnis = "π" + str(teiler)
    return ergebnis

# Umwandlung einer Zahl in eine spezielle Bruchdarstellung
def bruch_darstellung(zahl):
    if zahl == sqrt(5):
        bruch = "√5"

# Klasse zur Darstellung komplexer Zahlen
class KomplexeZahl:

    # Konstruktor: realteil (float), imaginarteil (float)
    def __init__(self, realteil, imaginarteil):
        self.realteil = realteil
        self.imaginarteil = imaginarteil
        self.textform = 0

    # Geometrische Darstellung r(cos(θ) + sin(θ)i)
    def geometrische_form(self):
        betrag_quadrat = (self.realteil ** 2) + (self.imaginarteil ** 2)
        betrag = sqrt(betrag_quadrat)
        cos_theta = self.realteil / betrag

        if betrag_quadrat == 5:
            betrag = "√5"
        if betrag_quadrat == 2:
            betrag = "√2"

        winkel = acos(cos_theta)
        winkel = degrees(winkel)
        winkel_pi = winkel_zu_bogenmass(winkel)

        return f"{betrag}(cos({winkel_pi})+sin({winkel_pi})i)"

    # Standarddarstellung a + bi
    def __str__(self):
        if self.imaginarteil > 0:
            imag_text = "+" + str(self.imaginarteil)
        else:
            imag_text = str(self.imaginarteil)

        self.textform = str(self.realteil) + imag_text + "i"
        return self.textform

    # Addition komplexer Zahlen
    def __add__(self, wert):
        self.realteil += wert.realteil
        self.imaginarteil += wert.imaginarteil

        if self.imaginarteil > 0:
            imag_text = "+" + str(self.imaginarteil)
        else:
            imag_text = str(self.imaginarteil)

        self.textform = str(self.realteil) + imag_text + "i"
        return self.textform

    # Subtraktion komplexer Zahlen
    def __sub__(self, wert):
        self.realteil -= wert.realteil
        self.imaginarteil -= wert.imaginarteil

        if self.imaginarteil > 0:
            imag_text = "+" + str(self.imaginarteil)
        else:
            imag_text = str(self.imaginarteil)

        self.textform = str(self.realteil) + imag_text + "i"
        return self.textform

    # Multiplikation komplexer Zahlen
    def __mul__(self, wert):
        a = self.realteil
        b = self.imaginarteil
        c = wert.realteil
        d = wert.imaginarteil

        self.realteil = (a * c) + (b * d * -1)
        self.imaginarteil = (b * c) + (a * d)

        if self.imaginarteil > 0:
            imag_text = "+" + str(self.imaginarteil)
        else:
            imag_text = str(self.imaginarteil)

        self.textform = str(self.realteil) + imag_text + "i"
        return self.textform

    # Division komplexer Zahlen
    def __truediv__(self, wert):
        a = self.realteil
        b = self.imaginarteil
        c = wert.realteil
        d = wert.imaginarteil

        real_o = (a * c) + (b * (-1 * d) * -1)
        imag_o = (b * c) + (a * (-1 * d))

        if imag_o > 0:
            imag_text = "+" + str(imag_o)
        else:
            imag_text = str(imag_o)

        oben = str(real_o) + imag_text + "i"
        unten = (c * c) + (d * d)

        if a == c and b == d:
            self.textform = 1
        else:
            self.textform = oben + "/" + str(unter)

        return self.textform

    # Potenz einer komplexen Zahl
    def __pow__(self, potenz):
        a = self.realteil
        b = self.imaginarteil
        a1 = self.realteil
        b1 = self.imaginarteil

        while potenz > 1:
            realteil = (a * a1) + (b * b1 * -1)
            imaginarteil = (b * a1) + (a * b1)

            a1 = realteil
            b1 = imaginarteil
            potenz -= 1

            self.realteil = realteil
            self.imaginarteil = imaginarteil

        if self.imaginarteil > 0:
            imag_text = "+" + str(self.imaginarteil)
        else:
            imag_text = str(self.imaginarteil)

        self.textform = str(self.realteil) + imag_text + "i"
        return self.textform

# Beispiel
zahl1 = KomplexeZahl(1, 1)
zahl2 = KomplexeZahl(1, 2)

geo = zahl1.geometrische_form()
print(geo)
