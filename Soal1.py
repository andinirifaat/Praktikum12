# import module matematika math
import math
# Input koefisien dari keyboard
a = int(input('Masukkan a: '))
b = int(input("Masukkan b: "))
c = int(input('Masukkan c: '))
# hitung diskriminan d
d = (b**2) - (4*a*c)
#percabangan jika nilai kecil Tu besar de 0
if d < 0:
    print("Tidak ada akar real")
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Akar 1:", x1)
    print("Akar 2:", x2)