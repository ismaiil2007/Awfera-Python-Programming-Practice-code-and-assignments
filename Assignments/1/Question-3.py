

'''
STEP 1 : I will open Anaconda prompt
STEP 2 : Navigate to The Required Directory in My file exist using cd commands
STEP 3 : I will run the command 'conda create --name sortenv python=3.9' to create the environment
STEP 4 : I will activate sortenv using command 'conda activate sortenv'
'''

import numpy as np

int_input = input("Enter Numbers : ")
int_list=[]

try:
    if int_input:
        int(int_input)
        for integer in int_input:
            # print("Starting Loop")
            # int(integer)
            # try:    
                # if type(integer) == int:
                    int_list.append(integer)
                    # print("appended")
            # except:
                # else:
                #     print("\n"+" "*7+"You are supposed to Enter Numbers!"+" "*7+"\n")
                #     break
        


        print("Sorted List: ",np.sort(int_list))
    else:
        print("\n"+" "*7+"Input is Blank!"+" "*7+"\n")
except :
    print("\n"+" "*7+"You are supposed to Enter Numbers!"+" "*7+"\n")

