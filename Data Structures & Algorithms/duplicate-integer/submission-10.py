class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Edge case; nums is an empty array
        if len(nums) == 0:
            return False

        has_duplicate = set()

        for num in nums:
            if num in has_duplicate:
                return True
            has_duplicate.add(num)
        
        return False