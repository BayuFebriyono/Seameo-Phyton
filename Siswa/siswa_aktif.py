import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import style

siswa = pd.read_excel("Siswa.xlsx")
group = siswa.groupby("Sekolah Asal")
sekolah = group["Sekolah Asal"].head(8).values
jumlah = group["Nama"].count()
tes = siswa.groupby("Sekolah Asal")[["Sekolah Asal"]]


style.use('ggplot')


x = []
for se in sekolah:
    if se in x :
        continue
    x.append(se)

y = []
for ju in jumlah:
    y.append(ju)



fig, ax = plt.subplots(figsize=(20, 10))

ax.bar(x, y, align='center')


ax.set_title('Sekolah Asal Siswa')
ax.set_ylabel('Jumlah')
ax.set_xlabel('Seokalh')



plt.show()
