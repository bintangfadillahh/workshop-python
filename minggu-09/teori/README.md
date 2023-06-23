# Minggu 9 - Virtual Environment dan Package Manager

## 12. Virtual Environments And Packages

### 12.1 Introduction

Aplikasi Python akan sering menggunakan paket dan modul yang tidak disertakan sebagai bagian dari pustaka standar. Aplikasi kadang-kadang membutuhkan versi perpustakaan tertentu, karena aplikasi mungkin memerlukan bug tertentu yang telah diperbaiki atau aplikasi mungkin ditulis menggunakan versi usang dari antarmuka perpustakaan.

Ini berarti tidak mungkin satu instalasi Python memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratan tersebut bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah membuat lingkungan virtual, pohon direktori mandiri yang berisi instalasi Python untuk versi Python tertentu, ditambah sejumlah paket tambahan.

### 12.2 Creating Virtual Environments

Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut venv. venv biasanya akan menginstal versi Python terbaru yang Anda miliki. Jika Anda memiliki beberapa versi Python di sistem Anda, Anda dapat memilih versi Python tertentu dengan menjalankan python3 atau versi apa pun yang Anda inginkan.

Untuk membuat lingkungan virtual, tentukan direktori tempat Anda ingin meletakkannya, dan jalankan modul venv sebagai skrip dengan jalur direktori:

```
python -m venv tutorial-env
```

Ini akan membuat direktori tutorial-env jika tidak ada, dan juga membuat direktori di dalamnya yang berisi salinan interpreter Python dan berbagai file pendukung.

Lokasi direktori umum untuk lingkungan virtual adalah .venv. Nama ini membuat direktori biasanya tersembunyi di shell Anda dan dengan demikian menyingkir sambil memberinya nama yang menjelaskan mengapa direktori itu ada. Itu juga mencegah bentrok dengan file definisi variabel lingkungan .env yang didukung beberapa perkakas.

Setelah Anda membuat lingkungan virtual, Anda dapat mengaktifkannya.

Di Windows, jalankan:

```
tutorial-env\Scripts\activate.bat
```

Mengaktifkan lingkungan virtual akan mengubah prompt shell Anda untuk menunjukkan lingkungan virtual apa yang Anda gunakan, dan memodifikasi lingkungan sehingga menjalankan python akan memberi Anda versi dan pemasangan Python tertentu. Misalnya:

```Python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

### 12.3 Managing Packages wit pip

Anda dapat menginstal, memutakhirkan, dan menghapus paket menggunakan program bernama pip. Secara default pip akan menginstal paket dari Python Package Index. Anda dapat menelusuri Indeks Paket Python dengan membukanya di browser web Anda.

pip memiliki sejumlah subperintah: "install", "uninstall", "freeze", dll. (Lihat panduan Memasang Modul Python untuk dokumentasi lengkap untuk pip.)

Anda dapat menginstal versi terbaru dari sebuah paket dengan menentukan nama paket:

```Python
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

python -m pip uninstall diikuti oleh satu atau lebih nama paket akan menghapus paket dari lingkungan virtual.

python -m pip show akan menampilkan informasi tentang paket tertentu

```
(tutorial-env) $ python -m pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```

python -m pip list akan menampilkan semua paket yang diinstal di lingkungan virtual

```
(tutorial-env) $ python -m pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

python -m pip freeze akan menghasilkan daftar serupa dari paket yang diinstal, tetapi hasilnya menggunakan format yang diharapkan oleh python -m pip install. Konvensi umum adalah meletakkan daftar ini di file requirements.txt

```
(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

Requirement.txt kemudian dapat dikomit ke kontrol versi dan dikirimkan sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan install -r

```
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```

## Getting Started with Conda

### Managing Conda

Verifikasi bahwa conda diinstal dan dijalankan di sistem Anda dengan mengetik:

```
conda --version
```

Perbarui conda ke versi saat ini. Ketik berikut ini:

```
conda update conda
```

Conda membandingkan versi dan kemudian menampilkan apa yang tersedia untuk diinstal.

Jika versi conda yang lebih baru tersedia, ketik y untuk memperbarui:

```
Proceed ([y]/n)? y
```

### Managing Environment

Buat lingkungan baru dan instal paket di dalamnya.

Kami akan memberi nama kepingan salju lingkungan dan menginstal paket BioPython. Di Anaconda Prompt atau di jendela terminal Anda, ketik berikut ini:

```
conda create --name snowflakes biopython
```

Untuk melihat daftar semua lingkungan Anda, ketik:

```
conda info --envs
```

Daftar lingkungan muncul, mirip dengan berikut ini:

```
conda environments:

    base           /home/username/Anaconda3
    snowflakes   * /home/username/Anaconda3/envs/snowflakes
```

### Managing python

Buat lingkungan baru bernama "ular" yang berisi Python 3.9:

```
conda create --name snakes python=3.9
```

### Managing packages

Untuk menemukan paket yang telah Anda instal, aktifkan terlebih dahulu lingkungan yang ingin Anda cari. Lihat di atas untuk perintah untuk mengaktifkan lingkungan ular Anda.

Periksa untuk melihat apakah paket yang belum Anda instal bernama "beautifulsoup4" tersedia dari repositori Anaconda (harus terhubung ke Internet):

Instal paket ini ke lingkungan saat ini:

```
conda search beautifulsoup4

conda install beautifulsoup4
```

Untuk menampilkan list yang terinstall :

```
conda list
```
