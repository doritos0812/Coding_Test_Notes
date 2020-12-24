def is_Prime(x):
    for i in range(2, int(x**(1/2)) + 1):
        if x % i == 0:
            return False
    return True

'''
print(is_Prime(7))
print(is_Prime(12))
'''