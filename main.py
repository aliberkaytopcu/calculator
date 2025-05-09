from sympy import symbols, diff, integrate, sympify, sin, cos, tan, exp, ln
from sympy.abc import x
import sys

def main():
    print("----- Python Matematik Hesap Makinesi -----")
    print("Komutlar: türev, integral, alan, hesapla, çıkış")
    
    while True:
        komut = input("\nKomut girin: ").strip().lower()
        
        if komut == "türev":
            ifade = input("Türevini almak istediğiniz ifadeyi girin (x türünden): ")
            try:
                f = sympify(ifade)
                print("Türev:", diff(f, x))
            except:
                print("Hatalı ifade!")

        elif komut == "integral":
            ifade = input("İntegralini almak istediğiniz ifadeyi girin (x türünden): ")
            tur = input("Belirli mi? (e/h): ").strip().lower()
            try:
                f = sympify(ifade)
                if tur == 'e':
                    a = float(input("Alt sınır: "))
                    b = float(input("Üst sınır: "))
                    print("Belirli integral:", integrate(f, (x, a, b)))
                else:
                    print("Belirsiz integral:", integrate(f, x))
            except:
                print("Hatalı ifade!")

        elif komut == "alan":
            ifade = input("Alanını hesaplamak istediğiniz fonksiyonu girin (x türünden): ")
            try:
                a = float(input("Alt sınır: "))
                b = float(input("Üst sınır: "))
                f = sympify(ifade)
                alan = integrate(abs(f), (x, a, b))
                print("Alan:", alan)
            except:
                print("Hatalı ifade!")

        elif komut == "hesapla":
            ifade = input("Hesaplanacak matematiksel ifadeyi girin: ")
            try:
                sonuc = sympify(ifade).evalf()
                print("Sonuç:", sonuc)
            except:
                print("Hatalı ifade!")

        elif komut == "çıkış":
            print("Çıkılıyor...")
            sys.exit()

        else:
            print("Bilinmeyen komut!")

if __name__ == "__main__":
    main()
