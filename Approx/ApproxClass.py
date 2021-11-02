import numpy as np
import scipy.signal as ss
from enum import IntEnum

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
    def __init__(self, wp, wa, Ap, Aa, des, n, Q):
        self.wp = wp
        self.wa = wa
        self.Ap = Ap
        self.Aa = Aa
        self.des = des
        self.n = n
        self.Q = Q

########################################################################################################################
class Approx:
    def __init__(self, type, FilterData, nmin, nmax, Qmax):
        self.type = type

    def get_n(self, FilterData):
        return




