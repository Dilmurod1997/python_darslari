# -*- coding: utf-8 -*-


print("yaqin do'stlaringiz ro'xatini tuzamiz. ")
ismlar = []
n = 1
while True:
    savol = f"{n}-do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("yana ism qo'shasizmi? (ha/yo'q)")
    n+=1
    if takrorlash !='ha':
        break
print("Do'stlaringiz ro'yxati: ")
for ism in ismlar:
    print(ism.title())