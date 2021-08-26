# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    if len(s2) < len(s1):
        (s1, s2) = (s2, s1)
    sub = ""
    nsub = 0
    for i in range(len(s1)):
        for j in range(i+1, len(s1)+1):
            s = s1[i:j]
            ns = len(s)
            if ns < nsub:
                continue
            if s in s2:
                if ns == nsub:
                    sub = min(s, sub)                    
                if ns > nsub:
                    sub = s
                    nsub = ns
    return sub
