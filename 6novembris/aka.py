# Kā apstrādāt datus, veidojot diagrammas
import matplotlib.pyplot as plt

import numpy as np
# numpy - pamata pakete pitonā, kura ļauj veikt zinātnisko staitļošanu

import pandas as pd
# pandas - datu analīzes bibliotēka

# Datu masīvs
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 17, 35, 29, 12]
 
# Zīmējam stabiņu diagrammu
plt.bar(categories, values, color="green")
plt.xlabel("Kategorijas")
plt.ylabel("Vērtības")
plt.title("Stabiņu diagramma")
plt.show()

# 1. Līniju grafiks ar masīvu sinuss grafiks
# datu masīvs - dati no kuriem tiks veidots masīvs
x= np.arange(0, 10, 0.1)
y= np.sin(x)

# Zīmējam Līniju grafiku
plt.plot(x,y, label="sin(x)", color="blue")
plt.xlabel("x vērtības")
plt.ylable("y vērtības")
plt.title("Līniju grafiks ar sinusoīdu")
plt.legend()
plt.show()

# mat - matemātika
# plot - līnijas diagrammas zīmēšana
# lib - bibliotēka



