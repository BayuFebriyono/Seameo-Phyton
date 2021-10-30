import pandas as pd
import matplotlib.pyplot as plt

siswa = pd.read_excel("Siswa.xlsx")
group = siswa.groupby("Alat Transportasi")
Transport = group["Alat Transportasi"].head(8).values
jumlah = group["Nama"].count()
tes = siswa.groupby("Sekolah Asal")[["Sekolah Asal"]]
print(jumlah)




x = []
for ta in Transport:
    if ta in x :
        continue
    x.append(ta)

y = []
for ju in jumlah:
    y.append(ju)


plt.pie(y, labels = x, startangle = 90)
plt.legend()
plt.show()