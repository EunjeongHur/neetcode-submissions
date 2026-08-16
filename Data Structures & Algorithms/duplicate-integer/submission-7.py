class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
        return False


# create a set because set is not allow us to store duplicate values
# loop through the nums list 
# then, if n exists in hashset -> return true 
# otherwise, add that number to the set. 
# After loop, return False

# Time Complexity:
# set initialization: O(1)
# for loop: O(n) 
# set operations:
#       - lookup : O(1)
#       - insertion: O(1)
# Therefore, overall time complexity is O(n)