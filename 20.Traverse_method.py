# It is a mthod to call the element from array one by one.
from array import *
arr1=array('i',[2,4,5,6,77,8,8])
def TraverseArray(array):
    for i in array:  # time comlexity O(n)
        print(i)     # constant time complexity O(1)
print(TraverseArray(arr1))

# Means time complexity =O(n)
# space complexity =O(1) , constant space comlexity because no need of any stack memory