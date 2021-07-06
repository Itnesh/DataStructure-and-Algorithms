# # step 1 : Recursive case - flow
# def factoril(n):
#     return n*factoril(n-1)
# print(factoril(3))
# #repeated 996 more times
# #maximum recursion depth exceeded

# so limit the stack memory
# so lets import sys function for limiting the stack memory 
# import sys
# sys.setrecursionlimit(10000)
# def factoril(n):
#     return n*factoril(n-1)
# print(factoril(3))

# step 2 : Base case - stoping the criterion
# def factoril(n):
#     if n in [0,1]:
#         return 1
#     else:
#         return n*factoril(n-1)
# print(factoril(3))
# print(factoril(-1))
# step 3: unintentional case - the constrains
def factoril(n):
    assert n>=0 and int(n)==n, "Number must be positive number only!"
    if n in [0,1]:
        return 1
    else:
        return n*factoril(n-1)
# print(factoril(-1))
# print(factoril(5))
# but 
print(factoril(1.5))