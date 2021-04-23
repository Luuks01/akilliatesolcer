iimport datetime
import random

ates = random.randint(30,40)
zaman = datetime.datetime.now()

if (int(ates) == 38):
    print("Ateşiniz 38 derece ve yüksek, acilen en yakın hasteneye gitmeniz gerekmektedir. Saat: " , zaman.hour,":", zaman.minute)

elif (int(ates) > 38):
    print("Ateşiniz", ates ,"derece, ve çok yüksek, acilen en yakın hasteneye gitmeniz gerekmektedir. Saat: " , zaman.hour,":", zaman.minute)

elif (int(ates) >34):
    print("Ateşiniz", ates ,"derece ve normal. Saat:" , zaman.hour,":", zaman.minute)

elif (int(ates) <35):
    print("Ateşiniz", ates , "derece ve çok düşük, acilen en yakın hasteneye gitmeniz gerekmektedir. Saat: " , zaman.hour,":", zaman.minute)


