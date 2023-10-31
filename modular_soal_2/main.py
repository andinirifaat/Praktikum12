from menu import menu
from persegi import persegi
from luas_lingkaran import lingkaran as l
import segitiga

def main():
    while True:
        menu()
        pilihan = input("Silakan masukkan nomor bentuk yang dipilih: ")
        
        if pilihan == "1":
            persegi()
        elif pilihan == "2":
            l()
        elif pilihan == "3":
            segitiga.segitiga()
        elif pilihan == "4":
            exit()
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()
