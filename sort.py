import time
from randomlist import random_list

start_time = time.time()
elapsed_time = 0

def bubblesort(list):
    print("---------------------Bubble Sort---------------------")
    print("Not Sorted: "+str(list))
    moves = 1
    while moves > 0:
        moves = 0
        for i in range(0,len(list)-1):
            if list[i] > list[i+1]:
                moves += 1
                n = list[i+1]
                list[i+1] = list[i]
                list[i] = n
                swapped = True
    elapsed_time = time.time()-start_time
    print("Sorted: "+str(list)+" Elapsed Time: "+str(elapsed_time))
    return list

def insertionsort(list):
    print("---------------------Insertion Sort---------------------")
    print("Not Sorted: "+str(list))
    
    for i in range(1,len(list)):
        j = i
        while list[j-1] > list[j] and j > 0:
            n = list[j-1]
            list[j-1] = list[j]
            list[j] = n
            j -= 1

    elapsed_time = time.time()-start_time
    print("Sorted: "+str(list)+" Elapsed Time: "+str(elapsed_time))
    return list

bubblesort(random_list())
insertionsort(random_list())