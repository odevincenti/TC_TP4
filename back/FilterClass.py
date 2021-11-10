import numpy as np
import scipy.signal as ss
from enum import IntEnum
from copy import copy

# TIPOS DE FILTROS
class FilterType(IntEnum):
    LP = 0
    HP = 1
    BP = 2
    BR = 3
    GD = 4
    ERR = 5

# TIPOS DE APROXIMACIONES
class ApproxType(IntEnum):
    BW = 0
    CH1 = 1
    CH2 = 2
    LG = 3
    C = 4
    B = 5
    G = 6

ftypes = ["lowpass", "highpass", "bandpass", "bandstop", "group delay"]
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
        self.G0 = None
        self.n = None
        self.g = None
        self.eps = None
        self.Q = None
        self.GD = None
        self.tol = None

    def print_data(self):
        print("wp =", self.wp)
        print("wa =", self.wa)
        print("Ap =", self.Ap)
        print("Aa =", self.Aa)
        print("des =", self.des)
        print("n =", self.n)
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
    def __init__(self, filter_type, approx, filter_data, n=None, Q=None, nmin=None, nmax=None, Qmax=None, rp=None, GD=None, tol=None):
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
        self.visibility = True
        self.data.eps = self.get_eps(self.data.Ap)
        self.data.wan = self.get_wan()
        self.data.rp = rp
        self.data.GD = GD
        self.data.tol = tol
        self.pole_pairs = None
        self.pole_pair_names = None
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
        self.name = ftypes[self.type].capitalize() + " " + atypes[self.approx] + " order " + str(self.data.n)
        self.data.g = self.data.g * self.fix_gain(self.get_numden())
        self.num, self.den = self.get_numden()

    def add_name_index(self, i):
        self.name = "C" + str(i) + ": " + self.name
        return self.name

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
        elif self.type == FilterType.GD:
            if self.data.GD is None: self.data.GD = 1E-3
            wan = self.data.wp*self.data.GD
        else:
            wan = 0
            self.filter_error()
        return wan

    def denormalize(self):
        if self.type == FilterType.LP:
            self.get_desfactor(1, self.data.wa/self.data.wp)
            z, p, g = ss.lp2lp_zpk(self.zeros, self.poles, self.data.g, self.data.wp / (2 * np.pi))
        elif self.type == FilterType.HP:
            self.get_desfactor(1, self.data.wp/self.data.wa)
            z, p, g = ss.lp2hp_zpk(self.zeros, self.poles, self.data.g, self.data.wp / (2 * np.pi))
        elif self.type == FilterType.BP:
            self.get_desfactor(1, (self.data.wa[1] - self.data.wa[0])/(self.data.wp[1] - self.data.wp[0]))
            z, p, g = ss.lp2bp_zpk(self.zeros, self.poles, self.data.g, np.sqrt(self.data.wp[0]*self.data.wp[1]) / (2 * np.pi), (self.data.wp[1] - self.data.wp[0]) / (2 * np.pi))
            #self.data.n = len(p)
        elif self.type == FilterType.BR:
            self.get_desfactor(1, (self.data.wp[1] - self.data.wp[0])/(self.data.wa[1] - self.data.wa[0]))
            z, p, g = ss.lp2bs_zpk(self.zeros, self.poles, self.data.g, np.sqrt(self.data.wp[0] * self.data.wp[1]) / (2 * np.pi), (self.data.wp[1] - self.data.wp[0]) / (2 * np.pi))
            #self.data.n = len(p)
        elif self.type == FilterType.GD:
            z, p, g = ss.lp2lp_zpk(self.zeros, self.poles, self.data.g, 2 * np.pi/(self.data.GD * self.data.wp))
        else:
            self.filter_error()
            z, p, g = [None, None, None]

        return z, p, g

    def fix_gain(self, numden, ftype=None):
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
        if ftype is None: ftype = self.type
        num, den = numden
        if ftype == FilterType.LP or ftype == FilterType.BR or ftype == FilterType.GD:
            if num[-1] != 0: k = den[-1] / num[-1]
            else: k = 1
        elif ftype == FilterType.HP:
            k = den[0] / num[0]
            if self.approx == ApproxType.C: k = k * 10**(-self.data.Ap/20)
        elif ftype == FilterType.BP:
            '''wo = self.data.wp[0] + (self.data.wp[1] - self.data.wp[0]) / 2
            w = np.linspace(wo, wo * 1.1, 3)
            w, h = ss.freqs_zpk(self.zeros, self.poles, self.data.g, w)
            habs = abs(h[0])
            k = 20*np.log10(habs)

            k = -2 * self.data.Q ** 2

            k = 1 / k'''

            z, poles, g = ss.tf2zpk(num, den)
            alpha = [-2*p.real for p in poles if p.imag > 0]
            k = np.prod(alpha)/(num[0])#**(1/len(num))# - np.log10(self.data.eps)
            k = 1

        else:
            self.filter_error()
            k = None
        return k

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
        if self.approx != ApproxType.CH2 and self.data.Q is None:
            w, mod, ph = ss.bode([self.zeros, self.poles, self.data.g], w=np.linspace(wp / 10, wa * 5, num=100000))
            stop_band = [w for w, mod in zip(w, mod) if mod <= (-self.data.Aa)]
            if len(stop_band) == 0: adjust = 1
            else: adjust = (((wa - stop_band[0]) / stop_band[0]) * self.data.des + 1)
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
        if A is not None:
            eps = np.sqrt(np.power(10, A/10) - 1)
        else: eps = None
        return eps

    def get_GD(self, w=None, z=None, p=None, k=None):
        if w is None:
            wmin, wmax = self.get_wminmax()
            w = np.linspace(wmin, wmax, num=int(10*wmax/wmin))
        if z is None: z = self.zeros
        if p is None: p = self.poles
        if k is None: k = self.data.g

        w, mod, ph = ss.bode([z, p, k], w)
        gd = np.divide(- np.diff(ph), np.diff(w))
        gd = np.append(gd, gd[len(gd) - 1])
        if self.data.GD is not None: GD = self.data.GD
        elif gd[0] != 0 and not np.isnan(gd[0]):
            GD = 1/gd[0]
        if gd[0] == 0 or np.isnan(gd[0]):
            gd[0] = 1E-15
            GD = 1/gd[0]
        gd = gd*GD/gd[0]

        return w, gd

    def get_wminmax(self):
        if self.type <= FilterType.HP:
            wmin = min(self.data.wp, self.data.wa) / 10
            wmax = max(self.data.wp, self.data.wa) * 10
        elif self.type == FilterType.GD:
            wmin = self.data.wp / 10
            wmax = self.data.wp * 10
        else:
            wmin = min(self.data.wp[0], self.data.wa[0]) / 10
            wmax = max(self.data.wp[1], self.data.wa[1]) * 10
        return wmin, wmax

    '''def get_wlim(self, A, wp):
        wlim = -1.0
        return wlim

    def calculate_wdes(self, wdes_min, wdes_max):
        if wdes_min != -1 and wdes_max != -1:
            wdes = wdes_min + (wdes_max - wdes_min) * self.data.des
        else:
            print("Error al calcular wlim")
            wdes = -1
            self.filter_error()
        return wdes

    def get_wdes(self):
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

    # plot_mod: dibuja el módulo de la transferencia de la curva
    # Recibe: - ax: axis
    #         - c: color
    #         - w: arreglo de w
    #         - A: Atenuación (True) o Ganancia (False)
    def plot_mod(self, ax, c, w=None, A=False, N=True):
        if w is None:
            wmin, wmax = self.get_wminmax()
            w = np.linspace(wmin / (2 * np.pi), wmax / (2 * np.pi), int(wmax / wmin * 10))
        w, mod, ph = ss.bode([self.num, self.den], w)
        if A: mod = - mod
        #if N and self.type <= FilterType.HP: w = w / (min(self.data.wa, self.data.wp) / (2 * np.pi))
        #elif N and self.type <= FilterType.BR: w = w / self.data.wan
        ax.semilogx(w, mod, label=self.name, color=c)
        return

    def plot_ph(self, ax, c,  w=None):
        if w is None:
            wmin, wmax = self.get_wminmax()
            w = np.linspace(wmin, wmax, int(wmax / wmin * 10))
        w, mod, ph = ss.bode([self.num, self.den], w)
        ax.semilogx(w, ph, label=self.name, color=c)
        return

    def plot_gd(self, ax, c, w=None):
        if w is None:
            wmin, wmax = self.get_wminmax()
            w = np.linspace(wmin, wmax, int(wmax / wmin * 10))
        w, gd = self.get_GD(w)
        ax.plot(w, gd, label=self.name, color=c)
        return

    def plot_zp(self, ax, c):
        ax.scatter(self.zeros.real, self.zeros.imag, marker='o', edgecolors=c, facecolors="None")
        ax.scatter(self.poles.real, self.poles.imag, marker='x', color=c, label=self.name)
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

    def get_stage_pairs(self, arr):
        pairs = []
        p = copy(arr)
        for i in range(len(p)):
            solo = True
            for j in range(i + 1, len(p)):
                if p[i].real - p[j].real < 1E-10 and p[i].imag + p[j].imag < 1E-10:
                    pairs.append([p[i], p[j]])
                    p = np.delete(p, j)
                    solo = False
                    break
                else:
                    solo = True
            if solo:
                pairs.append([arr[i]])
            if len(pairs) * 2 >= len(arr):
                break
        return pairs

    def get_pole_pairs(self):
        pairs = self.get_stage_pairs(self.poles)
        self.pole_pairs = pairs
        self.pole_pair_names = []

        for pair in self.pole_pairs:
            self.pole_pair_names.append(self.get_pole_pair_name(pair))

        return self.pole_pair_names

    def get_pole_pair_name(self, p):
        n = len(p)
        if n == 2:
            fo = (p[0] * p[1]).real
            Q = - ((p[0] + p[1]) / (p[0] * p[1])).real
            s = "Order " + str(n) + " - fo = " + str(np.around(fo, 3)) + " Hz - Q = " + str(np.around(Q, 3))
        elif n == 1:
            fo = p[0].real
            s = "Order " + str(n) + " - fo = " + str(np.around(fo, 3)) + " Hz"
        else:
            s = "ERROR: Se ingresó una cantidad de polos distinta de 1 o 2"
        return s

    def get_zero_pairs(self):
        pairs = self.get_stage_pairs(self.zeros)
        self.pole_pairs = pairs
        self.pole_pair_names = []

        for pair in self.pole_pairs:
            self.pole_pair_names.append(self.get_pole_pair_name(pair))

        return self.pole_pair_names

    def get_zero_pair_name(self, p):
        n = len(p)
        if n == 2:
            fo = (p[0] * p[1]).real
            Q = - ((p[0] + p[1]) / (p[0] * p[1])).real
            s = "Order " + str(n) + " - fo = " + str(np.around(fo, 3)) + " Hz - Q = " + str(np.around(Q, 3))
        elif n == 1:
            fo = p[0].real
            s = "Order " + str(n) + " - fo = " + str(np.around(fo, 3)) + " Hz"
        else:
            s = "ERROR: Se ingresó una cantidad de polos distinta de 1 o 2"
        return s

    def pair_zeros(self, poles):
        zeros = self.get_stage_pairs()
        for j in range(self.zeros):
            minz = np.infty
            for j in range(j, len(self.zeros)):

                pass
        return

    def get_stage_tf(self, z, p):
        num, den = ss.zpk2tf(z, p, 1)
        return num, den



