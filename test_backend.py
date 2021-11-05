from backend import FilterSpace, FilterType, ApproxType
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss

FS = FilterSpace()
FS.addFilter(FilterType.LP, ApproxType.BW, 1.0, 4.0, 0.5, 20, 50,  nmin=1, nmax=8, Qmax=150)
#FS.addFilter(FilterType.HP, ApproxType.BW, 4.0, 1.0, 0.5, 20, 0,  nmin=1, nmax=8, Qmax=150)
#FS.addFilter(FilterType.BP, ApproxType.BW, [2, 4], [1, 5], 0.5, 20, 100, nmin=1, nmax=8, Qmax=150)
#FS.addFilter(FilterType.BR, ApproxType.BW, [1, 5], [2, 4], 0.5, 20, 100, nmin=1, nmax=8, Qmax=150)
butter = FS.filters[0]
butter.print_self()

# BODE
fig, ax = plt.subplots(2, 1)
axmod, axph = ax
b, a = butter.num, butter.den
#w, h = ss.freqs(b, a)#, ss.findfreqs(b, a, 500, 'ba'))
H = ss.TransferFunction(b, a)
w, mod, ph = ss.bode(H)
axmod.semilogx(w, mod)
axph.semilogx(w, ph)
fig.suptitle('Butterworth filter frequency response')
axmod.set_xlabel('Frequency [radians / second]')
axmod.set_ylabel('Amplitude [dB]')
axmod.grid()
axph.set_xlabel('Frequency [radians / second]')
axph.set_ylabel('Phase [°]')
axph.grid()
#plt.ylim(-60, 10)
#plt.grid(which='both', axis='both')
#plt.show()

# POLOS Y CEROS
fig2, ax2 = plt.subplots(1, 1)
fig2.suptitle("Poles and Zeros")
ax2.scatter(butter.zeros.real, butter.zeros.imag, marker='o', edgecolors="red", facecolors="None")
ax2.scatter(butter.poles.real, butter.poles.imag, marker='x', color="blue")
ax2.set_xlabel('Real')
ax2.set_ylabel('Imaginary')
ax2.grid()

plt.show()




