import numpy as np
import scipy.signal as ss
from enum import IntEnum

# TIPOS DE FILTROS
class FilterType(IntEnum):
    LP = 0
    HP = 1
    BP = 2
    BR = 3
    ERR = 4

# TIPOS DE APROXIMACIONES
class ApproxType(IntEnum):
    BW = 0
    CH1 = 1
    CH2 = 2
    LG = 3
    C = 4
    B = 5
    G = 6

ftypes = ["lowpass", "highpass", "bandpass", "bandstop"]
atypes = ["Butterworth", "Cheby I", "Cheby II", "Legendre", "Cauer", "Bessel", "Gauss"]

# DATOS PARA EL FILTRO
class FilterData:
    def __init__(self, wp, wa, Ap, Aa, des):
        self.wp = wp
        self.wa = wa
        self.Ap = Ap
        self.Aa = Aa
        self.des = des
        self.wan = None
        self.n = None
        self.wdes = None
        self.eps = None
        self.Q = None
        self.k = None

    def print_data(self):
        print("wp =", self.wp)
        print("wa =", self.wa)
        print("Ap =", self.Ap)
        print("Aa =", self.Aa)
        print("des =", self.des)
        print("wan =", self.wan)
        print("n =", self.n)
        print("wdes =", self.wdes)
        print("eps =", self.eps)
        print("k =", self.k)
        return

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
    def __init__(self, filter_type, approx, filter_data, nmin, nmax, Qmax):
        self.type = filter_type
        '''self.wp = wp
        self.wa = wa
        self.Ap = Ap
        self.Aa = Aa
        self.des = des
        self.n = n
        self.Q = Q'''
        self.data = filter_data
        self.approx = approx
        self.data.wan = self.get_wan()
        self.data.eps = self.get_eps(self.data.Ap)
        self.data.n = self.get_n(nmin, nmax, Qmax)
        self.data.wdes = self.get_wdes()
        self.sos = self.get_sos()
        self.num, self.den = self.get_numden()
        self.zeros, self.poles, self.data.k = self.get_zpk()
        self.H = None

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

    # get_n: A partir del n óptimo, calcula el orden del filtro tomando en cuenta las restricciones.
    def get_n(self, nmin, nmax, Qmax):
        n = self.get_best_n()
        if n < nmin:
            n = nmin
        elif n > nmax:
            n = nmax
        return n
        # todo: buscar como limitar Q

    '''# get_wo: Calcula la frecuencia fundamental wo.
    def get_wo(self):
        if self.type == FilterType.BP or self.type == FilterType.BR:
            self.data.set_wo(np.sqrt(self.data.wp[0]*self.data.wp[1]))
        wo = -1.0
        return wo'''

    # get_sos: Obtiene la función del filtro
    def get_sos(self):
        sos = None
        return sos

    '''
    def parse_sos(self, sos):
        for i in range(len(sos)):
            sos_slice = sos[i]
            sos_num = sos_slice[0:3]
            sos_num = sos_num[::-1]
            sos_den = sos_slice[3:6]'''

    def get_zpk(self):
        z, p, k = ss.tf2zpk(self.num, self.den)
        return z, p, k

    def get_numden(self):
        num, den = ss.sos2tf(self.sos)
        return num, den

    def get_H(self, w=None):
        w, H = ss.freqs(self.num, self.den, w)
        return H

    def get_eps(self, A):
        eps = np.sqrt(np.power(10, A/10) - 1)
        return eps

    def get_wlim(self, A):
        wlim = -1.0
        return wlim

    def get_wdes(self):
        wdes_min = self.get_wlim(self.data.Ap)
        wdes_max = self.get_wlim(self.data.Aa)
        if wdes_min != -1 and wdes_max != -1:
            wdes = wdes_min + (wdes_max - wdes_min)*self.data.des
        else:
            print("Error al calcular wlim")
            wdes = -1
            self.filter_error()
        return wdes

    def filter_error(self):
        print("ERROR: No se pudo crear el filtro")
        self.type = FilterType.ERR
        return

    def print_self(self):
        print("\nFILTER")
        print("type: " + ftypes[self.type])
        print("approx: " + atypes[self.approx])
        self.data.print_data()
        print("sos:\n", self.sos)
        print("\t \t", self.num)
        print("H(s) = -----------------------------------------------------------------")
        print("\t \t", self.den)
        if self.H is not None: print(self.H)
        print("Zeros:", self.zeros)
        print("Poles:", self.poles)


