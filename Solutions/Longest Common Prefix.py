def longestCommonPrefix(strs):
    if len(strs)==1:
        return strs[0]
    test_word=strs[0]
    common=""

    for i in range(len(test_word)):
        counter=0
        for string in strs:
            if test_word[:i] ==string[:i]:
                counter+=1
        if counter==len(strs):
            common=test_word[:i]

    return common

