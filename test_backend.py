from backend import FilterSpace, FilterType, ApproxType
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss

FS = FilterSpace()
FS.addFilter(FilterType.HP, ApproxType.BW, 4000, 1000, 0.5, 20, 0, 1, 8, 5)
butter = FS.filters[0]
butter.print_self()

b, a = butter.num, butter.den
#w, h = ss.freqs(b, a)#, ss.findfreqs(b, a, 500, 'ba'))
H = ss.TransferFunction(b, a)
w, mod, ph = ss.bode(H)
plt.semilogx(w, mod)
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
#plt.ylim(-60, 10)
plt.grid(which='both', axis='both')
plt.show()








