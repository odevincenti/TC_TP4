import numpy as np
import scipy.signal as ss
from back.FilterClass import Filter, ApproxType


class Bessel(Filter):
    def __init__(self, filter_type, filter_data, n, Q, GD, nmin, nmax, Qmax):
        super().__init__(filter_type, ApproxType.B, filter_data, n, Q, GD, nmin, nmax, Qmax)

    def get_best_n(self, nmin, nmax):
        wan = self.data.wa * self.data.GD
        # wfn = self.ft * self.group_delay
        for n in range(nmin, nmax + 1):
            z, p, k = ss.bessel(n, 1, 'lowpass', analog=True, output='zpk', norm='delay')
            w, h = ss.freqs_zpk(z, p, k, worN=np.logspace(-1, np.log10(wan) + 3, num=2000))
            retGroup_f = -np.diff(np.unwrap(np.angle(h))) / np.diff(
                w)  # el retardo de grupo es la derivada de la fase respecto de w
            minPos = (np.abs(w - wan)).argmin()
            if retGroup_f[minPos] >= (1 - 1E-6):
                break
        return n


    def get_fun(self, n):
        z, p, k = ss.bessel(n, 1/self.data.GD, 'lowpass', analog=True, output='zpk', norm='delay')
        #factor = np.power(self.get_eps(self.data.Ap), -1/n)
        #p = [factor * pole for pole in p]
        return z, p, k
