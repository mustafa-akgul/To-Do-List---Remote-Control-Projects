import time 
import random
class Kumanda():
    def __init__(self,tv_durum = "Kapali",ses_seviyesi = 0,kanal_listesi = ["TRT"],kanal = "TRT"):
        self.tv_durum = tv_durum
        self.ses_seviyesi = ses_seviyesi
        self.kanal = kanal
        self.kanal_listesi = kanal_listesi
    
    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("TV zaten açık durumda !")
        else:
            print("Tv açılıyor")
            self.tv_durum = "Açık"

    def tv_kapa(self):
        if(self.tv_durum == "Kapali"):
            print("TV zaten kapali durumda !")
        else:
            print("Tv kapanıyor..")
            self.tv_durum = "Kapali"
    
    def ses_ayarla(self):
        ses_girdi = input("Ses arttir = +\nSes azalt = -\nÇıkış = *\n")
        while True :
                if (ses_girdi == '+') :
                    self.ses_seviyesi+=1
                    print(f"Ses seviyesi: {self.ses_seviyesi}")
                    break
                elif(ses_girdi == '-'):
                    self.ses_seviyesi-=1
                    print(f"Ses seviyesi: {self.ses_seviyesi}")
                    break
                elif(ses_girdi == '*'):
                    print(f"Ses seviyesi: {self.ses_seviyesi}")
                    break
                else:
                    print("Yanlış girdi !!")
    
    def kanal_ekleme(self):
        yeni_kanal = input("Hangi kanali eklemek istersiniz : ")
        self.kanal_listesi.append(yeni_kanal)
    
    def rastgele_kanal(self):
        rkanal= random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rkanal]
    
    def __len__(self):
        return len(self.kanal_listesi)    

    def __str__(self):
        return "Tv durumu : {}\nSes seviyesi : {}\nKanal Listesi : {}\nKanal : {}".format(self.tv_durum,self.ses_seviyesi,self.kanal_listesi,self.kanal)

kumanda = Kumanda()
print("""
      
    1. TV Aç
    2. TV Kapat
    3. Sesi Ayarla
    4. Kanal Ekleme
    5. Kanal Sayısını Öğrenme
    6. Rastgele Kanal Açma
    7. TV Bilgilerini Öğrenme
    8. Çıkmak için 'q' ya basın
    
""")
while True:
    işlem = input("Hangi işlemi yapmak istersiniz : ")
    if(işlem == 'q'):
        print("Program Sonlandırılıyor..")
        time.sleep(3)
        break
    elif (işlem == '1'):
        kumanda.tv_ac()
        time.sleep(1)
    elif(işlem == '2'):
        kumanda.tv_kapa()
        time.sleep(1)
    elif(işlem == '3'):
        kumanda.ses_ayarla()
    elif(işlem == '4'):
        kumanda.kanal_ekleme()
    elif(işlem == '5'):
        print(len(kumanda.kanal_listesi))
    elif(işlem == '6'):
        kumanda.rastgele_kanal()
    elif(işlem == '7'):
        print(kumanda)
    else:
        print("Geçersiz işlem !")
        