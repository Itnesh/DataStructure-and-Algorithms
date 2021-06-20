# It is sum of preceding number of first two number and start from 0 and 1
# 0 1 1 2 3 .....
# Step 1 : Recursive case - the flow
# fibonacci(n)= fibonacci(n-1)+fiboncci(n-2)
# Step 2 : Base case - Stopping criteria
# 0,1 =0, 1
# Step 3 : Unintentional case - the constrain 
# not negative and nor fractional number allowed
def fibonacci(n):
    assert n>=0 and int(n)==n , 'Fibonacci number must be positve and intger!'
    if n in [0,1]:
        return n

    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(3))
print(fibonacci(9))
print(fibonacci(-1))
print(fibonacci(2.4))