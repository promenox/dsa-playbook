def rl_encode(s):
    if not s:
        return ""
    
    count = 1
    result = ""

    for i in range(1, len(s)):
        if (s[i] == s[i - 1]):
            count += 1 
        else:
            # concat prev repeat to res string and reset count
            result += str(count) + s[i - 1]
            count = 1
    
    # handle last run
    result += str(count) + s[i - 1]

    return result

print(rl_encode("aaaaaabbbb"))
print(rl_encode("aabbababab"))

# def rl_decode(string):
#     pass