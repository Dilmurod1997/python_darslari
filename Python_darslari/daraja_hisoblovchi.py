# -*- coding: utf-8 -*-
"""
Created on Sat May  6 15:45:23 2023

@author: User
"""

print("kiritilgan sonni kvadratini hisoblovchi dastur")
savol = "istalgan sonni kiriting"
savol += "(dasturmi to'xtatish uchhun 'exit' deb yozing)==" 
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
print("dastur tugadi")