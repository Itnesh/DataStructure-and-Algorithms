# Step 1 : Recursive case - the flow
#{ 5 : 5/2=2 ramainder 1
# 5 is devidend 2 quotient 1 remainder
# 2/2 remainder 0
# binary(5): return f"{5%2}" +"{binary(5/2)}"}
# f(n)=n%2 + 10*f(n/2)
# 100010= 1*10 +0
# 10*10+0
# 100*10+0
# 1000*10+1
# 1001*10+0=100010

# Step 2 : Base case - stopping criteria
# Step 3 : Unitentional case - the Constraions
def decimaltobinary(n):
    assert int(n)==n, 'Number must be postive integer only!'
    if n==0:
        return 0
    else:
        return n%2 + 10*decimaltobinary(int(n/2))
print(decimaltobinary(-13))
