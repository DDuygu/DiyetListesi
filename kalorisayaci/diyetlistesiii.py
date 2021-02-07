import time

print("******kalori sayacina hosgeldiniz*****")



yas = int(input('yasinizi girin: '))
if yas <= 8:
        print('en fazla 1000 kalori alabilirsiniz')
        kalori1000 = [ 'sabah:'
                       '1 ince dilim kepek ekmek, 1 karper dilimi kadar beyaz peynir, domates, salatalık '
                       'ogle:'
                       '8 kaşık sebze yemeği, Yumurta büyüklüğünde 2 adet köfte ya da tavuk,salata ',
                       'aksam:'
                       '8 kaşık sebze yemeği, 1 ince dilim kepek ekmek, Salata, yogurt'
                    ]
        print(kalori1000)


elif 9 <= yas <= 13:
        print('en fazla 1600 kalori alabilirsiniz')
        kalori1600 = ['sabah:'
                      'Açık çay, 2 dilim ekmek, 6 zeytin, 3 kibrit kutusu peynir, istenilen kadar cig sebze'
                      'ogle:'
                      '6 kaşık sebze yemeği, 1 kase çorba, 2 dilim ekmek, istenildiği kadar yağsız salata'
                      'aksam:'
                      '1 kase çorba, 2 dilim ekmek ,istenildiği kadar yağsız salata'
                      ]

        print(kalori1600)

elif 14 <= yas <= 18:
        print('en fazla 1800 kalori alabilirsiniz')
        kalori1800 = [ 'sabah:'
                      'sekersiz cay, 2 k.k beyaz peynir, domates, salatalık, 2 dilim ekmek'
                      'ogle:'
                      '100 gr Haşlanmış tavuk, yoğurt (1 tabak 200 gr), yağsız salata'
                      'aksam:'
                      'Sebze yemeği (8 yemek kaşığı), kaymaksız 1 kase yoğurt, yağsız salata'
                       ]
        print(kalori1800)

elif 19 <= yas <= 30:
        print('en fazla 2000 kalori alabilirsiniz')
        kalori2000 = [ 'sabah:'
                      'Çay veya kahve (şekersiz), 1 su bardağı 200ml süt, 2 kibrit kutusu az yağlı beyaz peynir, salatalık , domates, 2 ince dilim kepekli ekmek'
                      'ogle:'
                      ' 100 g tavuk (ızgara veya haşlanmış), 1 kase yoğurt (kaymaksız,200 g), yağsız salata, 1 porsiyon meyve'
                      'aksam:'
                      '8 yemek kaşığı sebze yemeği, 1 kase kaymaksız yoğurt, yağsız salata, 6 yemek kaşığı makarna'

        ]
        print(kalori2000)

elif 31 <= yas <= 50:
        print('en fazla 2200 kalori alabilirsiniz')
        kalori2200 = ['sabah:'
                      'taze sıkılmış portakal suyu, 5 adet zeytin, 1 adet haşlanmış yumurta, 2 dilim kaşar peyniri, bir adet domates'
                      'ogle:'
                      ' bir kâse lahana çorbası, bir kâse yoğurt ve mevsim salata '
                      'aksam:'
                      '13 adet köfte, bir kâse yoğurt, mevsim salata'

        ]
        print(kalori2200)
elif yas > 50:
        print('en fazla 1600 kalori alabilirsiniz')
        kalori1400 = ['sabah:'
                      'Açık çay, 2 dilim ekmek, 6 zeytin, 3 kibrit kutusu peynir, istenilen kadar cig sebze'
                      'ogle:'
                      '6 kaşık sebze yemeği, 1 kase çorba, 2 dilim ekmek, istenildiği kadar yağsız salata'
                      'aksam:'
                      '1 kase çorba, 2 dilim ekmek ,istenildiği kadar yağsız salata'
                      ]
        print(kalori1400)


toplamkalori = 0
x = 'e'
while (x == 'e'):

        print("protein icin 1 basin")
        print("k.hidrat icin 2 basin")
        print("sebze icin 3 basin")
        print("programı kapatmak icin 4  basın")

        secim = int(input("menuden bir secenek sec"))

        #PROTEIN İCİN

        if (secim == 1):

            protein = {
                #'0': 0 ,
                'et': 100,
                'yumurta': 50,
                'sut': 150
                        }

            for x in protein:
                print(x)

            secilenyemek = str(input("sectiğiniz yemeğin adini girin: "))
            if (secilenyemek == 'et'):
                print('et seçtiniz: 100 kalori')
                toplamkalori = toplamkalori + 100
            elif (secilenyemek == 'yumurta'):
                print('yumurta seçtiniz: 50 kalori')
                toplamkalori = toplamkalori + 50
            elif (secilenyemek == 'sut'):
                print('sut seçtiniz: 150 kalori')
                toplamkalori = toplamkalori + 150

            x = str(input("başka yemek seçmek için e toplam kaloriyi görmek için h basın "))


        # KARBONHİDRAT

        elif (secim == 2):

            karbonhidrat = {
                #'0': 0 ,
                'makarna': 100,
                'pilav': 50,
                'patates kızartması': 150
                        }

            for x in karbonhidrat:
                print(x)

            secilenyemek = str(input("sectiğiniz yemeğin adini girin: "))

            if (secilenyemek == 'makarna'):
                print('makarna seçtiniz 100 kalori')
                toplamkalori = toplamkalori + 100

            elif (secilenyemek == 'pilav'):
                print('pilav seçtiniz 50 kalori')
                toplamkalori = toplamkalori + 50

            elif (secilenyemek == 'patates kizartmasi'):
                print('patates kizartmasi seçtiniz 50 kalori')
                toplamkalori = toplamkalori + 50


            x = str(input("başka yemek seçmek için e toplam kaloriyi görmek için h basın "))

            #SEBZE

        elif (secim == 3):

            sebze = {
                     # '0': 0 ,
                     'ıspanak': 100,
                     'fasulye': 500,
                     'patlıcan yemegi': 150
                 }

            for x in sebze:
                 print(x)

            secilenyemek = str(input("sectiğiniz yemeğin adini girin: "))
            if (secilenyemek == 'ıspanak'):
                print('ıspanak seçtiniz 100 kalori')
                toplamkalori = toplamkalori + 100

            elif (secilenyemek == 'fasulye'):
                print('domates seçtiniz 500 kalori')
                toplamkalori = toplamkalori + 50

            elif (secilenyemek == 'patlican yemegi'):
                print('patlican yemegi seçtiniz 150 kalori')
                toplamkalori = toplamkalori + 150


            x = str(input("başka yemek seçmek için e toplam kaloriyi görmek için h basın "))


        elif (secim == 4):
            print('cikis yapiliyor')
            time.sleep(1)
            exit()

else:
    print('seçimleriniz toplam',toplamkalori,'kalori ')
