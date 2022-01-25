import matplotlib.pyplot as plt
tahun=["2014","2015","2016","2017","2018"]
total=[429.874,275.737,234.451,262.899,283.640]
#1.)membuat kanvas kosong
fig,ax=plt.subplots()
#2.digunakan untuk plots garis nilai X terhadap garis nilai Y
ax.plot(tahun,total)
#3.memberikan label pada sumbu garis
ax.set_xlabel("Tahun")
ax.set_ylabel("Total")
#4.menyertai judul
ax.set_title("Analisis Tenaga Kerja Migran Indonesia")
#menampilkan sebuah gambar
plt.show()
