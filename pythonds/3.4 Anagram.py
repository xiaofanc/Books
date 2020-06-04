"""
Anagram:
'heart' and 'earth'
'python' and 'typhon'

"""
# Solution 1: checking off and replace O(n^2)
def anagram1(s1, s2):
    stillOK = True
    if len(s1) != len(s2):
        stillOK = False

    alist = list(s2) # string is immutable
    pos1 = 0

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        # when found = True, replace as None in s2
        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 += 1

    return stillOK


print(anagram1('abcd', 'bcda'))

# Solution 2: sort and compare O(nlogn) depends on sorting
def anagram2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    pos = 0
    match = True

    alist1.sort()
    alist2.sort()
    #return alist1.sort() == alist2.sort()
    while pos < len(alist1) and match:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            match = False
    return match

print(anagram2('abcd', 'bcda'))

# Solution 3: Brute Force - O(n!)

# Solution 4: count and compare - O(n)
def anagram4(s1, s2):
    freqs1 = {}
    for i in range(len(s1)):
        freqs1[s1[i]] = freqs1.get(s1[i], 0) + 1
        """
        if s1[i] in freqs1:
            freqs1[s1[i]] += 1
        else:
            freqs1[s1[i]] = 1
        """
    freqs2 = {}
    for j in range(len(s2)):
        freqs2[s2[j]] = freqs2.get(s2[j], 0) + 1
        """
        if s2[j] in freqs2:
            freqs2[s2[j]] += 1
        else:
            freqs2[s2[j]] = 1
        """
    for key in freqs1.keys():
        if freqs1[key] != freqs2[key]:
            return False
    return True

print(anagram4('abcd', 'bcda'))

def anagram4(s1, s2): 
    c1 = [0]*26
    c2 = [0]*26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for j in range(len(s2)):
        pos = ord(s1[j]) - ord('a')
        c2[pos] += 1

    t = 0
    match = True
    while t < len(c1) and match:
        if c1[t] == c2[t]:
            t += 1
        else:
            match = False
    return match

print(anagram4('abcd', 'bcda'))









