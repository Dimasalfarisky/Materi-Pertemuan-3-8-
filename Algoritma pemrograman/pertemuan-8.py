# praktetk 1
#Metode sort() digunakan untuk menyortir elemen dalam list secara langsung (in-place). Metode ini mengubah urutan elemen mengubah urutan elemen dalam list asli

# Parameter
# - "Key" (Opsional) berfungsi untuk menentukan kriteria penyortiran
# - "Reverse" berfungsi jika value nya adalah "True" maka akan menyortir angka dari terbesari ke terkecil, dan apabila valuenya adalah "False" maka akan mengurutkan dari terkecil hingga terbesar.
#Mengurutkan angka Terkecil Hingga Terbesar
numerik = [12,13,21,23,31,33,41,43,100]
numerik.sort()
print(numerik)

numerik = [12,13,21,23,31,33,41,43,100]
numerik.sort(reverse=False)
print(numerik)

#Mengurutkan angka terbesar hingga terkecil
numerik = [12,13,21,23,31,33,41,43,100]
numerik.sort(reverse=True)
print(numerik)

#Berdasarkan abjad (huruf pertama)
nama  = ["Dimas", "Rahmat", "Roy", "Yusran", "Afrian"]
nama.sort()
print(nama)
#Kapital lebih didahulukan dibandingkan huruf non-kapital


# praktek 2
#Kondisi (If, Elif, Else)
#if = untuk mengevaluasi sebuah kondisi. Jika kondisi tersebut bernilai True, maka blok kode didalamnya akan dieksekusi
#Elif = untuk memeriksa beberapa kondisi secara beruruta. Hanya satu blok yang akan dieksekusi, yaitu yang kondisi pertama kali bernilai True
# Else = untuk memberikan aksi alternatif jika kondisi dalam "If" dan "Elif" bernilai false.

#Contoh
nilai = 86

if nilai >= 90:
  print("Grade : A")
elif nilai >= 75:
  print("Grade : B")
elif nilai >= 60:
  print("Grade : C")
else:
  print("Grade : D")

