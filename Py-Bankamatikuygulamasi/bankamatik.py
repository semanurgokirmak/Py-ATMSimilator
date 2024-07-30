a = int(input("Paranız: "))


b = int(input("Lütfen bir işlem seçiniz:\n1-Bakiye sorgulama\n2-Para Yatırma\n3-Para Çekme\n4-Çıkış\n"))

if b == 1:
    print("Anlık Bakiyeniz:", a)

elif b == 2:
    
    yatirilan_para = int(input("Ne kadar para yatırmak istersiniz? "))
    a += yatirilan_para
    print("Yeni Bakiyeniz:", a)

elif b == 3:
    
    cekilen_para = int(input("Ne kadar para çekmek istersiniz? "))
    if cekilen_para <= a:
        a -= cekilen_para
        print("Yeni Bakiyeniz:", a)
    else:
        print("Hesabınızdaki tutardan fazla para çekmeye çalıştınız, lütfen yeniden deneyin.")

elif b == 4:
    print("Görüşürüz...")

else:
    print("Geçersiz işlem seçimi. Lütfen geçerli bir seçenek giriniz.")
