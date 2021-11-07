import numpy as np
import scipy.signal as ss
from back.FilterClass import Filter, ApproxType

class Cauer(Filter):
    def __init__(self, filter_type, filter_data, n, Q, rp, GD, nmin, nmax, Qmax):
        super().__init__(filter_type, ApproxType.C, filter_data, n, Q, rp, GD, nmin, nmax, Qmax)

    def get_best_n(self, nmin, nmax):
        n, wo = ss.ellipord(self.data.wp, self.data.wa, self.data.Ap, self.data.Aa, True)
        return n

    def get_fun(self, n):
        if self.data.rp is None: self.data.rp = self.data.Ap/2
        z, p, k = ss.ellipap(n, self.data.Ap, self.data.Aa)
        return z, p, k
