import numpy as np
import matplotlib.pyplot as plt

data_points = 100
def target_function(x, coeffs):

    scale_target = 1.  # scale_target of the data
    res = 0+0j
    for idx, coeff in enumerate(coeffs):
        exponent = np.complex128((idx+1) * 1j * scale_target * x)
        conj_coeff = np.conjugate(coeff)
        res += coeff * np.exp(exponent) + conj_coeff * np.exp(-exponent)

    return np.real(res)

def fourier_coefficients(f, K):
    """
    Computes the first 2*K+1 Fourier coefficients of a 2*pi periodic function.
    """
    n_coeffs = 2 * K + 1
    t = np.linspace(0, 2 * np.pi, n_coeffs, endpoint=False)
    y = np.fft.rfft(f(t)) / t.size

    return y

degree = 3

positive_idx = list(fourier_coefficients(lambda x: np.exp(np.complex128(1j*x)), degree))
# negative_idx = list(np.conjugate(positive_idx[::-1]))

# coefs = positive_idx

# for value in negative_idx:
#     coefs.append(value)

x = np.linspace(-1*np.pi, np.pi, data_points)

plt.plot(x, target_function(x, positive_idx), color='blue')
plt.axvline(0.0)
plt.axhline(0.0)
plt.show()