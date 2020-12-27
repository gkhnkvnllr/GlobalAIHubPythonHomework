# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:56:53 2020

@author: gkhnk
"""

import random

def main():
    get_word_list()
    get_user_name()
    rules()
    playing_game(cpu_choice)


def get_word_list():
    get_words = open("C:\\Users\gkhnk\Desktop\words.txt","r+") ### It depends to your file directory
    words = get_words.read()
    
    word_list = words.split()
    
    global cpu_choice
    cpu_choice = random.choice(word_list)
    
    return cpu_choice

    
def get_user_name():    
    users_name = input("Enter your name: ").capitalize()
    print(f'\nWelcome {users_name}',"\n")
    
    
def rules():
    print(" Rule 1: You have 10 chances to guess the number","\n",
          "Rule 2: We have lots of words which include words with 1 letter","\n",
          "Rule 3: Just have fun!\n")
    

def playing_game(cpu_choice):
    
    under_score_list = []
    for x in range(len(cpu_choice)):
        under_score_list.append(" _ ")
    print (''.join(map(str, under_score_list)))
    
    guessed = False
    for i in range(10):
        if guessed == True:
            break
        user_letter_guess = input("Make your letter guess: ")
        counter = 0
        for j in cpu_choice:
            if j == user_letter_guess.lower():
                under_score_list[counter] = j
            counter += 1
        if " _ " not in under_score_list:
            print(f'\nCongratulations! You found the "{cpu_choice}" at your {i+1}. letter guess')
            guessed = True
            break
        else:
            print ("\n",''.join(map(str, under_score_list)))
        
        while True:
            guess_ask = input("Do you have a word guess Yes/No: ").lower()
            if guess_ask == "yes":
                user_guess = input("Enter your guess: ").lower()
                if user_guess == cpu_choice:
                    print(f'\nCongratulations! You guessed the "{user_guess}" at your {i+1}. turn')
                    guessed = True
                    break
                elif user_guess != cpu_choice:
                    print("\nNice try but it's not correct!")
                    break
            elif guess_ask == "no":
                break
            else:
                print("\nEnter Yes/No")
                
    if i > 10 or guessed != True:
        print("\n!!! GAME OVER !!! ")
        print(f'The word was "{cpu_choice}"')

            

main()