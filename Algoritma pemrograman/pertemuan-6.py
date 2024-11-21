# Praktek 1
#Fungsi Abs, Int, dan Round

#absolut
#pengertian abs() digunakan untuk mengembalikan nilai absolut (positif) dari suatu bilangan
print(abs(-120))  #=> OUTPUT = 120 (MENJADI NILAI POSITIF)
print(abs(12.54)) #=> OUTPUT = 12.54

#int
#pengertian int() digunakan untuk mengonversi nilai menjadi bilangan bulat (integer)
print(int(10.3))    #=> OUTPUT = 10
print(int("2024"))  #=> OUTPUT = 2024 (KARENA MENGGUNAKAN STRING (""))

#round
#pengertian round() digunakan untuk membulatkan bilangan desimal ke bilangan terdekat
print(round(12.3))  #=> OUTPUT = 12
print(round(12.7))  #=> OUTPUT = 13
print(round(123.77,1))  #=> OUTPUT = 123.9 (fungsi ,1 adalah meminta dibulatkan 1 angka dibelakang koma)
print(round(123.456,2))  #=> OUTPUT = 123.46 (fungsi ,2 adalah meminta dibulatkan 2 angka dibelakang koma)


#Praktek 2
# NEW CODING

# fungsi input
nama = input("Masukkan Nama Anda:")
print("Halo, " + nama + "!")              #jika variabel tidak menggunakan "int" maka lebih baik menggunakan simbol (+)

umur = int(input("Masukkan Umur Anda:"))
print("Umur anda adalah", umur, "tahun.")  #jikan variabel merupakan "int" maka harus menggunakan tanda (,) tidak menggunakan tanda (+)

angka1 = float(input("Masukkan angka pertama:"))
angka2 = float(input("Masukkan angka kedua:"))
hasil = angka1 + angka2
print("Hasil penjumlahan:", hasil)

jawaban = input("Apakah  Anda ingin melanjutkan? (y/t):") .lower()
if jawaban == "y":
  print("Program dilanjutkan")
else:
  print("Program diberhentikan")