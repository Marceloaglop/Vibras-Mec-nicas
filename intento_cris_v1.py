import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
tabla = pd.read_csv(r"LAB 02\Mediciones limpias\Parte 1\Test(2024-10-10,15-58-18)\DataRecor2.csv", sep="\t", names=["tiempo", "posición"])
print(tabla.head())

# Gráfico de amplitud vs. tiempo
plt.figure(figsize=(10, 5))
plt.title("Gráfico Parte 1 medición 01")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición")
plt.plot(tabla["tiempo"], tabla["posición"], color="tab:blue", label="Datos")
plt.legend()
plt.show()

# Transformada de Fourier
# Definir la señal y la frecuencia de muestreo
signal = tabla["posición"].values
time = tabla["tiempo"].values
sampling_rate = 1 / np.mean(np.diff(time))  # calcular la frecuencia de muestreo

# Aplicar la transformada de Fourier
fft_values = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(len(signal), d=1/sampling_rate)

# Graficar la amplitud en función de la frecuencia, incluyendo la parte negativa
plt.figure(figsize=(10, 5))
plt.title("Transformada de Fourier completa de la señal")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
plt.plot(fft_freq, np.abs(fft_values))  # Muestra la transformada completa
plt.show()

# Gráfico de transformada de Fourier en el rango de -50 a +50 Hz
# Seleccionar solo el rango deseado
mask = (fft_freq >= -50) & (fft_freq <= 50)
fft_freq_rango = fft_freq[mask]
fft_values_rango = np.abs(fft_values[mask])

plt.figure(figsize=(10, 5))
plt.title("Transformada de Fourier (rango de -50 a +50 Hz)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
plt.plot(fft_freq_rango, fft_values_rango, color="purple")
plt.show()
