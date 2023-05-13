from signal_utils import custom_plot
import numpy as np
from scipy.fft import rfft, irfft
from scipy.signal import convolve, butter, cheby1, bessel, freqz, filtfilt
import matplotlib.pyplot as plt
import signals
import soundfile as sf

x = signals.Input_1kHz_15kHz

fs = 1000

# FIR filters
# bartlett_ir = np.bartlett(48)
# hamming_ir = np.hamming(48)
# blackman_ir = np.blackman(48)
# custom_plot(
#     (bartlett_ir, hamming_ir, blackman_ir),
#     "Finite Impulse Response filters", "n", "h(n)", 
#     legends=("Bartlett filter", "Hamming filter", "Blackman filter"),
#     colors=("blue", "green", "red"),
# )

# bartlett_fr = rfft(bartlett_ir, 2048) / 25.5
# hamming_fr = rfft(hamming_ir, 2048) / 25.5
# blackman_fr = rfft(blackman_ir, 2048) / 25.5

# bartlett_magnitude = 20 * np.log10(np.abs(bartlett_fr))
# hamming_magnitude = 20 * np.log10(np.abs(hamming_fr))
# blackman_magnitude = 20 * np.log10(np.abs(blackman_fr))

# custom_plot(
#     (bartlett_magnitude, hamming_magnitude, blackman_magnitude),
#     "FIR filters' frequency magnitude", "f", "Magnitude (dB)", 
#     legends=("Bartlett filter", "Hamming filter", "Blackman filter"),
#     colors=("blue", "green", "red"),
# )

# x_filtered_bartlett = convolve(x, bartlett_ir, "same")
# x_filtered_hamming = convolve(x, hamming_ir, "same")
# x_filtered_blackman = convolve(x, blackman_ir, "same")

# custom_plot(
#     (x, x_filtered_bartlett, x_filtered_hamming, x_filtered_blackman),
#     "FIR filter", "n", "h(n)", 
#     legends=("Orginal", "Bartlettt filter", "Hamming filter", "Blackman filter"),
#     colors=("black", "blue", "green", "red"),
#     overlapped=False
# )

# custom_plot(
#     (x, x_filtered_bartlett, x_filtered_hamming, x_filtered_blackman),
#     "FIR filter", "n", "h(n)", 
#     legends=("Orginal", "Bartlettt filter", "Hamming filter", "Blackman filter"),
#     colors=("black", "blue", "green", "red"),
# )


# bartlett_ir_scaled = 2 * bartlett_ir / np.sum(bartlett_ir)
# hamming_ir_scaled = 2 * hamming_ir / np.sum(hamming_ir)
# blackman_ir_scaled = 2 * blackman_ir / np.sum(blackman_ir)

# x_filtered_bartlett_scaled = convolve(x, bartlett_ir_scaled, "same")
# x_filtered_hamming_scaled = convolve(x, hamming_ir_scaled, "same")
# x_filtered_blackman_scaled = convolve(x, blackman_ir_scaled, "same")

# custom_plot(
#     (x, x_filtered_bartlett_scaled, x_filtered_hamming_scaled, x_filtered_blackman_scaled),
#     "FIR filter scaled", "n", "h(n)", 
#     legends=("Orginal", "Bartlettt filter", "Hamming filter", "Blackman filter"),
#     colors=("black", "blue", "green", "red"),
#     overlapped=False
# )
# custom_plot(
#     (x, x_filtered_bartlett_scaled, x_filtered_hamming_scaled, x_filtered_blackman_scaled),
#     "FIR filter scaled", "n", "h(n)", 
#     legends=("Orginal", "Bartlettt filter", "Hamming filter", "Blackman filter"),
#     colors=("grey", "blue", "green", "red"),
# )


# IIR filter
# butter_b, butter_a = butter(1, 40, "lowpass", fs=fs)
# butter_w, butter_fr = freqz(butter_b, butter_a)
# butter_magnitude = 20 * np.log10(np.abs(butter_fr))

# bessel_b, bessel_a = bessel(4, 40, "lowpass", fs=fs)
# bessel_w, bessel_fr = freqz(bessel_b, bessel_a)
# bessel_magnitude = 20 * np.log10(np.abs(bessel_fr))

# cheby_b, cheby_a = cheby1(12, 1, 40, "lowpass", fs=fs)
# cheby_w, cheby_fr = freqz(cheby_b, cheby_a)
# cheby_magnitude = 20 * np.log10(np.abs(cheby_fr))

# custom_plot(
#     (butter_magnitude, bessel_magnitude, cheby_magnitude),
#     "Butter filter frequency response", "f", "Magnitude (dB)", 
#     legends=("Butter filter", "Bessel filter", "Cheby filter"),
#     x_axis=butter_w,
#     colors=("blue", "green", "red"),
#     overlapped=False
# )

# x_butter = filtfilt(butter_b, butter_a, x)
# x_bessel = filtfilt(bessel_b, bessel_a, x)
# x_cheby = filtfilt(cheby_b, cheby_a, x)

# custom_plot(
#     (x, x_butter, x_bessel, x_cheby),
#     "x filtered", "n", "x(n)", 
#     legends=("Original", "Butter", "Bessel", "Cheby"),
#     colors=("purple", "blue", "orange", "green"),
#     overlapped=False
# )

# custom_plot(
#     (x, x_butter, x_bessel, x_cheby),
#     "x filtered", "n", "x(n)", 
#     legends=("Original", "Butter", "Bessel", "Cheby"),
#     colors=("purple", "blue", "orange", "green")
# )

# X = rfft(x)
# X_butter = rfft(x_butter)
# X_bessel = rfft(x_bessel)
# X_cheby = rfft(x_cheby)

# custom_plot(
#     (np.abs(X), np.abs(X_butter), np.abs(X_bessel), np.abs(X_cheby)),
#     "X freqency filtered", "f", "magnitude", 
#     legends=("Original", "Butter", "Bessel", "Cheby"),
#     colors=("purple", "blue", "orange", "green"),
#     overlapped=False
# )

# custom_plot(
#     (np.abs(X), np.abs(X_butter), np.abs(X_bessel), np.abs(X_cheby)),
#     "X freqency filtered", "f", "magnitude", 
#     legends=("Original", "Butter", "Bessel", "Cheby"),
#     colors=("purple", "blue", "orange", "green")
# )

# highpass_b, higpass_a = butter(4, 100, btype='highpass', fs=fs)
# highpass_w, highpass_fr = freqz(highpass_b, higpass_a)
# highpass_magnitude = 20 * np.log10(np.abs(highpass_fr))

# custom_plot(
#     (highpass_magnitude, ),
#     "Highpass filter freqency resonse", "f", "Magnitude (dB)", 
#     legends=("highpass filter", ),
#     x_axis=highpass_w
# )

# x_high = filtfilt(highpass_b, higpass_a, x)

# custom_plot(
#     (x, x_high),
#     "x through highpass", "n", "x(n)", 
#     legends=("Original", "highpass"),
#     colors=("blue", "orange",),
#     overlapped=False
# )

# X_high = rfft(x_high)
# X = rfft(x)
# custom_plot(
#     (np.abs(X), np.abs(X_high)),
#     "X through highpass", "f", "magnitude", 
#     legends=("Original", "highpass"),
#     colors=("blue", "orange",),
#     overlapped=False
# )


# Load the voice signal
voice_data, sample_rate = sf.read('voice.wav')
voice_fr = rfft(voice_data)
voice_fr_magnitude = 20 * np.log10(np.abs(voice_fr))
custom_plot(
    (voice_data, ),
    "Original voice data",
    "Sample", "Amplitude",
    legends=("voice", )
)
custom_plot(
    (voice_fr_magnitude, ),
    "Original voice frequency",
    "f", "Magnitude (dB)",
    legends=("Original", )
)


n = np.arange(len(voice_data))
noise = np.random.normal(0, 0.03, len(voice_data))
voice_with_noise = voice_data + noise
voice_with_noise_fr = rfft(voice_with_noise)
voice_with_noise_fr_magnitude = 20 * np.log10(np.abs(voice_with_noise_fr))

output_file = 'voice_with_noise.wav'
sf.write(output_file, voice_with_noise, sample_rate)

# Plot
custom_plot(
    (voice_with_noise, ),
    "Voice with noise",
    "Sample", "Amplitude",
    legends=("voice with noise", )
)

custom_plot(
    (voice_with_noise_fr_magnitude, ),
    "Voice with noise frequency",
    "f", "Magnitude",
    legends=("voice with noise", )
)

voice_with_noise, noise_sample_rate = sf.read('voice_with_noise.wav')

noise_filter_b, noise_filter_a = cheby1(12, 1, 0.15, "lowpass",)
noise_filter_w, noise_filter_fr = freqz(noise_filter_b, noise_filter_a)
noise_filter_magnitude = 20 * np.log10(np.abs(noise_filter_fr))

custom_plot(
    (noise_filter_magnitude, ),
    "Noise filter frequency response", "f", "Magnitude (dB)", 
    x_axis=noise_filter_w,
)


filtered_voice = filtfilt(noise_filter_b, noise_filter_a, voice_with_noise)
sf.write("filtered_voice.wav", filtered_voice, noise_sample_rate)

custom_plot(
    (voice_with_noise, filtered_voice, ),
    "Filtered voice", "Sample", "Amplitude",
    legends=("voice with noise", "filtered voice"),
    colors=("blue", "orange")
)

filtered_voice_fr = rfft(filtered_voice)
filtered_voice_magnitude = 20 * np.log10(np.abs(filtered_voice_fr))

custom_plot(
    (voice_fr_magnitude, filtered_voice_magnitude, ),
    "Filtered voice magnitude", "f", "Magnitude (dB)",
    legends=("Original", "Filtered"),
    colors=("blue", "orange")
)