# Minggu 8 - Pustaka Standar

## 10. Tur Singkat Pustaka Standar

### 10.1 Operating System Interface

Modul os menyediakan lusinan fungsi untuk berinteraksi dengan sistem operasi:

```Python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python311'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```

Pastikan untuk menggunakan gaya import os daripada from os import \*. Ini akan menjaga os.open() membayangi fungsi built-in open() yang beroperasi jauh berbeda.

Fungsi built-in dir() dan help() berguna sebagai bantuan interaktif untuk bekerja dengan modul besar seperti os:

```Python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```

Untuk tugas manajemen file dan direktori harian, modul shutil menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan:

```Python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

### 10.2 File Wildcard

Modul glob menyediakan fungsi untuk membuat daftar file dari pencarian wildcard direktori:

```Python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

### 10.3 Command Line Arguments

Skrip utilitas umum sering perlu memproses argumen baris perintah. Argumen ini disimpan dalam atribut argv modul sys sebagai daftar. Misalnya, hasil keluaran berikut dari menjalankan python demo.py satu dua tiga di baris perintah:

```Python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```

Modul argparse menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah.

```Python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```

### 10.4 Error Output Redirection and Program Termination

Modul sys juga memiliki atribut untuk stdin, stdout, dan stderr.

```Python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

Cara paling cepat untuk mengakhiri skrip adalah dengan menggunakan sys.exit().

### 10.5 String Pattern Matching

Modul re menyediakan alat ekspresi reguler untuk pemrosesan string tingkat lanjut. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi ringkas dan optimal:

```Python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena lebih mudah dibaca dan di-debug:

```Python
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```

### 10.6 Mathematics

Modul matematika memberikan akses ke fungsi perpustakaan C yang mendasari untuk matematika floating point:

```Python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```

Modul random menyediakan alat untuk membuat pilihan acak:

```Python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```

Modul statistik menghitung properti statistik dasar (rata-rata, median, varians, dll.) dari data numerik:

```Python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

### 10.7 Internet Access

Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah urllib.request untuk mengambil data dari URL dan smtplib untuk mengirim email:

```Python
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline

datetime: 2022-01-01T01:36:47.689215+00:00

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()
```

### 10.8 Dates and Times

Modul datetime menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks.

```Python
# dates are easily constructed and formatted
from datetime import date
now = date.today()
now
datetime.date(2003, 12, 2)
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days
14368
```

### 10.9 Data Compression

Pengarsipan data umum dan format kompresi didukung langsung oleh modul termasuk: zlib, gzip, bz2, lzma, zipfile dan tarfile.

```Python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

### 10.10 Performance Measurement

Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari berbagai pendekatan untuk masalah yang sama.Phython menyediakan alat pengukuran yang segera menjawab pertanyaan tersebut.

```Python
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```

### 10.11 Quality Controll

Salah satu pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah dengan menulis tes untuk setiap fungsi saat dikembangkan dan sering menjalankan tes tersebut selama proses pengembangan.

```Python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```

Modul unittest tidak semudah modul doctest, tetapi memungkinkan serangkaian pengujian yang lebih komprehensif untuk dipertahankan dalam file terpisah:

```Python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```

### 10.12 Batteries Included

Python memiliki filosofi "termasuk baterai". Ini paling baik dilihat melalui kemampuan canggih dan kuat dari paket yang lebih besar. Misalnya:

- Modul xmlrpc.client dan xmlrpc.server membuat penerapan panggilan prosedur jarak jauh menjadi tugas yang hampir sepele Terlepas dari nama modulnya, tidak diperlukan pengetahuan langsung atau penanganan XML.

- Paket email adalah pustaka untuk mengelola pesan email, termasuk MIME dan dokumen pesan berbasis RFC 2822. Tidak seperti smtplib dan poplib yang benar-benar mengirim dan menerima pesan, paket email memiliki perangkat lengkap untuk membuat atau mendekode struktur pesan yang kompleks (termasuk lampiran ) dan untuk mengimplementasikan penyandian internet dan protokol header.

- Paket json memberikan dukungan kuat untuk mem-parsing format pertukaran data yang populer ini. Modul csv mendukung pembacaan dan penulisan file secara langsung dalam format Comma-Separated Value, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh xml.etree.ElementTree, Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.

- Modul sqlite3 adalah pembungkus untuk perpustakaan database SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.

- Internasionalisasi didukung oleh sejumlah modul termasuk gettext, locale, dan paket codec.

## 11. Brief Tour of Standard Library - Part II

### 11.1 Output Formatting

```Python
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

```Python
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```

```Python
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```

```Python
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
locale.format("%d", x, grouping=True)
'1,234,567'
locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)
'$1,234,567.80
```

### 11.2 Templating

```Python
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

### 11.3 Working With Binary Data Record Layouts

Modul struct menyediakan fungsi pack() dan unpack() untuk bekerja dengan format rekaman biner dengan panjang variabel. Contoh berikut menunjukkan cara mengulang informasi header dalam file ZIP tanpa menggunakan modul zipfile. Kode paket "H" dan "I" "<" menunjukkan bahwa ukurannya standar dan dalam urutan byte little-endian:

```Python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```

### 11.4 Multi-threading

Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Thread dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima input pengguna saat tugas lain berjalan di latar belakang. Kasus penggunaan terkait menjalankan I/O secara paralel dengan komputasi di komputer lain benang.

Kode berikut menunjukkan bagaimana modul threading tingkat tinggi dapat menjalankan tugas di latar belakang sementara program utama terus berjalan:

```Python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

### 11.5 Logging

Modul logging menawarkan fitur lengkap dan sistem logging yang fleksibel.Sederhananya, pesan log dikirim ke file atau ke sys.stderr:

```Python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

### 11.6 Weak References

Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus).

```Python
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']                # fetch the object if it is still alive
10
del a                       # remove the one reference
gc.collect()                # run garbage collection right away
0
d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python311/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

### 11.7 Tools for Working with Lists

Banyak kebutuhan struktur data dapat dipenuhi dengan tipe daftar bawaan.

```Python
from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
26932
a[1:3]
array('H', [10, 700])
```

### 11.8 Decimal Floating Point Arithmetic

Modul desimal menawarkan tipe data Desimal untuk aritmatika floating point desimal Dibandingkan dengan implementasi float built-in dari floating point biner, kelas ini sangat membantu untuk

- aplikasi keuangan dan penggunaan lain yang membutuhkan representasi desimal yang tepat,

- kontrol atas presisi,

- kontrol atas pembulatan untuk memenuhi persyaratan hukum atau peraturan,

- pelacakan tempat desimal yang signifikan, atau

- aplikasi di mana pengguna mengharapkan hasil untuk mencocokkan perhitungan yang dilakukan dengan tangan.

```Python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```
