import numpy as np
from FilterClass import FilterType, FilterData, ApproxType
from Approx.butterworth import Butterworth
from Approx.bessel import Bessel
from Approx.legendre import Legendre
from Approx.cheby1 import ChebyI
from Approx.cheby2 import ChebyII

class FilterSpace:
    def __init__(self):
        self.filters = []       # Arreglo de filtros
        self.w_unit = "Hz"      # Unidad de frecuencia
        self.mod_unit = "dB"    # Unidad de módulo
        self.ph_unit = "°"      # Unidad de fase

    # addFilter: Recibe parámetros para el filtro y si tienen sentido, lo crea.
    # Devuelve True si pudo crearlo, False si no.
    # OJO: LAS FRECUENCIAS SE INGRESAN EN RAD/S (Chaquear esto desde el front)
    def addFilter(self, filter_type, approx, wp, wa, Ap, Aa, des, n=None, Q=None, rp=None, GD=None, nmin=None, nmax=None, Qmax=None):
        if not self.check_filter(filter_type, approx, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
            print("No se pudo crear el filtro")
            return False
        wp, wa = self.check_symmetry(filter_type, wp, wa)
        f = switch_atypes.get(approx)(filter_type, wp, wa, Ap, Aa, des/100, n, Q, rp, GD, nmin, nmax, Qmax)
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
        if r and filter_type == FilterType.LP and not wp < wa:
            print("El orden de las frecuencias de atenuación y paso no corresponde al de un filtro pasa bajos")
            r = False
        if r and filter_type == FilterType.HP and not wa < wp:
            print("El orden de las frecuencias de atenuación y paso no corresponde al de un filtro pasa altos")
            r = False
        if r and filter_type == FilterType.BP and not (wa[0] < wp[0] < wp[1] < wa[1]):
            print("El orden de las frecuencias de atenuación y paso no corresponde al de un filtro pasa banda")
            r = False
        elif r and filter_type == FilterType.BR and not (wp[0] < wa[0] < wa[1] < wp[1]):
            print("El orden de las frecuencias de atenuación y paso está mal")
            r = False
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
        if (filter_type == FilterType.LP or filter_type == FilterType.HP) and len_w != 1:
            print("ERROR: La frecuencia de paso o atenuación ingresada no es un único número")
            r = False
        elif (filter_type == FilterType.BP or filter_type == FilterType.BR) and len_w != 2:
            print("ERROR: Las frecuencias de paso o atenuación ingresadas no son un arreglo")
            r = False
        return r

    def check_symmetry(self, filter_type, wp, wa):
        if filter_type == FilterType.BP:
            if wp[0] * wp[1] <= wa[0] * wa[1]:
                wa[1] = (wp[0] * wp[1]) / wa[0]
            else:
                wa[0] = (wp[0] * wp[1]) / wa[1]
        elif filter_type == FilterType.BR:
            if wa[0] * wa[1] <= wp[0] * wp[1]:
                wp[1] = (wa[0] * wa[1]) / wp[0]
            else:
                wp[0] = (wa[0] * wa[1]) / wp[1]
        return wp, wa

def butterworth(filter_type, wp, wa, Ap, Aa, des, n, Q, rp, GD, nmin, nmax, Qmax):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Butterworth(filter_type, data, n, Q, rp, GD, nmin, nmax, Qmax)
    return f

def cheby1(filter_type, wp, wa, Ap, Aa, des, n, Q, rp, GD, nmin, nmax, Qmax):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = ChebyI(filter_type, data, n, Q, rp, GD, nmin, nmax, Qmax)
    return f

def cheby2(filter_type, wp, wa, Ap, Aa, des, n, Q, rp, GD, nmin, nmax, Qmax):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = ChebyII(filter_type, data, n, Q, rp, GD, nmin, nmax, Qmax)
    return f

def legendre(filter_type, wp, wa, Ap, Aa, des, n, Q, rp, GD, nmin, nmax, Qmax):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Legendre(filter_type, data, n, Q, rp, GD, nmin, nmax, Qmax)
    return f

def cauer(filter_type, wp, wa, Ap, Aa, des, n, Q, rp, GD, nmin, nmax, Qmax):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Bessel(filter_type, data, n, Q, rp, GD, nmin, nmax, Qmax)
    return f

def bessel(filter_type, wp, wa, Ap, Aa, des, n, Q, rp, GD, nmin, nmax, Qmax):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Bessel(filter_type, data, n, Q, rp, GD, nmin, nmax, Qmax)
    return f


# SWITCH
switch_atypes = {
    0: butterworth,
    1: cheby1,
    2: cheby2,
    3: legendre,
    4: cauer,
    5: bessel
}



