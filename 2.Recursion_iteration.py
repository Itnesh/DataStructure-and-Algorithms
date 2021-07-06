# Recursion is memory inefficient program because its takes extra stack memory for execution
# Recursion is used to easy to code where problem divided into subproblem in similar problem otherwise iteration is best
# It is most preferable in terms of graph and tree structure problem
# Recursion
def poweroftwo(n):
    """This function helps to create the power of two"""
    if n==0:
        return 1
    else:
        power=poweroftwo(n-1)
        return power*2
print(poweroftwo(5))

# Iteration
def poweroftwo_i(n):
    """This function can be used to create of power of two"""
    i=1
    power=1
    while i<n:
        power=power*2
        i=i+1
    return power
print(poweroftwo_i(3))
