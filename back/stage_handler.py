from copy import copy
import numpy as np
import scipy.signal as ss

def get_stage_pairs(arr):
    pairs = []
    p = copy(arr)
    for i in range(len(p)):
        solo = True
        for j in range(i + 1, len(p)):
            if p[i].real - p[j].real < 1E-10 and p[i].imag + p[j].imag < 1E-10:
                pairs.append([p[i], p[j]])
                p = np.delete(p, j)
                solo = False
                break
            else:
                solo = True
        if solo:
            pairs.append([arr[i]])
        if len(pairs) * 2 >= len(arr):
            break
    return pairs

def get_pair_name(p):
    n = len(p)
    if n == 2:
        fo = (p[0] * p[1]).real/(2 * np.pi)**2
        Q = - ((p[0] + p[1]) / (p[0] * p[1])).real
        s = "Order " + str(n) + " - fo = " + format_unit(fo, 3) + " Hz - Q = {:.{p}e}".format(Q, p=3)
    elif n == 1:
        fo = np.abs(p[0].real / (2 * np.pi))
        s = "Order " + str(n) + " - fo = " + format_unit(fo, 3) + " Hz"
    else:
        s = "ERROR: Se ingresó una cantidad de polos o ceros distinta de 1 o 2"
    return s


def get_stage_tf(z, p, g):
    num, den = ss.zpk2tf(z, p, g)
    return num, den

def combine_tf(nums, dens):
    nums = [np.poly1d(num) for num in nums]
    dens = [np.poly1d(den) for den in dens]
    num = np.poly1d(1)
    for i in range(len(nums)):
        num = np.polymul(num, nums[i])
    den = np.poly1d(1)
    for i in range(len(dens)):
        den = np.polymul(den, dens[i])
    return num, den

def plot_stage(ax, tf):
    wmin, wmax = self.get_wminmax()
    wmin = wmin / (2 * np.pi)
    wmax = wmax / (2 * np.pi)
    w = np.linspace(wmin, wmax, int(100 * wmax / wmin))
    cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
    ax.grid()
    for i in range(len(self.filters)):
        if self.filters[i].visibility:
            self.filters[i].plot_mod(ax, cycle[i % len(cycle)], w, A)
    ax.legend(loc="best")
    if not A:
        ax.set_title("Frequency response - Module")
    else:
        ax.set_title("Attenuation")
    ax.set_xlabel("$f$ [Hz]")
    if not A:
        ax.set_ylabel("$|H(s)|$ [dB]")
    else:
        ax.set_ylabel("A [dB]")
    ax.set_xlim([wmin, wmax])
    return

# format_unit: Obtiene la unidad correcta y escala el número para que sea más fácil de leer
# Recibe a x como número y la devuelve como string
def format_unit(x, d=2):
    y = np.abs(x)
    if y < 1E-12:
        m = ""
    elif y < 1E-9:
        m = "p"         # Pico
        x = x / 1E-12
    elif y < 1E-6:
        m = "n"         # Nano
        x = x / 1E-9
    elif y < 1E-3:
        m = "u"         # Micro
        x = x / 1E-6
    elif y < 1:
        m = "m"         # Mili
        x = x / 1E-3
    elif y < 1E3:
        m = ""          # Normal
    elif y < 1E6:
        m = "k"         # Kilo
        x = x / 1E3
    elif y < 1E9:
        m = "M"         # Mega
        x = x / 1E6
    else:
        m = "G"         # Giga
        x = x / 1E9
    return "{:.{p}f}".format(x, p=d) + m


