def strStr(haystack, needle):
    if needle == "":
        return 0
    elif needle in haystack:
        return haystack.index(needle)
    else:
        return -1
haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack,needle))