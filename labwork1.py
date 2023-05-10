import signals
import matplotlib.pyplot as plt
from scipy.fft import rfft, fftshift, irfft
from scipy.signal import convolve
import numpy as np
from signal_utils import custom_plot, is_periodic

# Get the signal
x = signals.Input_1kHz_15kHz
h = signals.Impulse_response
ECG = signals.ECG


period_of_x = 48
print(is_periodic(x, 48))
# Processing input signal

# Plot the signal
x_period = x[0:period_of_x ]
custom_plot((x, x_period), "Input signal x(n)", "n", "x(n)", stem=True, 
            colors=("blue", "orange"), legends=("Whole signal", "One period"))

# Discrete Fourier Transform
X = rfft(x_period)
X_whole = rfft(x)


frequency_axis = np.arange(len(X))

# Plot the real part
custom_plot((X.real,), "X(e^(jw)) real part", "frequency f", "real", legends=("real",))

# Plot the imaginary part
custom_plot((X.imag,), "X(e^(jw)) imaginary part", "frequency f", "imaginary", legends=("imaginary",))

# Plot the magnitude
custom_plot((np.abs(X),), "X(e^(jw)) magnitude", "frequency f", "magnitude", legends=("magnitude",))

# Plot the phase
custom_plot((np.angle(X),), "X(e^(jw)) phase", "frequency f", "phase", legends=("phase",))

# Inverse Discrete Fourier Transform
reconstructed_x = irfft(X)

# Plot the reconstructed
custom_plot((x_period, reconstructed_x), "orginal vs reconstructed x(n)", "n", "x(n)",
            stem=True, colors=("blue", "orange"), legends=("Original", "Reconstructed"))


# Plot impulse response
custom_plot((h,), "h(n) impulse response", "n", "h(n)", legends=("h(n)", ), stem=True)

# Discrete Fourier Transform
H = rfft(h)

# Plot the real part
custom_plot((H.real,), "H(e^(jw)) real part", "frequency f", "real", legends=("real",))

# Plot the imaginary part
custom_plot((H.imag,), "H(e^(jw)) imaginary part", "frequency f", "imaginary", legends=("imaginary",))

# Plot the magnitude
custom_plot((np.abs(H),), "H(e^(jw)) magnitude", "frequency f", "magnitude", legends=("magnitude",))

# Plot the phase
custom_plot((np.angle(H),), "H(e^(jw)) phase", "frequency f", "phase", legends=("phase",))

# Calculate y output signal using convolution

# Padding he signals
x_pad = np.zeros(len(x_period) + len(h) - 1)
h_pad = np.zeros(len(x_period) + len(h) - 1)
x_pad[0:len(x_period)] = x_period
h_pad[0:len(h)] = h

# Calculating the DFT of the padded signals
H_pad = rfft(x_pad)
X_pad = rfft(h_pad)

convoled_y_period = np.convolve(x_period, h)
convoled_y = np.convolve(x, h)
custom_plot((convoled_y, convoled_y_period), "y(n)", "n", "y(n)", 
            legends=("Whole signal", "One period",), colors=("blue", "orange"), stem=True)
Y_convoled = rfft(convoled_y_period)

# Calculate Y signal using frequency multiplication

Y_f_mul_padded  = X_pad * H_pad
custom_plot((np.abs(Y_convoled), np.abs(Y_f_mul_padded)), "Y(e^(jw)) computed via convolution and f multiplication", 
            "f", "magnitude", legends=("convoled", "padded and f mult"), colors=("blue", "orange"))

y_padded_recon = irfft(Y_f_mul_padded)
custom_plot((convoled_y_period, y_padded_recon), "y(n) computed via convolution and f multiplication", 
            "n", "y(n)", legends=("convoled", "padded and f mult"), colors=("blue", "orange"), stem=True)


Y_f_mul = X * np.pad(H, (0, len(X) - len(H)), "constant")
reconstructed_y = irfft(Y_f_mul)
custom_plot((reconstructed_y, irfft(Y_convoled)), "Reconstructed y(n) in one period", "n", "y(n)",
            legends=("y(n) by f mutiplication", "y(n) by convolve"), colors=("blue", "orange"), stem=True)


# Plot the real part
custom_plot((Y_f_mul.real, Y_convoled.real), "Y(e^(jw)) by f multiplication vs convolve", "frequency f",
            "real", legends=("Y by f mutiplication", "Y by convole and DTF"), colors=("blue", "orange"))
# Plot the imaginary part
custom_plot((Y_f_mul.imag, Y_convoled.imag), "Y(e^(jw)) by f multiplication vs convolve", "frequency f",
            "imaginary", legends=("Y by f mutiplication", "Y by convole and DTF"), colors=("blue", "orange"))
# Plot the phase
custom_plot((np.angle(Y_f_mul), np.angle(Y_convoled)), "Y(e^(jw)) by f multiplication vs convolve", "frequency f",
            "phase", legends=("Y by f mutiplication", "Y by convole and DTF"), colors=("blue", "orange"))
# Plot the magnitude
custom_plot((np.abs(Y_f_mul), np.abs(Y_convoled)), "Y(e^(jw)) by f multiplication vs convolve", "frequency f",
            "magnitude",  legends=("Y by mutiplication", "Y by convole and DTF"), colors=("blue", "orange"))


remove_low = X * np.pad(H[::-1], (len(X) - len(H[::-1]), 0), "constant")

custom_plot((remove_low ,), "low remove", "frequency", "magnitude")
custom_plot((irfft(remove_low),), "impulse response for h low", "n", "h(n)", stem=True)

impose = irfft(remove_low)

custom_plot((convolve(x_period, impose), ), "impulse response for h low", "n", "h(n)", stem=True)


# Convolution with full overlap only
y_convolved_without_echo = convolve(x_period, h, "same")
Y_convolved_without_echo = rfft(y_convolved_without_echo)
custom_plot((y_convolved_without_echo,), "y(n) convolved without echo", "n", "y(n)", stem=True)
custom_plot((np.abs(Y_convolved_without_echo),), "Y(e^(jw)) convolved without echo", "f", "magnitude")

print(is_periodic(ECG, 128))


custom_plot((ECG, ECG[:128]), "ECG", "n", "ECG", 
            legends=("Whole signal", "One period"), colors=("blue", "orange"))


ECG_period = ECG[:128]
ECG_frequency = rfft(ECG_period)
custom_plot((np.abs(ECG_frequency),), "ECG frequency", "f", "ECG")

ECG_low = ECG_frequency * np.pad(H, (0, len(ECG_frequency) - len(H)), "constant")
custom_plot((np.abs(ECG_low),),  "ECG frequency through lowpass", "f", "magnitude", 
            legends=("ECG", ))
ECG_reconstructed = irfft(ECG_low)
custom_plot((ECG_reconstructed,),  "ECG reconstructed through lowpass", "n", "ECG", 
            legends=("ECG reconstructed", ))


HIGHPASS_frequency = H[::-1]
custom_plot((np.abs(HIGHPASS_frequency), ),  "HIGHPASS filter frequency response" , "f", 
            "HIGHPASS", legends=("highpass",))

X_high = X * np.hstack((HIGHPASS_frequency, np.ones(len(X) - len(HIGHPASS_frequency))))
custom_plot((np.abs(X_high, ),), "X through highpass filter" , "f", "magnitude")


n = np.arange(128)
noise1 = 2.3*np.sin(1001/(2*np.pi) * n)
noise2 = 0.4*np.sin(1002/(2*np.pi) * n)
noise3 = 5.5*np.sin(1003/(2*np.pi) * n)
noise4 = 7.2*np.sin(1004/(2*np.pi) * n)
noise5 = 1.3*np.sin(1005/(2*np.pi) * n)
noise6 = 1.6*np.sin(1006/(2*np.pi) * n)
whitenoise = noise1 + noise2 + noise3 + noise4 + noise5 + noise6
WHITENOISE_fre = rfft(whitenoise)
custom_plot((whitenoise, ), "White noise", "n", "White noise", 
            legends=("White noise",))
custom_plot((np.abs(WHITENOISE_fre), ), "White noise frequency", "f", 
            "magnitude", legends=("White noise",))

ECG_noise = ECG_period + whitenoise
ECG_noise_fre = rfft(ECG_noise)
custom_plot((np.abs(ECG_noise), ), "ECG noise", 
            "n", "ECG", legends=("ECG noise",))
custom_plot((np.abs(ECG_noise_fre), ), "ECG noise frequency", 
            "f", "magnitude", legends=("ECG noise",))

ECG_remove_noise = ECG_noise_fre * np.pad(H, (0, len(ECG_noise_fre) - len(H)), "constant")
ECG_without_noise = irfft(ECG_remove_noise)
custom_plot((np.abs(ECG_remove_noise), ), "ECG fre without noise", "f", "magnitude")
custom_plot((ECG_without_noise, ), "ECG without noise", "f", "magnitude")