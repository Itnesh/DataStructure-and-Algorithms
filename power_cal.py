# Step 1: Recursive case - the flow
    # power(base, exp -1)
# Step 2: Base case - stopping criteria
# exp = 0 and 1
# Step 3: Unintentional case - the constrain

def power(base, exp):
    assert exp>=0 and int(exp)==exp, 'The exponent must be postive integer only!'
    if exp==0:
        return 1
    elif exp==1:
        return base
    else:
        return base * power(base, (exp - 1))
    
print(power(3,6))
# print(power(3,-1))
# print(power(3,1.5))