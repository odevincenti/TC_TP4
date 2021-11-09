import numpy as np
from back.FilterClass import FilterType, FilterData, ApproxType
from back.Approx.butterworth import Butterworth
from back.Approx.bessel import Bessel
from back.Approx.legendre import Legendre
from back.Approx.cheby1 import ChebyI
from back.Approx.cheby2 import ChebyII
from back.Approx.cauer import Cauer
from back.Approx.gauss import Gauss

class FilterSpace:
    def __init__(self):
        self.filters = []       # Arreglo de filtros
        self.w_unit = "Hz"      # Unidad de frecuencia
        self.mod_unit = "dB"    # Unidad de módulo
        self.ph_unit = "°"      # Unidad de fase

    # addFilter: Recibe parámetros para el filtro y si tienen sentido, lo crea.
    # Devuelve True si pudo crearlo, False si no.
    # OJO: LAS FRECUENCIAS SE INGRESAN EN RAD/S (Chaquear esto desde el front)
    def addFilter(self, filter_type, approx, wp, wa, Ap, Aa, des, n=None, Q=None, nmin=None, nmax=None, Qmax=None, rp=None, GD=None, tol=None):
        if self.check_filter(filter_type, approx, wp, wa, Ap, Aa) != "":
            print("No se pudo crear el filtro")
            return False
        wp, wa = self.check_symmetry(filter_type, wp, wa)
        f = switch_atypes.get(approx)(filter_type, wp, wa, Ap, Aa, des/100, n, Q, nmin, nmax, Qmax, rp, GD, tol)
        if f.type != FilterType.ERR:
            self.filters.append(f)
        else:
            print("Error al crear el filtro")
            del f
        return True

    # delFilter: Saca el filtro del FilterSpace y lo destruye
    # Recibe el filtro (elemento) (Lo puedo cambiar al índice o nombre, lo que resulte más cómodo)
    def delFilter(self, f):
        self.filters.remove(f)
        del f
        return

    # check_filter: Revisa que el filtro sea válido. Devuelve True si lo es, False si no.
    def check_filter(self, filter_type, approx, wp, wa, Ap, Aa):
        m = ""
        m = self.check_freq(filter_type, wp)
        if m == "":
            m = self.check_freq(filter_type, wa)
        if m == "" and filter_type == FilterType.LP and not wp < wa:
            m = "El orden de las frecuencias de atenuación y paso no corresponde al de un filtro pasa bajos"
        if m == "" and filter_type == FilterType.HP and not wa < wp:
            m = "El orden de las frecuencias de atenuación y paso no corresponde al de un filtro pasa altos"
        if m == "" and filter_type == FilterType.BP and not (wa[0] < wp[0] < wp[1] < wa[1]):
            m = "El orden de las frecuencias de atenuación y paso no corresponde al de un filtro pasa banda"
        elif m == "" and filter_type == FilterType.BR and not (wp[0] < wa[0] < wa[1] < wp[1]):
            m = "El orden de las frecuencias de atenuación y paso está mal"
        elif m == "" and filter_type == FilterType.GD and not (approx != ApproxType.B or approx != ApproxType.G):
            m = "Sólo se permiten filtros de retardo de grupo con aproximaciones de Bessel o de Gauss"
        #elif m == "" and (approx == ApproxType.B or approx == ApproxType.G) and filter_type != FilterType.GD:
        #    m = "Las aproximaciones de Bessel o Gauss deben ser de retardo de grupo"
        if Ap > Aa:
            m = "Ap no puede ser mayor que Aa"
        return m

    # check_freq: Revisa que el formato de la frecuencia sea consistente con el tipo.
    def check_freq(self, filter_type, w):
        m = ""
        try:
            len_w = len(w)
        except TypeError:
            len_w = 1
        if (filter_type == FilterType.LP or filter_type == FilterType.HP or filter_type == FilterType.GD) and len_w != 1:
            m = "ERROR: La frecuencia de paso o atenuación ingresada no es un único número"
        elif (filter_type == FilterType.BP or filter_type == FilterType.BR) and len_w != 2:
            m = "ERROR: Las frecuencias de paso o atenuación ingresadas no son un arreglo"
        return m

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

def butterworth(filter_type, wp, wa, Ap, Aa, des, n, Q, nmin, nmax, Qmax, rp, GD, tol):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Butterworth(filter_type, data, n, Q, nmin, nmax, Qmax, GD)
    return f

def cheby1(filter_type, wp, wa, Ap, Aa, des, n, Q, nmin, nmax, Qmax, rp, GD, tol):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = ChebyI(filter_type, data, n, Q, nmin, nmax, Qmax, rp, GD)
    return f

def cheby2(filter_type, wp, wa, Ap, Aa, des, n, Q, nmin, nmax, Qmax, rp, GD, tol):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = ChebyII(filter_type, data, n, Q, nmin, nmax, Qmax, GD)
    return f

def legendre(filter_type, wp, wa, Ap, Aa, des, n, Q, nmin, nmax, Qmax, rp, GD, tol):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Legendre(filter_type, data, n, Q, nmin, nmax, Qmax, GD)
    return f

def cauer(filter_type, wp, wa, Ap, Aa, des, n, Q, nmin, nmax, Qmax, rp, GD, tol):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Cauer(filter_type, data, n, Q, nmin, nmax, Qmax, GD)
    return f

def bessel(filter_type, wp, wa, Ap, Aa, des, n, Q, nmin, nmax, Qmax, rp, GD, tol):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Bessel(filter_type, data, n, Q, nmin, nmax, Qmax, GD, tol/100 if tol is not None else None)
    return f

def gauss(filter_type, wp, wa, Ap, Aa, des, n, Q, nmin, nmax, Qmax, rp, GD, tol):
    data = FilterData(wp, wa, Ap, Aa, des)
    f = Gauss(filter_type, data, n, Q, nmin, nmax, Qmax, GD, tol/100 if tol is not None else None)
    return f

# SWITCH
switch_atypes = {
    0: butterworth,
    1: cheby1,
    2: cheby2,
    3: legendre,
    4: cauer,
    5: bessel,
    6: gauss
}



