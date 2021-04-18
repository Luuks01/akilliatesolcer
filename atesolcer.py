import datetime

ates = input("Ateş değerini giriniz : ")
zaman = datetime.datetime.now()

if (int(ates) == 38):
    print("Ateşiniz çok yüksek, acilen en yakın hasteneye gitmeniz gerekmektedir. Saat: " , zaman.hour,":", zaman.minute)

elif (int(ates) > 38):
    print("Ateşiniz çok yüksek, acilen en yakın hasteneye gitmeniz gerekmektedir. Saat: " , zaman.hour,":", zaman.minute)

elif (int(ates) >34):
    print("Ateşiniz normal. Saat:" , zaman.hour,":", zaman.minute)

elif (int(ates) <35):
    print("Ateşiniz çok düşük, acilen en yakın hasteneye gitmeniz gerekmektedir. Saat: " , zaman.hour,":", zaman.minute)
