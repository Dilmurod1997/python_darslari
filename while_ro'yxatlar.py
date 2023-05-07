# -*- coding: utf-8 -*-
"""
Created on Sun May  7 13:25:29 2023

@author: User
"""

print("yaqin do'stlaringiz yoshini saqlaymiz. ")
dostlar = {}
ishora = True
while ishora:
    ism = input("do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)
    javob = input("yana malumot qo'shasizmi? (ha/yo'q)")
    if javob =="yo'q":
        ishora =False
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")