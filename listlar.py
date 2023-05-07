#list yaratish va unga elementlarni qo'shish va o'chirish
meva = input("meva nomini kiriting=")
mevalar = ["olma","nok", "gilos", "shaftoli"]
mevalar.append("behi")
mevalar.remove("gilos")
#if elif va else operatorlari
if meva == "olma":
        print(meva, "4000 so'm")
elif meva == "nok":
        print(meva, "6000 so'm")
elif meva == "gilos":
          print(meva, "2000 so'm")  
elif meva == "shaftoli":
          print(meva, "9000 so'm") 
elif meva == "behi":
          print(meva, "7000 so'm") 
else:
        print("bunday meva sotuvda mavjud emas")
    