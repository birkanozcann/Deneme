# Gelir ve gider değerlerini kullanıcıdan alıyoruz
gelir = float(input("Toplam gelirinizi girin (TL): "))
gider = float(input("Toplam giderinizi girin (TL): "))

# Kar/Zarar hesaplaması
net_kar = gelir - gider

# Sonucu ekrana yazdırma
if net_kar > 0:
    print(f"Karınız: {net_kar} TL")
elif net_kar < 0:
    print(f"Zararınız: {abs(net_kar)} TL")
else:
    print("Ne kar ne zarar ettiniz (Başa baş noktası).")