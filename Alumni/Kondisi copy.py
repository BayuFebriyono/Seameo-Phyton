import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

alumni = pd.read_excel("Alumni.xlsx")
group = alumni.groupby("Jurusan/Paket Keahlian")


kondisi = alumni[alumni['Kondisi Saat ini']=='Bekerja'].groupby("Jurusan/Paket Keahlian")
jumlah = group["Nama Lengkap"].count()
jurusan = group["Jurusan/Paket Keahlian"].head().values

kondisi1 = kondisi["Kondisi Saat ini"].count()



x= []
y =[]

for ju in jurusan:
    if ju in x:
        continue
    x.append(ju)

for kon in kondisi1:
    y.append(kon)


plt.pie(y, labels = x, startangle = 90,autopct='%1.1f%%')
plt.axis("equal")
plt.legend()
plt.show()

