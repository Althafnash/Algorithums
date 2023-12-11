"""
A Binary search is a algorithum in which we
first take the frist inex and lat index add and (/)
it to get the midpoint 

Now inside a while loop we first see if the midpoint 
is equal to target 

if the value below the midpoint is equal to the target 
we then print that as the target 

if the value above the midpoint is equal to the target
we print that value as the target  

or else if anything is not equal to the target we return 

if a target is found in any of these ocations then we 
verify it and print it

"""

def binary_search(list , target):
    first = 0 
    last = len(list) - 1

    while first <= last :
        midpoint = (first + last)//2

        if list[midpoint] == target :
            return midpoint
        elif list[midpoint] < target : 
            first =  midpoint + 1
        else :
            last = midpoint - 1
    
    return None 

def verfiy(index):
    if index is not None :
        print("Target found at index" , index)
    else :
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers , 12)
verfiy(result)

result = binary_search(numbers , 10)
verfiy(result)
