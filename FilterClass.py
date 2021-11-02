import numpy as np
import scipy.signal as ss
from enum import IntEnum
from Approx.ApproxClass import Approx, FilterData

# TIPOS DE FILTROS
class FilterType(IntEnum):
    LP = 0
    HP = 1
    BP = 2
    BR = 3

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
#
# ----------------------------------------------------------------------------------------------------------------------

class Filter:
    def __init__(self, type, approx, wp, wa, Ap, Aa, n, Q, des, nmin, nmax, Qmax):
        self.type = type
        '''self.wp = wp
        self.wa = wa
        self.Ap = Ap
        self.Aa = Aa
        self.des = des
        self.n = n
        self.Q = Q'''
        self.data = FilterData(wp, wa, Ap, Aa, des, n, Q)
        self.approx = Approx(approx, self.data, nmin, nmax, Qmax)

    def filter_error(self):
        print("ERROR: No se pudo crear el filtro")
