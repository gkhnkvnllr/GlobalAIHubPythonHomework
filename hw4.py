# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:24:51 2020

@author: gkhnk
"""

def main():
    
    student_info()
    if auth_check == True:
        student_lessons()
        if len(taken_lessons_list) >= 3:
            lessons_exam(taken_lessons_list)
    
    
def student_info():
    
    user_name = "Gökhan" # We already assigned name to check name_input
    user_surname = "Kovanlılar" # We already assigned surname to check surname_input
    
    global auth_check
    auth_check = False
    check_counter = False
    
    while True:
        for i in range(3):
            name_input = input("Enter your name: ").capitalize()
            surname_input = input("Enter your surname: ").capitalize()
            
            if name_input == user_name and surname_input == user_surname:
                print(f'\nWelcome {name_input}')
                check_counter = True
                auth_check = True
                break
            else:
                print("\nIncorrect name/surname")
                
        if check_counter == True:
            break
        else:
            print("\nTry again later")
            break
        
        
def student_lessons():
    
    semester_lessons_list = []
    global taken_lessons_list
    taken_lessons_list = []
    
    while True:
        semester_lessons = input("\nEnter your this semester's courses: ").capitalize()
        semester_lessons_list.append(semester_lessons)
        if len(semester_lessons_list) == 5:
            break
    
    while True:
        taken_lessons = input("\nEnter taken lessons: ").capitalize()
        if taken_lessons in semester_lessons_list:
            taken_lessons_list.append(taken_lessons)
            semester_lessons_list.remove(taken_lessons)
            taken_lessons_ask = input("\nDo you want to add another course? Yes/No: ").capitalize()
            if taken_lessons_ask == "Yes":
                continue
            elif taken_lessons_ask == "No":
                if len(taken_lessons_list) >= 3 and len(taken_lessons_list) <= 5:
                    return taken_lessons_list
                elif len(taken_lessons_list) < 3:
                    print("\nYou failed in class")
                break
            else:
                print(f'\nEnter Yes/No not "{taken_lessons_ask}"')
        elif taken_lessons not in semester_lessons_list:
            print("\nPlease enter this semester's lessons")
        
        
def lessons_exam(taken_lessons_list):
    
        grades_dictionary = {"midterm": 0, "final": 0, "project": 0}
        while True:
            add_grades = input("\nChoose one of your lesssons to add grades: ").capitalize()
            if add_grades in taken_lessons_list:
                midterm_grade = int(input("\nEnter your midterm grade: "))
                final_grade = int(input("\nEnter your final grade: "))
                project_grade = int(input("\nEnter your project grade: "))
                grades_dictionary.update({'midterm': midterm_grade, 'final': final_grade, 'project': project_grade})
                break
            else:
                print(f'\nEnter one of those lessons {taken_lessons_list}')
                
        total_grade = (grades_dictionary['midterm']*0.3) + (grades_dictionary['final']*0.5) + (grades_dictionary['project']*0.2)
        print(f'\nYour total grade is {total_grade}')
        if total_grade >= 90:
            print("Such a hardworking student! You have an 'AA'")
        elif total_grade >= 70 and total_grade < 90:
            print("You earned an 'BB'")
        elif total_grade >= 50 and total_grade < 70:
            print("Not bad you can do better 'CC'")
        elif total_grade >= 30 and total_grade < 50:
            print("You should work harder 'DD'")
        elif total_grade < 30:
            print("Congratulations YOU FAILED! You earned a 'FF'") 
            
        
main()