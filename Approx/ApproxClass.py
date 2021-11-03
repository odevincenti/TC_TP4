'''import numpy as np
import scipy.signal as ss
from enum import IntEnum


########################################################################################################################
class Approx:
    def __init__(self, type, FilterData, nmin, nmax, Qmax):
        self.type = type
        self.data = FilterData
        self.n = self.get_n(nmin, nmax, Qmax)
        self.sos = self.get_sos()

    def get_best_n(self):
        n = 0
        return n

    def get_n(self, nmin, nmax, Qmax):
        n = self.get_best_n()
        if n < nmin: n = nmin
        elif n > nmax: n = nmax
        return n
       

    def get_wo(self):


    def get_sos(self):
        sos = None
        return sos
'''
