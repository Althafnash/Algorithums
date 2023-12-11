"""
A recurisive binary algorithum is a binary alogrithum 
with an internal loop so if go through the binary alogrithum 
the following will happen 

Now inside a while loop we first see if the midpoint 
is equal to target 

if the value below the midpoint is equal to the target 
we then print that as the target 


"""

def recursive_binary_search(list , target):
    if len(list) == 0:
        return False
    else : 
        midpoint = len(list)//2

    if list[midpoint] == target:
        return True 
    elif list[midpoint] < target : 
        return recursive_binary_search(list[midpoint + 1 :] ,target)
    else :
        return recursive_binary_search(list[:midpoint] , target)

def verify(result):
    print("Target found " , result)

numbers = [1,2,3,4,5,6,7,8]

result = recursive_binary_search(numbers , 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)