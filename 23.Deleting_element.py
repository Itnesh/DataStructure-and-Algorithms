from array import *
arr1= array('i',[2,3,5,8,6])

arr1.remove(3)
print(arr1)

# Time complexity =O(n)
# Space complexity = O(1)

arr1.remove(6)
print(arr1)

# Time complexity =O(1)
# space complexity =O(1)

# why time complexity is varring ?
# If you remove from the last of element in array then there is no any shift in postion in array happens but if you remove from the begning means it shift the all element one step back all the element. Thats whils it takes n time more time than last elememt removal time.