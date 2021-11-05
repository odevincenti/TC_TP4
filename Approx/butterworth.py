import numpy as np
import scipy.signal as ss
from FilterClass import Filter, ApproxType, ftypes

class Butterworth(Filter):
    def __init__(self, filter_type, filter_data, n, Q, nmin, nmax, Qmax):
        super().__init__(filter_type, ApproxType.BW, filter_data, n, Q, nmin, nmax, Qmax)

    def get_best_n(self):
        n, wo = ss.buttord(self.data.wp, self.data.wa, self.data.Ap, self.data.Aa, True)
        return n

    def get_wlim(self, n, A, w):
        eps = self.get_eps(A)
        wlim = np.power(eps, -1/n)*w
        return wlim

    def get_sos(self):
        sos = ss.butter(self.data.n, self.data.wdes, ftypes[self.type], True, 'sos')
        return sos

    def get_numden(self):
        ba = ss.butter(self.data.n, self.data.wdes, ftypes[self.type], True, 'ba')
        num = ba[0]
        den = ba[1]
        return num, den
