# PRAKTIKUM 3
Alur algoritma program latihan1.py, latihan2.py, dan program1.py



# ALUR ALGORITMA latihan1.py
Sebelum memulai membuatnya, silahkan buka aplikasi Sublime terlebih dahulu, karna disini saya menggunakan Sublime.
>![open sublime](https://user-images.githubusercontent.com/46733958/52685704-52ea1200-2f7d-11e9-8093-acabbfbd8896.png)

# STEP 1

Jika sudah, silahkan tekan ctrl+s . Dan simpan file tersebut dengan berakhiran ".py" , contoh:
>![save](https://user-images.githubusercontent.com/46733958/52624002-45cb1580-2ee0-11e9-91bd-07e50f4f6fdf.png)
```
".py" adalah program python.
```

# STEP 2

Untuk line 1 silahkan ketik sesuai apa yang ada dibawah ini,
>![line 1](https://user-images.githubusercontent.com/46733958/52623276-8a55b180-2ede-11e9-968d-c15077fca50c.png)

Dan, untuk line 2 sampai line 9, silahkan ketik sesuai apa yang ada dibawah ini, ingat perhatikan setiap penempatan titik, dan koma.
>![line 2-9](https://user-images.githubusercontent.com/46733958/52623675-7f4f5100-2edf-11e9-8efa-f3a2cbca74a2.png)

Berikut penjelasannya:
```
print ('Masukkan nilai N: 5')
import random
jumlah = 5
a = 0
for x in range(jumlah):
	i = random.uniform(.0,.5)
	a+=1
	print('data ke:',a,'==>', i)
print ('selesai')

"print"  : berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks.
"import" : fungsi lanjut yang dipanggil oleh statement import.
"random" : untuk menentukan suatu pilihan. 
"range"  : merupakan fungsi yang menghasilkan list. Fungsi ini akan menciptakan sebuah list baru dengan rentang nilai tertentu. 
"uniform": digunakan untuk menampilkan bilangan float random dengan batas awal bilangan x, dan batas akhir bilangan y.
```

# STEP 3

Jika sudah, dan sama seperti apa yang ada di "Step 2" silahkan save program kalian. Dan jalankan program tersebut melalui command prompt.

Dan jika program yang tadi kita buat berhasil, maka tampilannya seperti dibawah ini:
>![latihan1work](https://user-images.githubusercontent.com/46733958/52685903-0d7a1480-2f7e-11e9-9151-4dc2d5d24f49.png)




# ALUR ALGORITMA latihan2.py
Sebelum memulai membuatnya, silahkan buka aplikasi Sublime terlebih dahulu, karna disini saya menggunakan Sublime.
>![open sublime](https://user-images.githubusercontent.com/46733958/52685704-52ea1200-2f7d-11e9-8093-acabbfbd8896.png)

# STEP 1

Jika sudah, silahkan tekan ctrl+s . Dan simpan file tersebut dengan berakhiran ".py" , contoh:
>![latihan2](https://user-images.githubusercontent.com/46733958/52686023-7e213100-2f7e-11e9-82f6-b2b76630c6fe.png)
```
".py" adalah program python.
```

# STEP 2

Untuk line 1 dan line 2 silahkan ketik sesuai apa yang ada dibawah ini,
>![line 1-2 latihan2](https://user-images.githubusercontent.com/46733958/52686504-91cd9700-2f80-11e9-8722-564571a4b5c7.png)

>Mengapa harus "max=0" dan type datanya itu "while True" ?
```
Karena jika suatu kodingan menggunakan while, kodingan itu tidak akan berhenti dengan menginput bilangan "0". Maka jika kita menginput bilangan "0" , maka eksekusi pun selesai.
```
Untuk line 2 sampai line 8, silahkan ketik sesuai apa yang ada dibawah ini, ingat perhatikan setiap penempatan titik, dan koma.
>![line 2-8](https://user-images.githubusercontent.com/46733958/52625819-6a28f100-2ee4-11e9-88ad-a952435b1960.png)

Berikut penjelasannya:
```
max=0
while True:
	a=int(input('Masukkan bilangan='))
	if max < a:
		max = a
	if a==0:
		break
print('Bilangan terbesarnya adalah',max)

"max"	: fungsi bulid-in untuk mencari nilai tertinggi. Fungsi ini dapat diberikan sebuah parameter berupa angka.
"while"	: disebut uncounted loop (perulangan yang tak terhitung), untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.
"int"	: berfungsi mengkonversi bilangan maupun string angka menjadi bilangan bulat (integer).
"if"	= Bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan. Dengan fungsi ini kita bisa menjalankan suatu perintah dalam kondisi tertentu. 
"input"	: masukan yang kita berikan ke program.
"break"	: fungsi yang menghentikan operasi dibawahnya jika suatu kondisi yang ditentukan telah tercapai.
"print"	: berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks.
```

# STEP 3

Jika sudah, dan sama seperti apa yang ada di "Step 2" silahkan save program kalian. Dan jalankan program tersebut melalui command prompt.

Dan jika program yang tadi kita buat berhasil, maka tampilannya seperti dibawah ini:
>![latihan2work](https://user-images.githubusercontent.com/46733958/52686194-3bac2400-2f7f-11e9-84f8-9897824c74c5.png)




# ALUR ALGORITMA program1.py
Sebelum memulai membuatnya, silahkan buka aplikasi Sublime terlebih dahulu, karna disini saya menggunakan Sublime.
>![open sublime](https://user-images.githubusercontent.com/46733958/52685704-52ea1200-2f7d-11e9-8093-acabbfbd8896.png)

# STEP 1
Jika sudah, silahkan tekan ctrl+s . Dan simpan file tersebut dengan berakhiran ".py" , contoh:
>![program1](https://user-images.githubusercontent.com/46733958/52686898-3b615800-2f82-11e9-866b-3dff1fbe3b64.png)
```
".py" adalah program python.
```

# STEP 2

Untuk line 1 dan line 2 silahkan ketik sesuai apa yang ada dibawah ini,
>![program1 line 1-2](https://user-images.githubusercontent.com/46733958/52687150-37820580-2f83-11e9-88be-b67eda629771.png)

>Mengapa "for x in range" ?
```
"for" perulangan yang terhitung, dan "range" mengembalikan deret integer berurut pada range yang ditentukan dari start sampai stop.
```
Untuk line 2 sampai line 16 silahkan ketik sesuai apa yang ada dibawah ini, ingat perhatikan setiap penggunaan titik dan koma!
>![program1 line 2-16](https://user-images.githubusercontent.com/46733958/52687322-f2120800-2f83-11e9-81ef-b4e7f7f643c2.png)

Berikut penjelasannya
```
a = 100000000
for x in range(1,9):
	if(x>=1 and x<=2):
		b=a*0
		print('Laba bulan ke-',x,' :',b)
	if(x>=3 and x<=4):
		c=a*0.1
		print('Laba bulan ke-',x,' :',c)
	if(x>=5 and x<=7):
		d=a*0.5
		print('Laba bulan ke-',x,' :',d)
	if(x==8):
		e=a*0.2
		print('Laba bulan ke-',x,' :',e)
total = b+b+c+c+d+d+d+e
print('\nTotal : ', total)

"print"	= Fungsi "print()" berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (Layar).
"if"	= Bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan. Dengan fungsi ini kita bisa menjalankan suatu perintah dalam kondisi tertentu. 
"for"	= Perulangan yang terhitung.
"range" = Mengembalikan deret integer berurut pada range yang ditentukan dari start sampai stop.
"for x in range" = "for" perulangan yang terhitung, dan "range" mengembalikan deret integer berurut pada range yang ditentukan dari start sampai stop.
"\nTotal" = Membuat garis baru, dan menampilkan total hasil dari apa yang kita inginkan.
```

# STEP 3
Jika sudah, dan sama seperti apa yang ada di "Step 2" silahkan save program kalian. Dan jalankan program tersebut melalui command prompt.

Dan jika program yang tadi kita buat berhasil, maka tampilannya seperti dibawah ini:
>![program1work](https://user-images.githubusercontent.com/46733958/52687986-ca706f00-2f86-11e9-8a8f-756dae1096ef.png)

				    SEKIAN DAN TERIMAKASIH, Rizky Ibrahim 18 TI A1

