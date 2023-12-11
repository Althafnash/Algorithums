"""
Made by Mohammed althaf 

A linear progreesion is a alogoritum in which 
we can find a target data in a list by looping 
trough every single index a comparing it to
the target data 

This is the funcationallity of the linear_search funcation 

Then we verifiy it and then we print it 

"""

def linear_search(list , target):
    """
    Retrun the index postion of the target if found , else returns None 
    """
    for i in range(0 , len(list)):
        if list[i] == target :
            return i
    return None 

def verfiy(index):
    if index is not None :
        print("Target found at index" , index)
    else :
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers , 12)
verfiy(result)

result = linear_search(numbers , 10)
verfiy(result)