import numpy as np
import scipy.signal as ss
from back.FilterClass import Filter, ApproxType

class Butterworth(Filter):
    def __init__(self, filter_type, filter_data, n, Q, rp, GD, nmin, nmax, Qmax):
        super().__init__(filter_type, ApproxType.BW, filter_data, n, Q, rp, GD, nmin, nmax, Qmax)

    def get_best_n(self, nmin, nmax):
        n, wo = ss.buttord(self.data.wp, self.data.wa, self.data.Ap, self.data.Aa, True)
        return n

    def get_fun(self, n):
        z, p, k = ss.buttap(n)
        factor = np.power(self.get_eps(self.data.Ap), -1/n)
        p = [factor * pole for pole in p]
        return z, p, k
