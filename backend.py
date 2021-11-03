import numpy as np
from FilterClass import Filter, FilterType
import Approx.ApproxClass

class FilterSpace:
    def __init__(self):
        self.filters = []       # Arreglo de filtros
        self.w_unit = "Hz"      # Unidad de frecuencia
        self.mod_unit = "dB"    # Unidad de módulo
        self.ph_unit = "°"      # Unidad de fase

    # addFilter: Recibe parámetros para el filtro y si tienen sentido, lo crea.
    # Devuelve True si pudo crearlo, False si no.
    # OJO: LAS FRECUENCIAS SE INGRESAN EN RAD/S (Chaquear esto desde el front)
    def addFilter(self, type, approx, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
        if not self.check_filter(type, approx, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
            return False
        f = Filter(type, approx, wp, wa, Ap, Aa, des, nmin, nmax, Qmax)
        self.filters.append(f)
        return True

    # check_filter: Revisa que el filtro sea válido. Devuelve True si lo es, False si no.
    def check_filter(self, type, approx, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
        r = True
        r = r and self.check_freq(type, wp)
        r = r and self.check_freq(type, wa)
        if Ap > Aa:
            r = False
        return r

    # check_freq: Revisa que el formato de la frecuencia sea consistente con el tipo.
    def check_freq(self, type, w):
        r = True
        try:
            len_w = len(w)
        except TypeError:
            len_w = 1
        if (type == FilterType.LP or type == FilterType.HP) and (len_w != 1):
            print("ERROR: La frecuencia de paso o atenuación ingresada no es un único número")
            r = False
        elif (type == FilterType.BP or type == FilterType.BR) and (len_w != 2):
            print("ERROR: Las frecuencias de paso o atenuación ingresadas no son un arreglo")
            r = False
        return r





