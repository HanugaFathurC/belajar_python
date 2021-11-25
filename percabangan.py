#if_else_biasa

#contoh1
nilai_mahasiswa=70 

if nilai_mahasiswa > 60 :
    print("Kamu lulus")
    
#contoh2
nilaiMahasiswa = 80

if nilaiMahasiswa > 80 :
    print("Nilai kamu baik")
elif nilaiMahasiswa > 70 :
    print("Tingkatkan nilai kamu") 
else :
    print("Kamu remidi")

#contoh3
nilaiUjianMahasiswa = float(input("Masukkan Nilaimu "))

if nilaiUjianMahasiswa >= 80 :
    print("Nilai kamu baik")
elif nilaiUjianMahasiswa > 70 :
    print("Tingkatkan nilai kamu") 
else :
    print("Kamu remidi")

#nested_if
nilai_mahasiswa1 = 60 
nilai_mahasiswa2 = 80 
nilai_mahasiswa3 = 90 
nilai_mahasiswa4 = 55
kkm = 60



#contoh1
if nilai_mahasiswa1 >= kkm :
    if nilai_mahasiswa1 == kkm :
        print("Kamu lulus tapi harus banyak belajar lagi.")
    elif nilai_mahasiswa1 > 80 :
        print ("Selamat km lulus dengan nilai yang baik. Tetap belajar")
    else : 
        print ("Kamu mendapat nilai yang sangat baik. Pertahankan")
else:
    print("Mohon maaf kamu remidi") 

#contoh2
nilai = float(input("Masukan nilaimu:" ))
if nilai >= 60 :
    if nilai == 60 :
        print("Kamu lulus tapi harus banyak belajar lagi.")
    elif nilai > 80 :
        print ("Selamat km lulus dengan nilai yang sangat baik. Tetap belajar")
    else : 
        print ("Kamu mendapat nilai yang  baik. Pertahankan")
else:
    print("Mohon maaf kamu remidi") 
    
#contohlain
nilai = float(input("Inputkan nilaimu: "))

if nilai >= 90:
   grade = "A"
elif nilai >= 70:
   grade = "B"
elif nilai >= 50:
   grade = "C"
elif nilai >= 40:
   grade = "D"
else:
   grade = "E"

print(grade)


#nb float digunakan untuk angka desimal int untuk angka bulat sedangkan str untuk string.
#jika melakukan convert caranya gampang
#tinggal float(masukan variabelmu) maka tipe data akan berubah jadi float
#penjelasan lebih lanjut di next chapter