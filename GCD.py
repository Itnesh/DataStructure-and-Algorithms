#How to calculate the greatest common division number
# gcd(48,18)
# 48=2*2*2*2*3
# 18=2*3*3
# gcd(48,18)=6

# According to Euclidian Algorithms
# gcd(48,18)
# 48/18=2 remainder 12
# 18/12 = 1 remainder 6
# 12/6= 2 remainder 0
# Step 1: Recursive case- the flow
# gcd(b,a%b)
# Step 2: Base case - stopping criteria
# a%b=0
# Step 3: Unintentional case - the constrain

def gcd(a,b):
    assert int(a)==a and int(b)==b, " The number must be Integer only! "
    if b==0:
        return a
    else:
        return gcd(b, a%b)
print(gcd(48,18))
# print(gcd(3,1.4))
# print(gcd(22,-2))