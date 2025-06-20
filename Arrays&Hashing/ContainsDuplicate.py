class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            num = nums.pop()
            if num in nums:
                return True
        return False
        
#TLE

class Solution(object):
    def containsDuplicate(self, nums):
        seen = []
        for num in nums:
            if num in seen:
                return True
            else:
                seen.append(num)
        return False
    
#TLE

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
    
#26.45%, 46.42%
#Pretty weak, can we use hash?

class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 0
        return False

#26.45%, 84.00%
#Didn't speed up, but better memory

class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
                return True
            else:
                seen[num] = 0
        return False

#70.91%, 88.58%
#Try abusing set inability to hold duplicates

class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
    
#97.84%, 18.38%
#so sets use more memory but are faster