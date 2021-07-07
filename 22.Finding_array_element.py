from array import *
arr1=array('i',[2,4,56,6,7])

def searcheElement(array,value):
    for i in array: # O(n)
        if i==value: #O(1)
            return array.index(value) #O(1)
    return "This value is not present" #O(1)
print(searcheElement(arr1,56))
print(searcheElement(arr1,80))

# Time complexity= O(n)
# Space complexity= Constant 