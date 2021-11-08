import numpy as np

from back.backend import FilterSpace, FilterType, ApproxType
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import scipy.signal as ss
from copy import copy

def plot_template(ax, ftype, fdata, A=True):
    if not A:
        Ap = - copy(fdata.Ap)
        Aa = - copy(fdata.Aa)
        ax.set_ylim([Aa*4 - Ap, Aa/Ap])
    else:
        Ap = copy(fdata.Ap)
        Aa = copy(fdata.Aa)
        ax.set_ylim([-Aa/Ap, Aa * 4 - Ap])

    rp = None
    ra = None
    r2 = None

    if ftype == FilterType.LP:
        rp = Rectangle((fdata.wp/10, Ap), fdata.wp - fdata.wp/10, Aa*4 - Ap, color="orange", alpha=0.5)
        ra = Rectangle((fdata.wa, 0), fdata.wa*10 - fdata.wa, Aa, color="orange", alpha=0.5)
        ax.set_xlim([fdata.wp/10, fdata.wa * 10 - fdata.wa])

    elif ftype == FilterType.HP:
        ra = Rectangle((fdata.wa / 10, 0), fdata.wa - fdata.wa / 10, Aa, color="orange", alpha=0.5)
        rp = Rectangle((fdata.wp, Ap), fdata.wp * 10 - fdata.wp, Aa*4 - Ap, color="orange", alpha=0.5)
        ax.set_xlim([fdata.wa/10, fdata.wp * 10 - fdata.wp])

    elif ftype == FilterType.BP:
        ra = Rectangle((fdata.wa[0] / 10, 0), fdata.wa[0] - fdata.wa[0] / 10, Aa, color="orange", alpha=0.5)
        rp = Rectangle((fdata.wp[0], Ap), fdata.wp[1] - fdata.wp[0], Aa * 4 - Ap, color="orange", alpha=0.5)
        r2 = Rectangle((fdata.wa[1], 0), fdata.wa[1]*10 - fdata.wa[1], Aa, color="orange", alpha=0.5)
        ax.set_xlim([fdata.wa[0]/10, fdata.wa[1]*10 - fdata.wa[1]])

    elif ftype == FilterType.BR:
        rp = Rectangle((fdata.wp[0]/10, Ap), fdata.wp[0] - fdata.wp[0]/10, Aa*4 - Ap, color="orange", alpha=0.5)
        ra = Rectangle((fdata.wa[0], 0), fdata.wa[1] - fdata.wa[0], Aa, color="orange", alpha=0.5)
        r2 = Rectangle((fdata.wp[1], Ap), fdata.wp[1] * 10 - fdata.wp[1], Aa*4 - Ap, color="orange", alpha=0.5)
        ax.set_xlim([fdata.wp[0]/10, fdata.wp[1]*10 - fdata.wp[1]])

    elif ftype == FilterType.GD:
        ax.set_xlim([fdata.wp/10, fdata.wp * 10])

    if ftype != FilterType.GD:
        ax.add_patch(rp)
        ax.add_patch(ra)
    if r2 is not None: ax.add_patch(r2)

    return

FS = FilterSpace()
#FS.addFilter(FilterType.LP, ApproxType.B, 1000, 3000, 3, 30, 0, rp=1, GD=1, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.HP, ApproxType.BW, 4000, 1000, 0.5, 20, 20, rp=1, GD=1, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.BP, ApproxType.LG, [2, 4], [1, 5], 3, 20, 0, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.BR, ApproxType.C, [1, 5], [2, 4], 0.5, 20, 0, rp=1, nmin=1, nmax=15, Qmax=150)
FS.addFilter(FilterType.GD, ApproxType.G, 1000, 3000, 3, 30, 0, tol=20, GD=10E-3, nmin=1, nmax=15, Qmax=150)
fil = FS.filters[0]
fil.print_self()

# BODE
fig, ax = plt.subplots(2, 1)
axmod, axph = ax
plot_template(axmod, fil.type, fil.data, False)
b, a = fil.num, fil.den
wmin, wmax = fil.get_wminmax()
#wmin = min(fil.data.wp, fil.data.wa)/10 if fil.type <= FilterType.HP elif fil.type <= FilterType.GD else min(fil.data.wp[0], fil.data.wa[0])/10
#wmax = max(fil.data.wp, fil.data.wa)*10 if fil.type <= FilterType.HP else max(fil.data.wp[1], fil.data.wa[1])*10
w = np.linspace(wmin, wmax, int(wmax/wmin * 10))
H = ss.TransferFunction(b, a)
w, mod, ph = ss.bode(H, w)
axmod.semilogx(w, mod)
axph.semilogx(w, ph)
fig.suptitle("Filter frequency response")
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
ax2.scatter(fil.zeros.real, fil.zeros.imag, marker='o', edgecolors="red", facecolors="None")
ax2.scatter(fil.poles.real, fil.poles.imag, marker='x', color="blue")
ax2.set_xlabel('Real')
ax2.set_ylabel('Imaginary')
ax2.grid()

# RETARDO DE GRUPO
figGD, axGD = plt.subplots(1, 1)
wmin, wmax = fil.get_wminmax()
#wmin = min(fil.data.wp, fil.data.wa)/10 if fil.type <= FilterType.HP elif fil.type <= FilterType.GD else min(fil.data.wp[0], fil.data.wa[0])/10
#wmax = max(fil.data.wp, fil.data.wa)*10 if fil.type <= FilterType.HP else max(fil.data.wp[1], fil.data.wa[1])*10
w = np.linspace(0, wmax*2/3, int(wmax/wmin * 10))
w, gd = fil.get_GD(w)
axGD.plot(w, gd)
#axGD.set_ylim([0, 1])
figGD.suptitle("Filter group delay")
axGD.set_xlabel('Frequency [radians / second]')
axGD.set_ylabel('Group Delay')
axGD.grid()

plt.show()




