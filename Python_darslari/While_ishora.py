# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:11:05 2023

@author: User
"""

print("kiritilgan sonni kvadratini hisoblovchi dastur")
savol = "istalgan sonni kiriting"
savol += "(dasturmi to'xtatish uchhun 'exit' deb yozing)==" 
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:  print(float(qiymat)**2)
print("dastur to'xtadi")