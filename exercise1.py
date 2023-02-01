import random
'''
questo è un commento multilinea 

create a list 
print it 
shuffle it 
print it again
use at least one function

'''


MyAwesomeList= [1,2, 3, 4 ,5 ] # declare list

def shuffle():                  #define method 
    random.shuffle(MyAwesomeList)
 

print(MyAwesomeList)    # print 1
shuffle()               # call the shuffle method
print(MyAwesomeList)    # print 2 


