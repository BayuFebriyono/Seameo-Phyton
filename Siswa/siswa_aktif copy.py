import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import style

siswa = pd.read_excel("Siswa.xlsx")
asal_smp = siswa.groupby('Sekolah Asal')['Nama'].count().reset_index(name='Jumlah')

final =asal_smp.nlargest(5, ['Jumlah'])

jumlah=[]
for i in final['Jumlah']:
    jumlah.append(i)

sekolah1 =[]
for i in final['Sekolah Asal']:
    sekolah1.append(i)
           
fig, ax = plt.subplots()

ax.barh(sekolah1, jumlah, align='center')

ax.set_title('Sekolah Asal Siswa')
ax.set_ylabel('Sekolah')
ax.set_xlabel('Jumlah')



plt.show()