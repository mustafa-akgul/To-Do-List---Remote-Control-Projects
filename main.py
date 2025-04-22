import taskFunctions

while True:
    print("""
    To Do List Uygulamasına Hoşgeldiniz
    1-Görevleri Görüntüleme
    2-Görev Ekleme
    3-Görev Silme
    4-Tamamlanmış Görevleri Görüntüleme
    5-Çıkmak için 'q' tuşuna basın
    """)    
    islem = input("İşlem yapmak istediğiniz seçeneğin numarasını girin :  ")
    
    if islem == '1':
        taskFunctions.monitor_to_tasks()
    if islem == '2':
        taskFunctions.add_list()
    if islem == '3':
        taskFunctions.del_from_list()
    if islem == '4':
        taskFunctions.completed_tasks()
    if islem == 'q':
        break
    else:
        print("Hatalı değer girdiniz !")
