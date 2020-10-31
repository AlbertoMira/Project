import numpy as np
from scipy.fftpack import fft
import pickle

#movementProcessing() can:
 #- Read the measurements coming from the .txt files.
 #- Store the data you process.
 #- Process several movements.

def movementProcessing():
    processMovement = input("Do you want to process a movement?\n1. Yes\n2. No\n")
    l_all_movements=[] #This list will contain all the arrays regarding all the movements you want to process.
    while processMovement=="Yes":
        movement = input("Enter the name of the file related to the movement: ")
        numberFiles =int(input("Enter the number of files you have regarding this movement: "))
        sensors =int(input("Enter the number of sensors you have: "))
        l=[]
        l1=[]
        l2=[]
        for i in range (1,numberFiles+1): #Here, the user enters the number of files. Mind that all file names should follow the same structure.
            f=open(movement+"_"+str(i)+".txt", "r")
            lists=f.readlines()
            lists=lists[3:]
            for e in lists: #Taking only the information which is useful for us.
                e=''.join(e)
                e=e.split(";")
                j=2
                while j<(sensors+2):
                    l2.append(e[j]) 
                    j=j+1
                l1.append(l2)
                l2=[]
            if len(l1)>=120:
                l.append(l1[0:120]) 
            l1=[]

        data=np.array(l)
        data=fftOnVector(data)
        l_all_movements.append(data) #Store the arrays related to the movement into a list. This is because if you want to process more movements afterwards,
                                     #you will have all of them splitted in different arrays.
        response = input("Do you want to store the data?\n1. Yes\n2. No\n")
        if response == "Yes":
            finalData=np.array(l_all_movements) #Array of arrays.
            vectorToPickle(finalData)
        else:
            print("Data not stored")
        processMovement = input("Do you want to process another movement?\n1. Yes\n2. No\n")
    print("Program finished")


def fftOnVector(vector): #Perform the fft of the given data.
    return fft(vector)


def vectorToPickle(vector): #Store the data using Pickle
    name = input("Enter the name of the movement: ")
    pFile = open(name, "wb")
    pickle.dump(vector, pFile)
    pFile.close()


movementProcessing()

        
    
    





















        



