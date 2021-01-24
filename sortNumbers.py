# -*- coding: utf-8 -*-
"""
Spyder Editor
Author:Stan
This file is for code bootcamp question
"""

#define the function signature which takes a list of numbers(in bracket)
def sortNumbers(numbers):
    #step 1: create an empty list for storing the sorted result
    result = []
    #step 2: get the each number from input list of numbers
  
    
    for n in numbers:
        # if the result list is empty, then just put the number at the beginning
        if len(result) == 0:
            result.insert(0,n)
        # otherwise, compare it with the numbers in the result list. 
        else:
            # initialise the index of inserting position in the result list
            index = 0
            for i in result:
                #If it is bigger than the first element, increase its index by 1
                if n > i:
                    index = index + 1
                #when it is either equal or smaller, break the circle
                else:
                    break
            # so all the other numbers will be inserted in an ascending way
            result.insert(index,n)
    # return the result list
    return result

# test case
numbers = []
numbers1 = [1,34,2,87,4,9]
numbers2 = [1, 23, 2, 3, 4, 3]
print(sortNumbers(numbers))
print(sortNumbers(numbers1))
print(sortNumbers(numbers2))


#def main():
#    #test case
#    numbers = []
#    numbers1 = [1,34,2,87,4,9]
#    numbers2 = [1, 23, 2, 3, 4, 3]
#    print(sortNumbers(numbers))
#    print(sortNumbers(numbers1))
#    print(sortNumbers(numbers2))
#    
#if __name__ == "__main__":
#    main()
        
    
    
