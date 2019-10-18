# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:44:19 2019

@author: Hwayne

practice 2.1

"""
'''
輸入半徑計算圓之周長、面積等值
'''
radius=eval(input("Enter a value for radius:"))

area=radius*radius*3.1415926

Perimeter=2*3.1415926*radius

print("此圓之周長為",Perimeter,"面積為",area )
'''
computeAverage.py


'''
number1=eval(input("Please enter the first number: "))
number2=eval(input("Please enter the second number: "))
number3=eval(input("Please enter the third number: "))

average=(number1+number2+number3)/3
print("the average of",number1,number2,number3,"is",average)

'''
computeAverageWithSimultaneousAssignment.py

'''
'''

print("求平均值，可輸入任意多個數")
lst=[]
str=raw_input("請輸入數值，用空行隔開")
lst1=str.split(" ")
i = 0
while i<=len(lst)+1:
    lst.append(int(lst1.pop())  
    i += 1
    
def sum(list)    :
    "對列表數據求合"
    s=0
    for x in list:
        s += x
    return s

def acerage(list):
    
    "對列表數據求平均"
    avg=0
    avg=sum(list)/(len(list)*1.0)
    rwturn avg

print("avg=%f"%average(lst))    
    
    
    
    
    
    
    
    
    
    
    
    
    