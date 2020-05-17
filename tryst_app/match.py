# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from numpy import array

activityList = pd.read_csv("activitylist.csv")
activityList = pd.DataFrame(activityList)
personality_questions = pd.read_csv("p_questions.csv")
personality_questions = pd.DataFrame(personality_questions)
print(activityList)
# print(activityList.iloc[7][1])

class User:

        def questions(self):
            ctr = 0 
            for i in range(0, 5):
                for j in range (0, 5):
                    print ("Question: {}".format(personality_questions.iloc[ctr][0]))
                    self.update(i, j, input("ANSWER: "))
                    print("\n")
                    ctr = ctr + 1 
        
        def update(self,i,j, val):
            self.init_array[i][j] = val
            
        def __init__(self, name, email, init_array, final_state):
            self.name = name
            self.email = email
            self.init_array = init_array
            self.final_state = final_state
        
        def prep_fs(self):
            for i in range(0,5):
                sum = 0
                for j in range(0, 5):
                    sum = sum + self.init_array[i][j]
                average = sum/5
                #print("average: {}".format(average))
                if average > 0.5:
                    self.final_state[i] = 1
                else:
                    self.final_state [i]= 0
                

initial_state = np.arange(25).reshape(5,5)
final_state = np.arange(5)
print(final_state)
status = input("If online: 1,else type 2: ")
name1 = input("User 1 , enter name: ")
email1 = input("User 1, enter email: ")

User1 = User(name1,email1, initial_state,final_state)

name2 = input("User 2, enter name: ")
email2 = input("User 2, enter email: ")

User2 = User(name2,email2, initial_state,final_state)

print("\nonly enter 1, 0 or -1 for the next set \n") 
print("{}! Your Turn to answer questions!\n".format(User1.name))
User1.questions()
print(User1.init_array)
User1.prep_fs()
print(User1.final_state)

print("{}! Your Turn to answer questions!\n".format(User2.name))
User2.questions()        
print(User1.init_array)  
User2.prep_fs()
print(User2.final_state)

combi = np.arange(5)
for i in range (0,5):
    combi[i] = (User1.final_state[i] + User2.final_state[i])/2

print(combi)

truthVal = 0
for rows in range(1, len(activityList)):
    test_array = np.array(activityList.iloc[rows][2:])
    value = combi == test_array
    if value.all():
        if status == 2:
            print("Your ideal date: {}".format(activityList.iloc[rows][1]))
            break
        else: 
            print("Your ideal online date: {}".format(activityList.iloc[rows][0]))
            break
    else:
        continue
      
            
            
    


     
        

