vize1 = int(input("Vize 1 notunuzu giriniz : \n"))
vize2 = int(input("Vize 2 notunuzu giriniz : \n"))
final = int(input("Final notunuzu giriniz : \n"))

def puanHesapla(vize1, vize2, final):
    if 0 <= vize1 < 100 and 0 <= vize2 < 100 and 0 <= final < 100:
        puan = (vize1*0.3) + (vize2*0.3) + (final*0.4)
        print(notGosterimi(puan))
    else:
        print("Notlar aralık dışındadır.")

def notGosterimi(x):
    if x >= 90:
        return "AA"
    elif 85 <= x < 90:
        return "BA"
    elif 80 <= x < 85:
        return "BB"
    elif 75 <= x < 80:
        return "CB"
    elif 70 <= x < 75:
        return "CC"
    elif 65 <= x < 70:
        return "DC"
    elif 60 <= x < 65:
        return "DD"
    elif 55 <= x < 60:
        return "FD"
    else:
        return "FF"

puanHesapla(vize1, vize2, final)

