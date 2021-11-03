import numpy as np
import scipy.signal as ss
from FilterClass import Filter, ApproxType

class Legendre(Filter):
    def __init__(self, FilterData, nmin, nmax, Qmax):
        super().__init__(ApproxType.BW, FilterData, nmin, nmax, Qmax)

    def get_best_n(self):
        n, wo = ss.buttord(self.data.wp, self.data.wa, self.data.Ap, self.data.Aa, True)
        return n

    #def get_sos(self):
     #   sos = ss.butter(self.n, )

