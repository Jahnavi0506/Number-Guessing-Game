# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:14:58 2025

@author: jahnavi
"""
import random

print("Hey,Hi welcome to number game .In this game u have to guess a number .The number lies between 1 to 100.You have 5 chances .")
actual_no=random.randrange(100)
chances=5
attempt=0
while attempt<chances:
    attempt+=1
    guess=int(input("enter a number in the range of 100 :"))
    if ( actual_no==guess):
        print(f'you got it in{attempt} attempt')
        break
    elif attempt>=chances and guess!=actual_no:
        print(f"sorry u are out of chances and the number is {actual_no}")
    elif guess > actual_no:
        print("your number is higher")
    elif guess < actual_no:
        print("your number is lesser")
        