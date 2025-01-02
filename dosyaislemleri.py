import time
global urunler

def urunekle(adet):
    for i in range(adet):
        urunkod = int(input(f"{i+1}. ürünün kodunu giriniz: "))
        urunad= input(f"{i+1}. ürünün adını giriniz: ")
        urunmiktar= int(input(f"{i+1}. ürünün miktarını giriniz: "))
        urunmaliyet= float(input(f"{i+1}. ürünün maliyetini giriniz: "))
        urunsatis= float(input(f"{i+1}. ürünün satış miktarını giriniz: "))
        print("-------------------")
        with open("20010011049.txt","a",encoding="utf-8") as dosya:
            dosya.write("{}-{}-{}-{}-{}-\n".format(urunkod,urunad,urunmiktar,urunmaliyet,urunsatis))

def urunlistele():
    global urunler
    for key,value in urunler.items():
        print(key+" kodlu ürünün",end=" ")
        for k,v in value.items():
            print("'{}': {} ".format(k,v),end="")
        print("")

def urunguncelle(kod):
    def dosyayayaz():
        #urunler sözlüğündeki key ile kod eşleşirse güncel bilgiler dosyaya yazılacak
        with open("20010011049.txt", "w", encoding="utf-8") as file:
            for key, v in urunler.items():
                file.write(key + "-")
                for x in v.values():
                    i=str(x)
                    file.write(i + "-")
                file.write("\n")
    global urunler
    kontrol=0
    for key,value in urunler.items():
        if key == kod:
            ad= input("Güncellenecek ürünün yeni adı: ")
            miktar= int(input("Güncellenecek ürünün yeni miktarı: "))
            maliyet= float(input("Güncellenecek ürünün yeni maliyeti: "))
            satis= float(input("Güncellenecek ürünün yeni satış fiyatı: "))
            value["adı"] = ad
            value["adedi"] = miktar
            value["maliyeti"] = maliyet
            value["satış fiyatı"] = satis
            kontrol=1

    if kontrol==1:
        dosyayayaz()
        print("Ürün güncellendi. Menüye dönülüyor...")

    if kontrol==0:
        print("Aranan koda sahip ürün bulunamadı. Menüye dönülüyor...")



def urunara(kod):
    global urunler
    kontrol=0
    for key,value in urunler.items():
        if key==kod:
            kontrol=1
            print(key + " kodlu ürünün", end=" ")
            for k, v in value.items():
                print("'{}': {} ".format(k, v), end="")
            print("")

    if kontrol==0:
        print("Aranan koda sahip ürün bulunamadı. Menüye dönülüyor...")



def urunsil(kod):
    global urunler
    kntrl=0
    for keys in urunler.keys():
        if keys==kod:
            kntrl=1
            tut=keys
    if kntrl==1:
        urunler.pop(tut)
        #ürünler sözlüğündeki key ve girilen kod eşleştikten sonra sözlükten o bölüm siliniyor
        with open("20010011049.txt","w",encoding="utf-8") as file:
            #istenilen ürün silindikten sonra güncel sözlük dosyaya aktarılıyor
            for key,v in urunler.items():
                file.write(key+"-")
                for i in v.values():
                    file.write(i+"-")
                file.write("\n")
        print("Ürün silindi. Menüye dönülüyor...")

    if kntrl==0:
        print("Aranan koda sahip ürün bulunamadı. Menüye dönülüyor...")


def karhesapla(durum):
    liste=[]
    toplamkar=0
    for key,value in urunler.items():
        satis = float(value["satış fiyatı"])
        alis = float(value["maliyeti"])
        miktar= int(value["adedi"])
        kar= satis-alis
        yenikar= kar*miktar
        tuple=(key,kar,yenikar)
        liste.append(tuple)
        toplamkar+=yenikar
    # kâr bilgilerinin tutulduğu bir dosyaya liste içindeki tuplelar yazılıyor
    with open("20010011049_kar.txt","w",encoding="utf-8") as d:
        for demetler in liste:
            d.write("{} kodlu ürünün -> 1 adette kârı: {:.2f} -> toplam kârı: {:.2f}".format(demetler[0],float(demetler[1]),float(demetler[2])))
            d.write("\n")
        d.write("Toplam kâr: {:.2f}".format(toplamkar))

    def karyaz():
        for i in liste:
            print("{} nolu ürün için --> 1 adetteki kârınız: {:.2f} --> toplam adetteki kârınız: {:.2f}".format(i[0],i[1],i[2]))
        print("Toplam kârınız: {:.2f}".format(toplamkar))
    if durum:
        karyaz()

def menu():
    global urunler
    while True:
        print("\n--------PASTANE STOK TAKİP OTOMASYONU--------")
        print("1-Ürün Ekle\n2-Ürün Güncelle\n3-Ürünü Sil\n4-Stoğu Görüntüle\n5-Kar Hesapla\n6-Ürün Ara\n7-Programdan Çık")

        while True:
            print("-------------------")
            secim = input("Seçiminizi giriniz: ")

            urunler = {}
            #her menüye dönüşte dosya okunup sözlük içinde sözlüğe aktarılıyor
            with open("20010011049.txt", "r", encoding="utf-8") as dosyaoku:
                satirlar = dosyaoku.readlines()
                if satirlar!="\n":
                    for i in satirlar:
                        bilgiler = {}
                        satir = i.split("-")
                        satir.pop()
                        bilgiler["adı"] = satir[1]
                        bilgiler["adedi"] = satir[2]
                        bilgiler["maliyeti"] = satir[3]
                        bilgiler["satış fiyatı"] = satir[4]
                        urunler[satir[0]] = bilgiler

            if secim=="1":
                print("----ÜRÜN EKLEME----")
                adet = int(input("Kaç farklı ürün eklenecek? "))
                print("-------------------")
                urunekle(adet)
                print("Başarıyla eklendi. Menüye dönülüyor...")
                time.sleep(2)
                break

            elif secim=="2":
                print("----ÜRÜN GÜNCELLEME----")
                kod = input("Güncellenecek ürünün kodunu giriniz: ")
                print("-------------------")
                urunguncelle(kod)
                time.sleep(2)
                break

            elif secim == "3":
                print("----ÜRÜN SİLME----")
                kod = input("Silmek istediğiniz ürünün kodunu giriniz: ")
                print("-------------------")
                urunsil(kod)
                time.sleep(2)
                break

            elif secim=="4":
                print("----ÜRÜN LİSTELEME----")
                urunlistele()
                break

            elif secim=="5":
                print("----KAR HESAPLAMA----")
                karhesapla(True)
                break

            elif secim=="6":
                print("----ÜRÜN ARAMA----")
                kod = input("Aradığınız ürünün kodunu giriniz: ")
                urunara(kod)
                time.sleep(2)
                break

            elif secim=="7":
                # programdan çıkmadan önce kar bilgilerini içeren dosyayı güncellemeli
                karhesapla(False)
                break
            else:
                print("Hatalı seçim. Tekrar deneyiniz.")

        if secim=="7":
            print("Program sonlandı.")
            exit()

menu()