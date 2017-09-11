def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    if exp == 0:
        return 1.0
    else:
        for i in range(1, exp):
            result = result*base
            print (result)
        return result

print(iterPower(2,0))
