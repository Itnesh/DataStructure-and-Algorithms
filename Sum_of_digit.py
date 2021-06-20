# Step 1 : Recursive case - the flow
#     f(n)=(n/10)+(n%10)
# Step 2 : Base case - stoping the creation
# n=0
# Step 3 : Unintensional case- Criterion constarins
# int(n)=n and n>=0

def sumofdigit(n):
    assert n>=0 and int(n)==n, 'input number must be positive integer'
    if n==0:
        return 0
    else:
        return int(n%10) + sumofdigit(int(n/10))
# print(sumofdigit(-2))
# print(sumofdigit(1.5))
print(sumofdigit(442))