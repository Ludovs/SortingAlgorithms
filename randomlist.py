import random

def random_list():
    list_lenght = 16
    list_output = []
    for i in range(0,list_lenght):
        list_output.append(random.randint(0,99))
    return list_output
