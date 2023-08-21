def isAnagram(s,t):
    if len(s)!= len(t):
        return False  
    
    charsDict1= {}
    charsDict2= {}
    for i in s:
        if i not in charsDict1.keys():
            charsDict1[i]=1
        else:
            charsDict1[i]+=1
    
    for i in t:
        if i not in charsDict2.keys():
            charsDict2[i]=1
        else:
            charsDict2[i]+=1

    return charsDict2==charsDict1
    

""" 2nd solution
def isAnagram(s,t):
    return sorted(s)==sorted(t)
"""
