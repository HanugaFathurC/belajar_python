"""
Nama : Hanuga Fathur Chaerulisma
TOPIC : Ekspresi, Variabel, Komposisi, Statemen, Input, Output secara sederhana
"""

print("Selamat datang di contoh soal trapesium berserta pembahasannya.")
nama=input("Silahkan masukan nama anda :) ", )
print("Haloo ", nama, "selamat belajar.") 

#Keliling Trapesium

#masalah1
print("1. Jika sebuah trapezium yang mempunyai panjang sisi AB = 2 cm, BC = 7 cm, CD = 9 cm, DA = 8 cm. Cari dan hitunglah keliling trapezium tersebut !")
ab = 2
bc = 7
cd = 9
da = 8
diketSoal1 = print("Diketahui ", "AB = ", ab, ", BC = ", bc, ", CD = " , cd, ", DA = ", da)
rumusKeliling = print("K = AB + BC + CD + DA") 
jawab1  = print("Jadi jawabannya adalah " , ab + bc + cd + da , "cm" ) 

print(diketSoal1, rumusKeliling, jawab1 ) #akan menghasilkan None di akhir karena perlu pendefinisian tipe data. Sebab variable dianggap none.


#masalah2
print("1. Jika sebuah trapezium yang mempunyai panjang sisi AB = 2 cm, BC = 7 cm, CD = 9 cm, DA = 8 cm. Cari dan hitunglah keliling trapezium tersebut !")
ab = 2
bc = 7
cd = 9
da = 8
diketSoal1 = ab, bc, cd, da
print("Diketahui pada soal AB, BC, CD, DA Trapesium adalah ", diketSoal1) #terdapat kurung pada diketSoal 1 karena disimpan pada suatu variabel dan memiliki tipe data yang berbeda.
print("K = AB + BC + CD + DA") 
jawab1  = ab + bc + cd + da 
print("Maka keliling lingkaran adalah ", jawab1, "cm" ) #tidak akan menghasilkan none karena variabelnya telah didefinisikan dengan variabel yang mengandung tipe data.


#penyelesaian
print("1. Jika sebuah trapezium yang mempunyai panjang sisi AB = 2 cm, BC = 7 cm, CD = 9 cm, DA = 8 cm. Cari dan hitunglah keliling trapezium tersebut !")
ab = 2
bc = 7
cd = 9
da = 8
print("Diketahui pada soal AB, BC, CD, DA Trapesium adalah ", ab, bc, cd, da) 
print("K = AB + BC + CD + DA") 
jawab1  = ab + bc + cd + da 
print("Maka keliling lingkaran adalah ", jawab1, "cm" ) 