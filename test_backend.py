from backend import FilterSpace, FilterType, ApproxType
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss

FS = FilterSpace()
FS.addFilter(FilterType.LP, ApproxType.BW, 1.0, 4.0, 0.5, 20, 0, 1, 8, 80)
butter = FS.filters[0]
butter.print_self()


b, a = butter.num, butter.den
w, h = ss.freqs(b, a)
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green') # cutoff frequency
plt.show()








