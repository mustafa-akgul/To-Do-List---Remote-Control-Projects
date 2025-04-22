
import time
gorevler = []
tamamlanan_gorevler = []
def add_list():

    while True:
        deger = input("Gorev eklemek için gorevin adini yazin veya 'q' tuşuna basın : ")
        if(deger == 'q'):
            break
        else:
            gorevler.append(deger)
            print("Gorev ekleniyor..")
            time.sleep(0.3)
def del_from_list():
    while True:
       
        if not gorevler:  
            print("Herhangi bir görev bulunmuyor. Görev ekleyin.\n")
            deger = input("Çıkmak için 'q' tuşuna basın : ")
            if(deger == 'q'):
                print("Çıkış yapılıyor..")
                time.sleep(0.3)
                break
             

        print("--Mevcut gorevler--\n")
        for i, gorev in enumerate(gorevler):
            print(f"ID : {i} Gorev Adı : {gorev}")

        deger = input("Görev silmek için gorev numarasini yazin veya 'q' tuşuna basın : ")

        if deger == 'q':
            print("Çıkış yapılıyor..")
            time.sleep(0.3)
            break
        elif deger.isdigit():
            deger = int(deger)
            if 0 <= deger < len(gorevler):
                del gorevler[deger]
                print("Görev siliniyor..")
                time.sleep(0.3)
            else:
                print("Geçersiz görev numarası!")
        else:
            print("Lütfen geçerli bir görev numarası girin!")
            
def monitor_to_tasks():

    while True:
        print("--Mevcut gorevler--\n")
        
        if not gorevler:
            print("Herhangi bir görev bulunmuyor")
            deger = input("Çıkmak için 'q' tuşuna basın : ")
            if(deger == 'q'):
                print("Çıkış yapılıyor..")
                time.sleep(0.3)
                break
        else:
            for i in range(len(gorevler)):
                print(f"ID == {i} Gorev Adı == {gorevler[i]}\n")

            deger = input("Görev tamamladıysanız ID numarasını yazin veya çıkmak için 'q' tuşuna basın : ")
            if(deger == 'q'):
                    print("Çıkış yapılıyor..")
                    time.sleep(0.3)
                    break
            elif(deger.isdigit()):
                    deger = int(deger)
                    tamamlanan_gorevler.append(gorevler[deger])
                    del gorevler[deger]

def completed_tasks():
    while True:
        if not tamamlanan_gorevler:
            print("Tamamlanmış herhangi bir görev bulunmuyor")
            deger = input("Çıkmak için 'q' tuşuna basın : ")
            if(deger == 'q'):
                print("Çıkış yapılıyor..")
                time.sleep(0.3)
                break

        for i in range(len(tamamlanan_gorevler)):
                    print(f"ID : {i} Gorev Adı : {tamamlanan_gorevler[i]}\n")
                    deger = input("Çıkmak için 'q' tuşuna basın : ")
                    if(deger == 'q'):
                        print("Çıkış yapılıyor..")
                        time.sleep(0.3)
                        break