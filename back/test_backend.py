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

    wp = np.array(fdata.wp) / (2 * np.pi)
    wa = np.array(fdata.wa) / (2 * np.pi)

    if ftype == FilterType.LP:
        rp = Rectangle((wp/10, Ap), wp - wp/10, Aa*4 - Ap, color="orange", alpha=0.5)
        ra = Rectangle((wa, 0), wa*10 - wa, Aa, color="orange", alpha=0.5)
        ax.set_xlim([wp/10, wa * 10 - wa])

    elif ftype == FilterType.HP:
        ra = Rectangle((wa / 10, 0), wa - wa / 10, Aa, color="orange", alpha=0.5)
        rp = Rectangle((wp, Ap), wp * 10 - wp, Aa*4 - Ap, color="orange", alpha=0.5)
        ax.set_xlim([wa/10, wp * 10 - wp])

    elif ftype == FilterType.BP:
        ra = Rectangle((wa[0] / 10, 0), wa[0] - wa[0] / 10, Aa, color="orange", alpha=0.5)
        rp = Rectangle((wp[0], Ap), wp[1] - wp[0], Aa * 4 - Ap, color="orange", alpha=0.5)
        r2 = Rectangle((wa[1], 0), wa[1]*10 - wa[1], Aa, color="orange", alpha=0.5)
        ax.set_xlim([wa[0]/10, wa[1]*10 - wa[1]])

    elif ftype == FilterType.BR:
        rp = Rectangle((wp[0]/10, Ap), wp[0] - wp[0]/10, Aa*4 - Ap, color="orange", alpha=0.5)
        ra = Rectangle((wa[0], 0), wa[1] - wa[0], Aa, color="orange", alpha=0.5)
        r2 = Rectangle((wp[1], Ap), wp[1] * 10 - wp[1], Aa*4 - Ap, color="orange", alpha=0.5)
        ax.set_xlim([wp[0]/10, wp[1]*10 - wp[1]])

    elif ftype == FilterType.GD:
        ax.set_xlim([wp/10, wp * 10])

    if ftype != FilterType.GD:
        ax.add_patch(rp)
        ax.add_patch(ra)
    if r2 is not None: ax.add_patch(r2)

    return

FS = FilterSpace()
#FS.addFilter(FilterType.LP, ApproxType.B, 1000 * (2 * np.pi), 3000 * (2 * np.pi), 3, 30, 100, rp=1, GD=1, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.LP, ApproxType.CH1, 1000 * (2 * np.pi), 3000 * (2 * np.pi), 3, 30, 0, rp=1, GD=1, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.HP, ApproxType.B, 4000, 1000, 3, 30, 0, rp=1, GD=1, nmin=1, nmax=20, Qmax=150)
#FS.addFilter(FilterType.BP, ApproxType.B, [2 * (2 * np.pi), 4 * (2 * np.pi)], [1 * (2 * np.pi), 5 * (2 * np.pi)], 5, 40, 0, n=3, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.BP, ApproxType.LG, [2 * (2 * np.pi), 4 * (2 * np.pi)], [1 * (2 * np.pi), 5 * (2 * np.pi)], 3, 20, 0, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.BR, ApproxType.C, [1, 5], [2, 4], 0.5, 20, 0, rp=1, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.BR, ApproxType.B, [1, 5], [2, 4], 0.5, 20, 100, rp=1, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.GD, ApproxType.B, 10, 1500, 3, 30, 0, tol=20, GD=10E-3, nmin=1, nmax=15, Qmax=150)
fil = FS.filters[0]
fil.print_self()

# BODE
fig, ax = plt.subplots(2, 1)
axmod, axph = ax
plot_template(axmod, fil.type, fil.data, False)
FS.plot_mod(axmod)
FS.plot_ph(axph)
'''b, a = fil.num, fil.den
wmin, wmax = fil.get_wminmax()
#wmin = min(fil.data.wp, fil.data.wa)/10 if fil.type <= FilterType.HP elif fil.type <= FilterType.GD else min(fil.data.wp[0], fil.data.wa[0])/10
#wmax = max(fil.data.wp, fil.data.wa)*10 if fil.type <= FilterType.HP else max(fil.data.wp[1], fil.data.wa[1])*10
w = np.linspace(wmin, wmax, int(wmax/wmin * 10))
#H = ss.TransferFunction(b, a)
fil.plot_mod(axmod, w)
fil.plot_ph(axph, w)
fig.suptitle("Filter frequency response")
axmod.set_xlabel('Frequency [radians / second]')
axmod.set_ylabel('Amplitude [dB]')
axmod.grid()
axph.set_xlabel('Frequency [radians / second]')
axph.set_ylabel('Phase [°]')
axph.grid()
#plt.ylim(-60, 10)
#plt.grid(which='both', axis='both')
#plt.show()'''

# POLOS Y CEROS
fig2, ax2 = plt.subplots(1, 1)
FS.plot_zp(ax2)
'''fig2.suptitle("Poles and Zeros")
ax2.scatter(fil.zeros.real, fil.zeros.imag, marker='o', edgecolors="red", facecolors="None")
ax2.scatter(fil.poles.real, fil.poles.imag, marker='x', color="blue")
ax2.set_xlabel('Real')
ax2.set_ylabel('Imaginary')
ax2.grid()'''

# RETARDO DE GRUPO
figGD, axGD = plt.subplots(1, 1)
FS.plot_gd(axGD)
'''wmin, wmax = fil.get_wminmax()
#wmin = min(fil.data.wp, fil.data.wa)/10 if fil.type <= FilterType.HP elif fil.type <= FilterType.GD else min(fil.data.wp[0], fil.data.wa[0])/10
#wmax = max(fil.data.wp, fil.data.wa)*10 if fil.type <= FilterType.HP else max(fil.data.wp[1], fil.data.wa[1])*10
w = np.linspace(0, wmax*2/3, int(wmax/wmin * 10))
fil.plot_gd(axGD, w)
#axGD.set_ylim([0, 1])
figGD.suptitle("Filter group delay")
axGD.set_xlabel('Frequency [radians / second]')
axGD.set_ylabel('Group Delay')
axGD.grid()'''

plt.show()




