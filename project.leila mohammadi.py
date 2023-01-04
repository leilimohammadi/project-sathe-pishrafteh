# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 20:09:48 2023

@author: shaver pc
"""

x= {} 
#دستور اضافه کردن                                  

def add(): 
  n= input("Enter your name:") 
  i= input("Enter your id:") 
  x[n]=i;
  
  
  #دستور حذف                                         

def delete(): 
  i= input("Enter name for deleting:") 
  x.pop(i) 
  
  
  
#دستور نمایش                                      

def show(): 
  for n,i in x.items():
      
    print(i,':',n)     
 
    
while True: 
    
  y= int(input('1:add student \n 2:delete student \n 3show student \n 4:exit \n ')) 
  
  if y == 1:  
      add( ) 
  elif y == 2: 
    delete()       
  elif y == 3: 
     show() 
  else: 
    break;