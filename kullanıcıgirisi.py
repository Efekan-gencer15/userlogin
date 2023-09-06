print(
    """
********************
KULLANICI GİRİŞİ
********************"""
)


sys_kul_adı = "efekan"
sys_parola = "12345"

giriş_hakkı = 3

while True:
    kullanıcı_adı=input("Kullanı Adı:")
    parola = input("Parola:")

    if(kullanıcı_adı !=sys_kul_adı and sys_parola==parola):
        print("Kullanıcı Adı Hatalı")
        giriş_hakkı-=1
    elif(kullanıcı_adı ==sys_kul_adı and sys_parola!=parola):
        print("Parola Hatalı !")
        giriş_hakkı-=1
        print("Giriş Hakkı:" ,giriş_hakkı)
    elif(kullanıcı_adı !=sys_kul_adı and sys_parola !=parola):
        print("Kullanıcı Adı ve Parola Hatalı!")
        giriş_hakkı-=1
        print("Giriş Hakkı:" ,giriş_hakkı)
        print("Giriş Hakkı:" ,giriş_hakkı)
    else:
        print("Başarıyla Giriş Yaptınız!")
    if(giriş_hakkı==0):
        print("Giriş Hakkınız Bitti")
        break              