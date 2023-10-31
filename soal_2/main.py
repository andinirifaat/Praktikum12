from package_s2.menu import menu
from package_s2.luas_segitiga import segitiga
from package_s2.luas_lingkaran import lingkaran
from package_s2.luas_persegi_panjang import persegi

def main():
    while True:
        print("Pilih Bentuk 2D")
        print()
        print("1. Persegi Panjang")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("4. Keluar")
        
        pilihan = input("Silakan masukkan nomor bentuk yang dipilih: ")
        
        if pilihan == "1":
            persegi()
        elif pilihan == "2":
            lingkaran()
        elif pilihan == "3":
            segitiga()
        elif pilihan == "4":
            exit()
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()
