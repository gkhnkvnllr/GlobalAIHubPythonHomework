# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:38:47 2020

@author: gkhnk
"""
user_info = []

user_first = input("Enter your First Name: ")
user_info.append(user_first)

user_last = input("Enter your Last Name: ")
user_info.append(user_last)

user_age = int(input("Enter your age: "))
user_info.append(user_age)

user_birth = int(input("Enter your birth year: "))
user_info.append(user_birth)

"""
counter = 0

while counter < len(user_info):
    print(user_info[counter])
    counter += 1
"""    
for i in user_info:
    print(i)


if user_info[2] <= 18:
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street")
    
    
    # Gökhan Kovanlılar