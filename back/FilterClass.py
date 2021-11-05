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
        #self.wan = None
        self.n = None
        self.wdes = None
        self.eps = None
        self.Q = None
        self.GD = None
        self.g = None

    def print_data(self):
        print("wp =", self.wp)
        print("wa =", self.wa)
        print("Ap =", self.Ap)
        print("Aa =", self.Aa)
        print("des =", self.des)
        #print("wan =", self.wan)
        print("n =", self.n)
        print("wdes =", self.wdes)
        print("eps =", self.eps)
        print("g =", self.g)
        print("GD =", self.GD)
        print("Q =", self.Q)
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
    def __init__(self, filter_type, approx, filter_data, n=None, Q=None, GD = None, nmin=None, nmax=None, Qmax=None):
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
        #self.data.wan = self.get_wan()
        self.data.eps = self.get_eps(self.data.Ap)
        self.data.GD = GD
        if n is not None: self.data.n = n
        else: n = self.get_n(nmin, nmax)
        if Q is not None: self.data.Q = Q
        self.zeros, self.poles, self.data.g = self.get_zpk(n)
        self.zeros, self.poles, self.data.g = self.denormalize()
        while not self.check_Q(Qmax):
            n = n - 1
            self.zeros, self.poles, self.data.g = self.get_zpk(n)
            self.zeros, self.poles, self.data.g = self.denormalize()
            if len(self.poles) == 0:
                print("No existe aproximación que cumpla con el Q máximo pretendido")
        self.data.n = n
        self.num, self.den = self.get_numden()
        self.fix_gain()
        self.num, self.den = self.get_numden()
        #self.sos = self.get_sos()
        #self.H = None

    # get_best_n: Calcula el n óptimo, depende de la aproximación. No toma en cuenta nmin y nmax.
    def get_best_n(self, nmin, nmax):
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
        elif self.type == FilterType.BR:
            wan = (self.data.wp[1] - self.data.wp[0])/(self.data.wa[1] - self.data.wa[0])
        else:
            wan = 0
            self.filter_error()
        return wan

    def denormalize(self):
        if self.approx == ApproxType.B:
            return self.zeros, self.poles, self.data.g
        elif self.type == FilterType.LP:
            self.get_desfactor(1, self.data.wa/self.data.wp)
            z, p, g = ss.lp2lp_zpk(self.zeros, self.poles, self.data.g, self.data.wp)
        elif self.type == FilterType.HP:
            self.get_desfactor(1, self.data.wp/self.data.wa)
            z, p, g = ss.lp2hp_zpk(self.zeros, self.poles, self.data.g, self.data.wp)
        elif self.type == FilterType.BP:
            self.get_desfactor(1, (self.data.wa[1] - self.data.wa[0])/(self.data.wp[1] - self.data.wp[0]))
            z, p, g = ss.lp2bp_zpk(self.zeros, self.poles, self.data.g, np.sqrt(self.data.wp[0]*self.data.wp[1]), self.data.wp[1] - self.data.wp[0])
            self.data.n = len(p)
        elif self.type == FilterType.BR:
            self.get_desfactor(1, (self.data.wp[1] - self.data.wp[0])/(self.data.wa[1] - self.data.wa[0]))
            z, p, g = ss.lp2bs_zpk(self.zeros, self.poles, self.data.g, np.sqrt(self.data.wp[0] * self.data.wp[1]), self.data.wp[1] - self.data.wp[0])
            self.data.n = len(p)
        else:
            self.filter_error()
            z, p, g = [None, None, None]

        return z, p, g

    def fix_gain(self):
        '''G = 1
        if self.type == FilterType.LP or self.type == FilterType.BR:
            w = np.linspace(1E-6, 1E-5, 3)
        elif self.type == FilterType.HP:
            w = np.linspace(1E9, 1E10, 3)
        elif self.type == FilterType.BP:
            wo = self.data.wp[0] + (self.data.wp[1] - self.data.wp[0])/2
            w = np.linspace(wo, wo * 1.1, 3)
        else:
            self.filter_error()
            w = [None, None]
        w, mod, ph = ss.bode([self.zeros, self.poles, self.data.g], w)
        k = np.power(10, mod[0]/20)
        return (G/k)#/np.power(10, self.data.Ap/20)'''
        if self.type == FilterType.LP or self.type == FilterType.BR:
            k = self.den[-1] / self.num[-1]
        elif self.type == FilterType.HP:
            k = self.den[0] / self.num[0]
        elif self.type == FilterType.BP:
            alpha = [-2*p.real for p in self.poles if p.imag > 0]
            k = np.prod(alpha)
        else:
            self.filter_error()
            k = None
        self.data.g = k * self.data.g
        return

    # get_n: A partir del n óptimo, calcula el orden del filtro tomando en cuenta las restricciones.
    def get_n(self, nmin, nmax):
        n = self.get_best_n(nmin, nmax)
        if nmin is not None and n < nmin:
            n = nmin
        elif nmax is not None and n > nmax:
            n = nmax
        return n

    '''# get_wo: Calcula la frecuencia fundamental wo.
    def get_wo(self):
        if self.type == FilterType.BP or self.type == FilterType.BR:
            self.data.set_wo(np.sqrt(self.data.wp[0]*self.data.wp[1]))
        wo = -1.0
        return wo'''

    '''# get_sos: Obtiene la función del filtro
    def get_sos(self):
        sos = ss.zpk2sos(self.zeros, self.poles, self.data.k)
        return sos'''

    '''
    def parse_sos(self, sos):
        for i in range(len(sos)):
            sos_slice = sos[i]
            sos_num = sos_slice[0:3]
            sos_num = sos_num[::-1]
            sos_den = sos_slice[3:6]'''

    def get_fun(self, n):
        z = [None]
        p = [None]
        g = None
        return z, p, g

    def get_desfactor(self, wp, wa):
        if self.data.Q is None:# and self.data.n is None:
            w, mod, ph = ss.bode([self.zeros, self.poles, self.data.g], w=np.linspace(wp / 10, wa * 5, num=100000))
            stop_band = [w for w, mod in zip(w, mod) if mod <= (-self.data.Aa)]
            adjust = (((wa - stop_band[0]) / stop_band[0]) * self.data.des + 1)*(1 - 0.3045*self.data.des)
        else:
            adjust = 1

        self.zeros = self.zeros * adjust
        self.poles = self.poles * adjust
        self.data.g = self.data.g * adjust

        return adjust

    def get_zpk(self, n):
        z, p, g = self.get_fun(n)
        z = np.around(z, 5)
        p = np.around(p, 5)
        return z, p, g

    def check_Q(self, Qmax):
        r = True
        Q = []
        for pole in self.poles:
            Q.append(abs(abs(pole) / (2 * pole.real)))
        self.data.Q = max(Q)
        if Qmax is not None and self.data.Q > Qmax:
            r = False
        return r

    def get_numden(self):
        num, den = ss.zpk2tf(self.zeros, self.poles, self.data.g)
        return num, den

    '''def get_H(self, w=None):
        w, H = ss.freqs(self.num, self.den, w)
        return H'''

    def get_eps(self, A):
        eps = np.sqrt(np.power(10, A/10) - 1)
        return eps

    '''def get_wlim(self, A, wp):
        wlim = -1.0
        return wlim'''

    '''def calculate_wdes(self, wdes_min, wdes_max):
        if wdes_min != -1 and wdes_max != -1:
            wdes = wdes_min + (wdes_max - wdes_min) * self.data.des
        else:
            print("Error al calcular wlim")
            wdes = -1
            self.filter_error()
        return wdes'''

    '''def get_wdes(self):
        if self.type == FilterType.LP:
            wdes_min = self.get_wlim(self.data.Ap, self.data.wp)
            wdes_max = self.get_wlim(self.data.Aa, self.data.wa)
            wdes = self.calculate_wdes(wdes_min, wdes_max)

        elif self.type == FilterType.HP:
            wdes_min = 1/self.get_wlim(self.data.Aa, 1/self.data.wa)
            wdes_max = 1/self.get_wlim(self.data.Ap, 1/self.data.wp)
            wdes = self.calculate_wdes(wdes_max, wdes_min)

        elif self.type == FilterType.BP:
            eps_p = self.get_eps(self.data.Ap)
            eps_a = self.get_eps(self.data.Aa)
            eps = eps_p + self.data.des * (eps_a - eps_p)
            wdes = [-1, -1]
            wdes[0] = 1/(eps**(-1/self.data.n)*(1/self.data.wp[0]))
            wdes[1] = eps**(-1/self.data.n)*self.data.wp[1]
            wodes = np.power(self.data.wp[0], 1 - self.data.des) * np.power(self.data.wp[1], self.data.des)
            #wodes = self.data.wp[0] ** self.data.des + self.data.wp[1] ** self.data.des
            wo = np.sqrt(self.data.wp[0] * self.data.wp[1])
            B = self.data.wp[1] - self.data.wp[0]
            wdes[0] = (np.sqrt((wodes * B) ** 2 + 4 * wo ** 2) + wodes * B) / 2
            wdes[1] = (np.sqrt((wodes * B) ** 2 + 4 * wo ** 2) - wodes * B) / 2

        elif self.type == FilterType.BR:
            wdes_min, wdes_max = [-1, -1], [-1, -1]
            wdes_min[0] = self.get_wlim(self.data.Ap, self.data.wp[0])
            wdes_max[0] = self.get_wlim(self.data.Aa, self.data.wa[0])
            wdes_min[1] = 1/self.get_wlim(self.data.Aa, 1/self.data.wa[1])
            wdes_max[1] = 1/self.get_wlim(self.data.Ap, 1/self.data.wp[1])
            wdes = [-1, -1]
            wdes[0] = self.calculate_wdes(wdes_min[0], wdes_max[0])
            wdes[1] = self.calculate_wdes(wdes_min[1], wdes_max[1])

        else:
            print("Error al calcular wlim")
            wdes = -1
            self.filter_error()

        return wdes'''

    def filter_error(self):
        print("ERROR: No se pudo crear el filtro")
        self.type = FilterType.ERR
        return

    def print_self(self):
        print("\nFILTER")
        print("type: " + ftypes[self.type])
        print("approx: " + atypes[self.approx])
        self.data.print_data()
        #print("sos:\n", self.sos)
        print("\t \t", self.num)
        print("H(s) = -----------------------------------------------------------------")
        print("\t \t", self.den)
        #if self.H is not None: print(self.H)
        print("Zeros:", self.zeros)
        print("Poles:", self.poles)