# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:18:44 2023

@author: User
"""

print("kiritilgan sonni kvadratini hisoblovchi dastur")
savol = "istalgan sonni kiriting"
savol += "(dasturmi to'xtatish uchhun 'exit' deb yozing)==" 
while  True: #abadiy sikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else: print(float(qiymat)**2)
print('dastur toxtadi')
    