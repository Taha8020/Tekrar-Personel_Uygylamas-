def hazir_personeller():
    # Hazır personel listemiz (Yaş bilgisi de eklendi)
    personel_listesi = [
        {"isim": "Ali", "soyisim": "Yılmaz", "departman": "IT", "maas": 5000,"yas": 30},
        {"isim": "Ebru", "soyisim": "Kara", "departman": "HR", "maas": 4500,"yas": 28},
        {"isim": "Mehmet", "soyisim": "Demir", "departman": "Finance", "maas": 6000,"yas": 35},
        {"isim": "Elif", "soyisim": "Çelik", "departman": "Marketing", "maas": 4800,"yas": 26},
        {"isim": "Can", "soyisim": "Öztürk", "departman": "Sales", "maas": 5200,"yas": 32}
    ]
                
    
    return personel_listesi

def personel_ekle(mevcut_liste):
    while True:
        try:
            girilecek_personel_sayisi = int(input("Kaç personel eklemek istiyorsunuz? "))
            break
        except ValueError:
            print("Hatalı giriş! Lütfen bir sayı giriniz.")
            
    for i in range(girilecek_personel_sayisi):
        print(f"\n--- {i+1}. Personel ---")
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")
        departman = input("Departman: ")
        
        while True:
            try:
                maas = float(input("Maaş: "))
                break
            except ValueError:
                print("Hatalı giriş! Lütfen maaşı sayı olarak giriniz.")
                
        while True:
            try:
                yas = int(input("Yaş: "))
                break
            except ValueError:
                print("Hatalı giriş! Lütfen yaşı tam sayı olarak giriniz.")
                
        yeni_personel = {
            "isim": isim,
            "soyisim": soyisim,
            "departman": departman,
            "maas": maas,
            "yas": yas
        }
        mevcut_liste.append(yeni_personel)
        print(f"Başarıyla eklendi: {isim} {soyisim}")
    
    return mevcut_liste

def giris():
    # Program ilk açıldığında hazır listeyi yüklüyoruz
    ana_liste = hazir_personeller()

    while True:
        print("\n----- Personel Kayıt Sistemi -----")
        print("1. Hazır ve Eklenen Personelleri Görüntüle")
        print("2. Yeni Personel Ekle")
        print("3. Çıkış")
        
        secim = input("Lütfen bir seçenek giriniz (1-2-3): ").strip()
        
        if secim == "1":
            print("\n--- Personel Listesi ---")
            for sira, p in enumerate(ana_liste, 1):
                print(f"{sira}. İsim: {p['isim']} {p['soyisim']} | Departman: {p['departman']} | Yaş: {p['yas']} | Maaş: {p['maas']}")
                
        elif secim == "2":
            # Yeni eklenenleri ana listeye dahil ediyoruz
            ana_liste = personel_ekle(ana_liste)
            
            # İstediğin o "bittiğinde görmek ister misin?" sorusu:
            gorme_istegi = input("\nKayıt işlemi tamamlandı. Güncel listeyi şimdi görmek ister misiniz? (E/H): ").strip().upper()
            if gorme_istegi == 'E':
                print("\n--- Güncel Personel Listesi ---")
                for sira, p in enumerate(ana_liste, 1):
                    print(f"{sira}. İsim: {p['isim']} {p['soyisim']} | Departman: {p['departman']} | Yaş: {p['yas']} | Maaş: {p['maas']}")
                    
        elif secim == "3":
            print("Sistemden çıkılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim! Lütfen 1, 2 veya 3 girin.")

if __name__ == "__main__":
    giris()