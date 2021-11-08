import numpy as np
import scipy.signal as ss
from back.FilterClass import Filter, ApproxType, FilterType


class Bessel(Filter):
    def __init__(self, filter_type, filter_data, n, Q, nmin, nmax, Qmax, GD, tol):
        super().__init__(filter_type, ApproxType.B, filter_data, n, Q, nmin, nmax, Qmax, None, GD, tol)

    def get_best_n(self, nmin, nmax):
        if self.type == FilterType.GD:
            wpn = self.get_wan()*self.data.GD
            if self.data.tol is None: self.data.tol = 0.1
            n = nmin
            for i in range(nmax - nmin):
                [b, a] = ss.bessel(n, 1, analog=True, norm='delay')
                w, mod, ph = ss.bode([b, a])
                #w, h = ss.freqs_zpk(z, p, k, worN=np.logspace(wpn/10, wpn*10, num=2000))
                group_delay = np.divide(-np.diff(ph), np.diff(w))  # d(ph)/d(w)
                closest = (np.abs(w - wpn)).argmin()
                if group_delay[closest] >= (1 - self.data.tol):
                    break
                n = n + 1
        return n


    def get_fun(self, n):
        #z, p, k = ss.bessel(n, self.data.wp*self.data.GD, 'lowpass', analog=True, output='zpk', norm='delay')
        z, p, k = ss.bessel(n, 1, 'lowpass', analog=True, output='zpk', norm='delay')
        return z, p, k
