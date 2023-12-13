def todo_list():
    icerik= []

    while True:
        print("\nTo Do LIST")
        print("1. Gorev ekle")
        print("2. Gorevleri Listele")
        print("3. Gorevleri Sil")
        print("4. Cikis")

        secim = input("Seciminizi yapiniz:")

        if secim =='1':
            metin = input("Eklemek istediginiz gorevi girin: ")
            icerik.append(metin)
            print("Gorev eklendi.")

        elif secim == '2':
            print("Gorevler:\n")
            if not icerik:
                print("Gosterilecek icerik bulunamiyor.")
            else:
                for index, metin in enumerate(icerik,start=1):
                    print(f"{index} . {metin}")

        elif secim == '3':
            if not icerik:
                print("Silinecek icerik bulunamiyor.")
            else:
                print("\nSilinecek Gorevler:")
                for index, metin in enumerate(icerik,start=1):
                    print(f"{index} . {metin}")

                metin_index = int(input("Silmek istediginiz gorevin numarasini girin:"))

                if 1 <= metin_index <= len(icerik):
                    silinen_metin = icerik.pop(metin_index-1)
                    print(f"{silinen_metin} gorevi silindi.")
                else:
                    print("Gecersiz gorev numarasi.")

        elif secim == '4':
            print("Programdan cikiliyor.")
            break
        else:
            print("Gecersiz secenek.Lutfen tekrar giriniz.")
            


if __name__ == "__main__":
    todo_list()




