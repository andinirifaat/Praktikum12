
def persegi():
    print("Menghitung Luas Persegi Panjang")
    p = int(input("Masukkan Panjang :" )) 
    l = int(input("Masukkan Lebar :" ))
    luas = p * l #operasi mencari luas
    print ("Luas Persegi Panjang adalah" ,luas)
    print ()
    print ("Coba lagi [Y/N]? ") 
    back = input().upper()
    if back == "Y":
        import menu
        menu.menu() 
    else:
        exit() 



#memperbaiki sintaksis kutip
#kurang lengkapnya tanda kurung
#belum ditambahkan int didepan input
#tadi belum diimport + menu.menu belum
 #mennganti raw_inputr jadi input
 #indentansi