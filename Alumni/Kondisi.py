import pandas as pd
import matplotlib.pyplot as plt

alumni = pd.read_excel("Alumni.xlsx")
group = alumni.groupby("Kondisi Saat ini")
kondisi = group["Kondisi Saat ini"].head().values
jumlah = group["Nama Lengkap"].count()



x =[]
y = []

for ko in kondisi:
    if ko in x:
        continue
    x.append(ko)

for ju in jumlah:
    y.append(ju)

plt.pie(y, labels = x, startangle = 90,autopct='%2.1f%%')
plt.axis("equal")
plt.legend()
plt.show()