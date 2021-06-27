from array import *
arr1=array('d',[2.4,5.6,4.5,3.5,3.5])

def AccessArray(array, index):
    assert index >=0, 'Index must be positve number'
    if index >= len(array):
        print("There is no any element in this index")
    else:
        print(array [index])
AccessArray(arr1,4)

# O- Notion
# Time Complexity =constant~ O(1)
# Space complexity = O(1)