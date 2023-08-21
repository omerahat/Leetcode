def isPalindrome(x):
    
    x=str(x)
    return x[::-1]==x

"""
2nd solution
def isPalindrome(x):
    x=str(x)
    if len(x)%2==0:
        return x[len(x)//2:]==(x[:len(x)//2])[::-1]
    else:
        return x[len(x)//2+1:]==(x[:len(x)//2])[::-1]
"""
