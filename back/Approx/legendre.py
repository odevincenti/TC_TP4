import numpy as np
import scipy.signal as ss
from ApproxClass_old import Approx, ApproxType

class Legendre(Approx):
    def __init__(self, FilterData, nmin, nmax, Qmax):
        super().__init__(ApproxType.LG, FilterData, nmin, nmax, Qmax)


    def get_best_n(self):
        n = 1
