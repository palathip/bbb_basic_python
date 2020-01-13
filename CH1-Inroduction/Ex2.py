# -*- coding: utf-8 -*-
redian = input("Insert Redian:")
hight = input("Insert Hight:") #ทดสอบ

def Find_Vol_Piramid (r,h):
    vol = ((1*1.0)/3)*3.141*(r**2)*h
    return vol
#
print Find_Vol_Piramid(r=redian,h=hight)
