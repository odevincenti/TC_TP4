import numpy as np
import scipy.signal as ss
from enum import IntEnum
from Approx.ApproxClass import Approx

# TIPOS DE FILTROS
class FilterType(IntEnum):
    LP = 0
    HP = 1
    BP = 2
    BR = 3

# TIPOS DE APROXIMACIONES
class ApproxType(IntEnum):
    BW = 0
    CH1 = 1
    CH2 = 2
    LG = 3
    C = 4
    B = 5
    G = 6

# DATOS PARA EL FILTRO
class FilterData:
    def __init__(self, wp, wa, Ap, Aa, des):
        self.wp = wp
        self.wa = wa
        self.Ap = Ap
        self.Aa = Aa
        self.des = des
        self.wo = None
        self.n = None
        self.Q = None

    def set_wo(self, wo):
        self.wo = wo

    def set_order(self, n):
        self.n = n

    def set_Q(self, Q):
        self.Q = Q


########################################################################################################################
# FILTER CLASS
# Parámetros:
# - type (Tipo de filtro): - LP (Low Pass)
#                          - HP (High Pass)
#                          - BP (Band Pass)
#                          - BR (Band Reject)
# - approx (Tipo de aproximación): - BW (Butterworth)
#                                  - CH1 (Cheby I)
#                                  - CH2 (Cheby II)
#                                  - LG (Legendre)
#                                  - C (Cauer)
#                                  - B (Bessel)
#                                  - G (Gauss)
# - wp: Frecuencia de paso
# - wa: Frecuencia de atenuación
# - Ap: Máxima atenuación en la banda pasante
# - Aa: Mínima atenuación en la banda atenuante
# - des: Rango de desnormalización
# - nmin: Grado mínimo
# - nmax: Grado máximo
# - Qmax: Máxima selectividad
# ----------------------------------------------------------------------------------------------------------------------

class Filter:
    def __init__(self, type, approx, wp, wa, Ap, Aa, des, nmin, nmax, Qmax):
        self.type = type
        '''self.wp = wp
        self.wa = wa
        self.Ap = Ap
        self.Aa = Aa
        self.des = des
        self.n = n
        self.Q = Q'''
        self.data = FilterData(wp, wa, Ap, Aa, des)
        self.approx = approx
        self.wan = self.wan()
        self.n = self.get_n(nmin, nmax, Qmax)
        self.sos = self.get_sos()

    # get_best_n: Calcula el n óptimo, depende de la aproximación. No toma en cuenta nmin y nmax.
    def get_best_n(self):
        n = 0
        return n

    # get_wan: Calcula la wa normalizada
    def get_wan(self):
        if self.type == FilterType.LP:
            wan = self.data.wa/self.data.wp
        elif self.type == FilterType.HP:
            wan = self.data.wp/self.data.wa
        elif self.type == FilterType.BP:
            wan = (self.data.wa[1] - self.data.wa[0])/(self.data.wp[1] - self.data.wp[0])
        elif self.type == FilterType.BP:
            wan = (self.data.wp[1] - self.data.wp[0])/(self.data.wa[1] - self.data.wa[0])
        else:
            wan = 0
            self.filter_error()
        return wan

    # get_n: A partir del n óptimo, calcula el orden del filtro tomando en cuenta las restircciones.
    def get_n(self, nmin, nmax, Qmax):
        n = self.get_best_n()
        if n < nmin:
            n = nmin
        elif n > nmax:
            n = nmax
        return n
        # todo: buscar como limitar Q

    # get_wo: Calcula la frecuencia fundamental wo.
    def get_wo(self):
        if self.type == FilterType.BP or self.type == FilterType.BR:
            self.data.set_wo(np.sqrt(self.data.wp[0]*self.data.wp[1]))

    # get_sos: Obtiene la función del filtro
    def get_sos(self):
        sos = None
        return sos

    def filter_error(self):
        print("ERROR: No se pudo crear el filtro")
        return






