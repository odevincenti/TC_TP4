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

    ax.add_patch(rp)
    ax.add_patch(ra)
    if r2 is not None: ax.add_patch(r2)

    return

FS = FilterSpace()
FS.addFilter(FilterType.LP, ApproxType.CH1, 1, 1.5, 0.5, 20, 0, rp=1, GD=1, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.HP, ApproxType.CH1, 1.5, 1.0, 0.5, 20, 0, rp=1, GD=1, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.BP, ApproxType.CH1, [2, 4], [1, 5], 3, 20, 0, nmin=1, nmax=15, Qmax=150)
#FS.addFilter(FilterType.BR, ApproxType.CH1, [1, 5], [2, 4], 0.5, 20, 10, rp=1, nmin=1, nmax=15, Qmax=150)
butter = FS.filters[0]
butter.print_self()

# BODE
fig, ax = plt.subplots(2, 1)
axmod, axph = ax
plot_template(axmod, butter.type, butter.data, False)
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




