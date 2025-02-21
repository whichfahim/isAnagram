from collections import defaultdict

def isAnagram(s, t):
    if len(s)!=len(t):
        return False
    else:
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for i in range(len(s)):
            s_count[s[i]] += 1
            t_count[t[i]] += 1
        
        if s_count == t_count:
            return True
        else:
            return False

def groupAnagram(words):
    hashMaps = []
    for word in words:
        for i in len(word):
            # create a hashmap for each word
            # append it to the list of hashmaps
            new_hashMap = {}
            new_hashMap[word[i]] += 1
            
    return [[]]

# s = "racecar"
# t = "carrace"

# s = "jar"
# t = "jam"

# s = "bbcc"
# t = "ccbc"

# print(isAnagram(s,t))

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagram(strs))
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
