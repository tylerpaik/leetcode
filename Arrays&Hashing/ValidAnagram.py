class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in t:
                s[1:]
            else:
                return False
        return True
    
#Doesnt account for when all the letters are present but different numbers of said letters. Trying hashing strategy
    
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True

#84.42%, 82.41% 
#It seems like its typically faster to compare two hash tables than to subtract from the same one, so lets see if that decreases the time

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counts = {}
        countt = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for char in t:
            countt[char] = countt.get(char, 0) + 1
        return counts == countt
  
#72.25%, 96.56%
#wasnt faster, but uses very little memory. get saves memory and loses speed

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counts = {}
        countt = {}
        for char in s:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
        for char in t:
            if char not in countt:
                countt[char] = 0
            countt[char] += 1
        return counts == countt
    
#94.05%, 82.41%

