# Minggu 7 - OOP di Python

## 9. Classes

Class menyediakan sarana bundling data dan fungsionalitas bersama. Membuat class baru akan membuat tipe objek baru, yang memungkinkan instance baru dari tipe tersebut dibuat. Setiap instance class dapat memiliki atribut yang melekat padanya untuk mempertahankan statusnya. Instance class juga dapat memiliki metode (ditentukan oleh kelasnya) untuk memodifikasi statusnya.

Dibandingkan dengan bahasa pemrograman lain, mekanisme class Python menambahkan class dengan sintaks dan semantik baru yang minimal. Ini adalah campuran dari mekanisme class yang ditemukan di C++ dan Modula-3. Class Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme pewarisan class memungkinkan banyak class dasar, class turunan dapat mengganti metode apa pun dari class atau class dasarnya, dan metode dapat memanggil metode class dasar dengan nama yang sama . Objek dapat berisi jumlah dan jenis data yang sewenang-wenang. Seperti halnya modul, class mengambil bagian dari sifat dinamis Python: mereka dibuat saat runtime, dan dapat dimodifikasi lebih lanjut setelah dibuat.

### 9.1 Names and Object

Objek memiliki individualitas, dan banyak nama (dalam berbagai cakupan) dapat terikat ke objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain. Ini biasanya tidak dihargai pada pandangan pertama di Python, dan dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tupel). Namun, aliasing mungkin memiliki efek yang mengejutkan pada semantik kode Python yang melibatkan objek yang dapat diubah seperti daftar, kamus, dan sebagian besar jenis lainnya. Ini biasanya digunakan untuk kepentingan program, karena alias berperilaku seperti penunjuk dalam beberapa hal. Misalnya, melewatkan objek itu murah karena hanya sebuah pointer yang dilewatkan oleh implementasi; dan jika sebuah fungsi memodifikasi objek yang diteruskan sebagai argumen, pemanggil akan melihat perubahannya — ini menghilangkan kebutuhan akan dua mekanisme penerusan argumen yang berbeda seperti di Pascal.

## 9.2 Python Scopes and Namespaces

Namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama saat ini diimplementasikan sebagai kamus Python, tetapi biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin berubah di masa mendatang. Contoh ruang nama adalah: kumpulan nama bawaan (berisi fungsi seperti abs(), dan nama pengecualian bawaan); nama global dalam modul; dan nama lokal dalam pemanggilan fungsi. Dalam arti himpunan atribut suatu objek juga membentuk namespace. Hal penting yang harus diketahui tentang ruang nama adalah sama sekali tidak ada hubungan antara nama di ruang nama yang berbeda; misalnya, dua modul berbeda dapat menentukan fungsi maksimalkan tanpa kebingungan — pengguna modul harus mengawalinya dengan nama modul.

### 9.2.1 Scopes and Namespaces example

```Python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

Output :

```Python
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

## 9.3 A first look at Classes

### 9.3.1 Class Definition Syntax

```Python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

Definisi class, seperti definisi fungsi (pernyataan def) harus dijalankan sebelum memiliki efek apa pun. (Anda dapat menempatkan definisi class di cabang pernyataan if, atau di dalam fungsi.)

Dalam praktiknya, pernyataan di dalam definisi class biasanya berupa definisi fungsi, tetapi pernyataan lain diperbolehkan, dan terkadang berguna — kita akan membahasnya lagi nanti. Definisi fungsi di dalam class biasanya memiliki bentuk daftar argumen yang khas, ditentukan oleh konvensi pemanggilan metode — sekali lagi, ini akan dijelaskan nanti.

Saat definisi class dimasukkan, namespace baru dibuat, dan digunakan sebagai cakupan lokal — jadi, semua penugasan ke variabel lokal masuk ke namespace baru ini. Secara khusus, definisi fungsi mengikat nama fungsi baru di sini.

### 9.3.2 Class Object

Referensi atribut menggunakan sintaks standar yang digunakan untuk semua referensi atribut di Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di ruang nama kelas saat objek kelas dibuat. Jadi, jika definisi kelas terlihat seperti ini:

```Python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

Instansiasi kelas menggunakan notasi fungsi. Anggap saja objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. Misalnya (dengan asumsi kelas di atas):

```Python
x = MyClass()
```

Operasi instantiasi ("memanggil" objek kelas) membuat objek kosong. Banyak kelas suka membuat objek dengan instance yang disesuaikan dengan keadaan awal tertentu. Oleh karena itu kelas dapat mendefinisikan metode khusus bernama **init**(), seperti ini:

```Python
def __init__(self):
    self.data = []
```

Saat kelas mendefinisikan metode **init**() , instantiasi kelas secara otomatis memanggil **init**() untuk instance kelas yang baru dibuat. Jadi dalam contoh ini, instance baru yang diinisialisasi dapat diperoleh dengan:

```Python
x = MyClass()
```

Tentu saja, metode **init**() mungkin memiliki argumen untuk fleksibilitas yang lebih besar. Dalam hal ini, argumen yang diberikan kepada operator instansiasi kelas diteruskan ke **init**(). Misalnya,

```Python
>>> class Complex:
...    def __init__(self, realpart, imagpart):
...        self.r = realpart
...        self.i = imagpart

>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

### 9.3.3 Instance Objects

Ada dua jenis nama atribut yang valid: atribut data dan metode.

atribut data sesuai dengan "variabel instan" di Smalltalk, dan dengan "anggota data" di C++. Atribut data tidak perlu dideklarasikan; seperti variabel lokal, mereka muncul saat pertama kali ditugaskan. Misalnya, jika x adalah turunan dari MyClass yang dibuat di atas, potongan kode berikut akan mencetak nilai 16, tanpa meninggalkan jejak:

```Python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

### 9.3.4 Method Objects

Biasanya, sebuah metode dipanggil tepat setelah terikat:

```Python
x.f()
```

Dalam contoh MyClass, ini akan mengembalikan string 'hello world'. Namun, tidak perlu langsung memanggil metode: x.f adalah objek metode, dan dapat disimpan dan dipanggil di lain waktu. Misalnya:

```Python
xf = x.f
while True:
    print(xf())
```

### 9.3.5 Class and Instance Variables

```Python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```

```Python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

```Python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

## 9.4 Random Remarks

Jika nama atribut yang sama muncul di kedua instance dan di kelas, maka pencarian atribut akan memprioritaskan instance tersebut:

```Python
>>> class Warehouse:
...   purpose = 'storage'
...   region = 'west'
...
>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```

Objek fungsi apa pun yang merupakan atribut kelas menentukan metode untuk instance kelas itu. Definisi fungsi tidak perlu dilampirkan secara tekstual dalam definisi kelas: menugaskan objek fungsi ke variabel lokal di kelas juga boleh. Misalnya:

```Python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

Metode dapat memanggil metode lain dengan menggunakan atribut metode dari argumen diri:

```Python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

Nama BaseClassName harus didefinisikan dalam ruang lingkup yang berisi definisi kelas turunan. Di tempat nama kelas dasar, ekspresi sewenang-wenang lainnya juga diperbolehkan. Ini bisa berguna, misalnya, ketika kelas dasar didefinisikan dalam modul lain:

```Python
class DerivedClassName(modname.BaseClassName):
```

# 9.6 Private Variables

Name mangling sangat membantu untuk membiarkan subclass menimpa metode tanpa memutuskan panggilan metode intraclass. Misalnya:

```Python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

Contoh di atas akan berfungsi bahkan jika MappingSubclass akan memperkenalkan pengenal **update karena diganti dengan \_Mapping**update di kelas Mapping dan \_MappingSubclass\_\_update di kelas MappingSubclass.

## 9.7 Odds and Ends

```Python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int
```

```Python
>>> john = Employee('john', 'computer lab', 1000)
>>> john.dept
'computer lab'
>>> john.salary
1000
```

## 9.8 Iterators

Sekarang Anda mungkin telah memperhatikan bahwa sebagian besar objek kontainer dapat di-loop menggunakan pernyataan for:

```Python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

Gaya akses ini jelas, ringkas, dan nyaman. Penggunaan iterator meliputi dan menyatukan Python. Di belakang layar, pernyataan for memanggil iter() pada objek kontainer. Fungsi mengembalikan objek iterator yang mendefinisikan metode **next**() yang mengakses elemen dalam wadah satu per satu. Ketika tidak ada lagi elemen, **next**() memunculkan pengecualian StopIteration yang memberi tahu for loop untuk diakhiri. Anda dapat memanggil metode **next**() menggunakan fungsi bawaan next() ; contoh ini menunjukkan cara kerjanya:

```Python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

## 9.9 Generators

Generator adalah alat yang sederhana dan kuat untuk membuat iterator. Mereka ditulis seperti fungsi biasa tetapi menggunakan pernyataan hasil kapan pun mereka ingin mengembalikan data. Setiap kali next() dipanggil, generator melanjutkan di mana ia tinggalkan (ia mengingat semua nilai data dan pernyataan mana yang terakhir dieksekusi). Contoh menunjukkan bahwa generator dapat dengan mudah dibuat:

```Python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```

```Python
>>> for char in reverse('golf'):
...    print(char)
...
f
l
o
g
```

## 9.10 Generator Expressions

Beberapa generator sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaks yang mirip dengan pemahaman daftar tetapi dengan tanda kurung, bukan tanda kurung siku. Ekspresi ini dirancang untuk situasi di mana generator langsung digunakan oleh fungsi penutup. Ekspresi generator lebih kompak tetapi kurang fleksibel daripada definisi generator lengkap dan cenderung lebih ramah memori daripada pemahaman daftar yang setara.

Contoh:

```Python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>>     valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```
