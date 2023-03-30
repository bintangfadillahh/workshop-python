# 4. Pengendali Aliran Data

> Selain while statement yang sudah dikenalkan, Python menggunakan flow control statement yang juga dikenal di bahasa lain, tetapi dengan sedikit perbedaan

## 4.1 If Statement

> Contoh If Statement :

```Python
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```

> Bagian **elif** bisa kosong atau lebih, dan bagian **else** opsional. Keyword 'elif' adalah singkatan dari 'else if', dan itu berguna untuk menghindari indent yang berlebihan. Sebuah urutan if...elif...else adalah pengganti dari switch or case yang ditemukan di bahasa lain bahasa lain

## 4.2 For Statement

> Statement **for** di Python sedikit berbeda dengan yang biasa digunakan pada C atau Pascal. Daripada menggunakan iterasi aritmatika, atau memberi user kemampuan untuk mendefinisikan langkah iterasi dan kondisi berhenti, 'for' dalam Python melakukan iterasi pada item

```Python
# Measure some string
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

```Python
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

## 4.3 The range() function

> Jika kau perlu melakukan iterasi menggunakan urutan angka, maka built-in function **range()** sangat berguna.

```Python
for i range(5):
...   print(i)
...
0
1
2
3
4
```

> Kita juga dapat mendefinisikan angka awal dari range

```Python
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]

>>> list(range(-10, -100, -30))
[-10, -40, -70]
```

> Untuk mengiterasikan indeks, kita bisa menggabungkan **range()** dan **len()** :

```Python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```

> Hal aneh akan terjadi jika kita print sebuah range :

```Python
>>> range(10)
range(0, 10)
```

> Kita juga dapat menggabungkan **sum()** dan **range()**

```Python
>>> sum(range(4)) # 0 + 1 + 2 + 3
6
```

## 4.4 Break and Continue Statement, and else Clauses on Loops

> Break statement, seperti pada C, melakukan break pada loop **for** atau **while**

```Python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

> Else clause dimiliki oleh **for** loop, bukan **if** statement

> **Continue** statement, juga sama dengan C

```Python
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```

## 4.5 Pass Statement

> Pass Statement tidak melakukan apapun. Dapat digunakan saat program memerlukan syntactically tetapi tidak memerlukan action, sebagai contoh :

```Python
>>> while true:
        pass  # Busy-wait for keyboard interrupt (Ctrl+C)
```

> Biasanya digunakan untuk membuat class minimal :

```Python
>>> class MyEmptyClass:
        pass
```

> Tempat lain **pass** dapat digunakan adalah sebagai pengganti untuk function atau conditional body ketika mengerjakan code baru, sehingga kita dapat berpikir pada tingkatan abstrak.

```Python
>>> def initlog(*args):
        pass   # Remember to implement this!
```

## 4.6 Match Statement

> Sebuah **Match Statement** mengambil expression dan membandingkan nilainya dengan pola berurutan sebagai satu atau beberapa case blocks. Secara kasar mirip dengan switch statement pada C, Java atau Javascript, tetapi lebih mirip dengan pattern matching di bahasa Rust atau Haskell. Hanya pola pertama yang sesuai dieksekusi dan dapat mengekstrak komponen dari value ke dalam variabel

> Bentuk paling sederhana membandingkan nilai subject terhadap satu atau lebih literal

```Python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

> Kita dapat menggabungkan beberapa literal dalam satu pola menggunakan | ("or"):

```Python
case 401 | 403 | 404:
    return "Not Allowed"
```

> Pola dapat terlihat seperti unpacking, dan dapat digunakan untuk mengikat variabel:

```Python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

> Jika Anda menggunakan class untuk menyusun data, Anda dapat menggunakan nama kelas diikuti dengan daftar argumen yang menyerupai konstruktor, tetapi dengan kemampuan untuk menangkap atribut ke dalam variabel:

```Python
7/-class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

```Python
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
```

4.7 Defining Function

> Kita dapat membuat function yang menuliskan deret Fibonacci ke batas arbiter :

```Python
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

> Kata kunci def memperkenalkan definisi function. Itu harus diikuti oleh nama function dan daftar parameter formal yang dikurung. Pernyataan yang membentuk isi function dimulai dari baris berikutnya, dan harus diberi indentasi.

> Nama lain juga dapat menunjuk ke objek function yang sama dan juga dapat digunakan untuk mengakses function tersebut:

```Python
>>> fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```

> Sangat mudah untuk menulis function yang mengembalikan daftar angka deret Fibonacci, alih-alih mencetaknya:

```Python
>>> def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
