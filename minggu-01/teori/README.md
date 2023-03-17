# BAB 1

## 1. Python

> Python sangat sederhana untuk digunakan. Menawarkan lebih banyak struktur dan dukungan lebih untu program besar daripada shell scripts atau batch file. Dengan python kita juga dapat membelah program menjadi modul-modul yang dapat kita gunakan kembali dalam program Python lainnya. Dan Python menawarkan koleksi module standar yang dapat kita gunakan.

> Python memungkinkan program ditulis dengan compact dan mudah dibaca. Program yang ditulis dengan Python biasanya jauh lebih pendek daripada program C, C++, atau Java yang setara, karena beberapa alasan:

    - Tipe data tingkat tinggi memungkinkan kita mengekspresikan operasi complex dalam satu pernyataan
    - Pengelompokan pernyataan dilakukan dengan lekukan alih-alih tanda kurung awal dan akhir
    - Tidak diperlukan deklarasi variabel atau argumen

# BAB 2

## 2. Menggunakan Intepreter Python

> Python interpreter biasanya terinstall pada /usr/local/bin/python3.10. Pada mesin Windows tempat Anda menginstal Python dari Microsoft Store, perintah python3.10 akan tersedia. Jika Anda menginstal launcher py.exe, Anda dapat menggunakan perintah py.

> Python interpreter bekerja seperti Unix Shell: ketika dipanggil dengan standard input yang terkoneksi pada mesin tty, itu akan membaca dan mengeksekusi perintah secara interaktif. Ketika dipanggil dengan argument nama file atau dengan file sebagai input standar, itu membaca dan mengeksekusi sebuah script dari file

> Secara default, Source code Python di-encode dengan UTF-8. Dalam encoding tersebut, karakter dari sebagian besar bahasa di dunia dapat digunakan sekaligus dalam <i>string literals</i>, <i>identifiers</i>, dan <i>comments</i>. Meskipun kebanyakan <i>Standard library</i> hanya menggunakan ASCII.

# BAB 3

## 3. Pengenalan Pada Python

### 3.1 Menggunakan Python Sebagai Kalkulator

- 3.1.1 Numbers

  ```
  >>> 2 + 2
  4
  >>> 50 - 5*6
  20
  >>> 20 / 4
  5

  >>> 5 ** 2 #perpangkatan
  25

  >>> width = 20
  >>> height = 5 * 9
  >>> width * height
  900
  ```

  > Dalam mode interaktif, ekspresi tercetak terakhir ditugaskan ke variabel \_ . Ini berarti ketika Anda menggunakan Python sebagai kalkulator, akan lebih mudah untuk melanjutkan perhitungan, misalnya:

  ```
  >>> tax = 12.5 / 100
  >>> price = 100.50
  >>> price * tax
  12.5625
  >>> price + _
  113.0625
  >>> round(_, 2)
  113.06
  ```

- 3.1.2 String

  >

  ```
  'spam eggs'  # single quotes
  'spam eggs'
  'doesn\'t'  # use \' to escape the single quote...
  "doesn't"
  "doesn't"  # ...or use double quotes instead
  "doesn't"
  '"Yes," they said.'
  '"Yes," they said.'
  "\"Yes,\" they said."
  '"Yes," they said.'
  '"Isn\'t," they said.'
  '"Isn\'t," they said.'

  ```

  ```
  >>> print('C:\some\name')  # \n berarti newline pada code ini
  C:\some
  ame
  >>> print(r'C:\some\name')
  C:\some\name
  ```

- 3.1.3 Lists

  > Python mengetahui beberapa jenis <i>compound data types</i>, yang digunakan untuk mengelompokkan values. Yang paling serbaguna adalah lists

  ```
  >>> squares = [1, 4, 9, 16, 25]
  >>> squares
  [1, 4, 9, 16, 25]

  >>> squares[0] #indexing untuk return item

  >>> squares + [36, 49, 64, 81, 100]
  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  ```

  ```
  >>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
  >>> 4 ** 3  # the cube of 4 is 64, not 65!
  64
  >>> cubes[3] = 64  # replace the wrong value
  >>> cubes
  [1, 8, 27, 64, 125]


  # Tidak seperti string yang bersifat immutable, list bersifat mutable
  >>> cubes.append(216)
  >>> cubes.append(7 ** 3)
  >>> cubes
  [1, 8, 27, 65, 125, 216, 343]
  ```
