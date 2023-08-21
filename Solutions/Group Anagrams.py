def groupAnagrams(strs):

    if len(strs) <= 1:
        return [strs]
    
    words = []
    result = []

    for word in strs:
        if sorted(list(word)) not in words:
            words.append(sorted(list(word)))
            result.append([word])
        else:
            index = words.index(sorted(list(word)))
            result[index].append(word)

        

    return result

