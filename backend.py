import numpy as np
from FilterClass import FilterType, FilterData, ApproxType
from Approx.butterworth import Butterworth

class FilterSpace:
    def __init__(self):
        self.filters = []       # Arreglo de filtros
        self.w_unit = "Hz"      # Unidad de frecuencia
        self.mod_unit = "dB"    # Unidad de módulo
        self.ph_unit = "°"      # Unidad de fase

    # addFilter: Recibe parámetros para el filtro y si tienen sentido, lo crea.
    # Devuelve True si pudo crearlo, False si no.
    # OJO: LAS FRECUENCIAS SE INGRESAN EN RAD/S (Chaquear esto desde el front)
    def addFilter(self, filter_type, approx, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
        if not self.check_filter(filter_type, approx, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
            return False
        f = switch_atypes.get(approx)(filter_type, wp, wa, Ap, Aa, des, nmin, nmax, Qmax)
        if f.type != FilterType.ERR:
            self.filters.append(f)
        else:
            print("Error al crear el filtro")
            del f
        return True

    # check_filter: Revisa que el filtro sea válido. Devuelve True si lo es, False si no.
    def check_filter(self, filter_type, approx, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
        r = True
        r = r and self.check_freq(filter_type, wp)
        r = r and self.check_freq(filter_type, wa)
        if Ap > Aa:
            r = False
        return r

    # check_freq: Revisa que el formato de la frecuencia sea consistente con el tipo.
    def check_freq(self, filter_type, w):
        r = True
        try:
            len_w = len(w)
        except TypeError:
            len_w = 1
        if (filter_type == FilterType.LP or filter_type == FilterType.HP) and (len_w != 1):
            print("ERROR: La frecuencia de paso o atenuación ingresada no es un único número")
            r = False
        elif (filter_type == FilterType.BP or filter_type == FilterType.BR) and (len_w != 2):
            print("ERROR: Las frecuencias de paso o atenuación ingresadas no son un arreglo")
            r = False
        return r

def butterworth(filter_type, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Butterworth(filter_type, data, nmin, nmax, Qmax)
    return f

def cheby1(filter_type, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Butterworth(filter_type, data, nmin, nmax, Qmax)
    return f

def cheby2(filter_type, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Butterworth(filter_type, data, nmin, nmax, Qmax)
    return f

def legendre(filter_type, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Butterworth(filter_type, data, nmin, nmax, Qmax)
    return f

# SWITCH
switch_atypes = {
    0: butterworth,
    1: cheby1,
    2: cheby2,
    3: legendre,
}



