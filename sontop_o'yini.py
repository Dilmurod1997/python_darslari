# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:33:00 2023

@author: Sharipov Dilmurod
"""
import random

def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"1 dan {x} gacha bo'lgan son o'yladim topa olasizmi")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin>tasodifiy_son:
            print("men o'ylagan son bundan kichikroq")
        elif taxmin<tasodifiy_son:
            print("men o'ylagan son bundan kattaroq")
        else:
            break
    
    print(f"Tabriklayman siz {taxminlar} urinishda to'g'ri topdingiz!!!")
    return taxminlar
    
def sontop_pc(x=10):
    input(f"1 dan {x} gacha bo'lgan biron son o'ylang va istalgan tugmani bosing.  Men topaman>>>")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin =quyi
        javob = input(f"siz {taxmin} sonini o'yladingiz: to'g'ri (t), "
                      f"men o'ylagan son bundan kattaroq (+), men o'ylagan son bundan kichikroq (-)>>>")
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    
    print(f"men {taxminlar} urinishda Topdim!!!")
    return taxminlar
    
def play (x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user<taxminlar_pc:
            print(f"Tabriklayman siz yutdingiz!!!")
        elif taxminlar_user>taxminlar_pc:
            print("men yutdim")
        else:print("Durrang")
        yana = int(input("yana o'ynaysizmi ha(1), yo'q (0)"))
    
            
