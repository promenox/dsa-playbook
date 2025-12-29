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
    
    # handle appendage on last run
    result += str(count) + s[i - 1]

    return result

def rl_decode(s):
    if not s:
        return ""
    
    result = ""

    # assumes pairwise str [digit][char] 
    for i in range(len(s) // 2):
        # expands pairwise in explicit format [digit][char]
        result += ((s[(i * 2) + 1]) * int(s[(i * 2)]))

    return result

# encoding test
print(rl_encode("aaaaaabbbb"))
print(rl_encode("aabbababab"))

# decoding test
print(rl_decode("6a4b"))
print(rl_decode("2a2b1a1b1a1b1a1b"))
