import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

print("GRACIAS Clau")
#sep="\t" es pq los archivos estan separados por tabs ;)
tabla = pd.read_csv(r"LAB 02\Mediciones limpias\Parte 1\Test(2024-10-10,15-58-18)\DataRecor2.csv", sep="\t", names = ["tiempo","posición"])
print(tabla.head())



var1 = find_peaks(tabla["posición"], distance= 50 ) # guarda los indices de los peaks
print(type(var1))
print(var1)
print(var1[0])

tablapeaks = tabla.iloc[var1[0],:]
#plt.plot(tablapeaks["tiempo"],tablapeaks["posición"])
#plt.show()

tabla_pos = tabla[tabla["posición"]>0]

#plt.plot(tabla_pos["tiempo"],tabla_pos["posición"])
#plt.show()
'''
var1 = find_peaks(tabla_pos["posición"], distance= 8*10**2 ) # guarda los indices de los peaks
print(type(var1))
print(var1)
print(var1[0])

tablapeaks = tabla_pos.iloc[var1[0],:] #GOOOOOOOOD
plt.plot(tablapeaks["tiempo"],tablapeaks["posición"])
plt.plot(tabla["tiempo"],tabla["posición"])
plt.show()
'''

##########################################################

var1 = find_peaks(tabla["posición"], distance= 2*8*10**2 ) # guarda los indices de los peaks
tablapeaks = tabla.iloc[var1[0],:] #GOOOOOOOOD


plt.title("Gráfico Parte 1 medición 01")
plt.xlabel("tiempo [s]")
plt.ylabel("posición maybe, no estoy segur??")
plt.plot(tabla["tiempo"],tabla["posición"], color="tab:blue")
plt.plot(tablapeaks["tiempo"],tablapeaks["posición"], "-" , color="r", linewidth = 1)

plt.show()