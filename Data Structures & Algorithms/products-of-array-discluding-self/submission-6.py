class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #[1,2,4,6]
        res = [1] * (len(nums)) # [1, 1, 1, 1]

        for i in range(1, len(nums)): 
            res[i] = res[i-1] * nums[i-1]

        # i = 1, res[1] = res[0] (1) * nums[0] (1) => 1
        # i = 2, res[2] = res[1] (1) * nums[1] (2) => 2
        # i = 3, res[3] = res[2] (2) * nums[2] (4) => 8

        #res = [1, 1, 2, 8]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #3에서 0까지 하나씩 내려감
            res[i] *= postfix 
            postfix *= nums[i]
        
        # i = 3, res[3] = res[3] (8) * postfix (1) => 8 / postfix = postfix (1) * nums[3] (6) => 6
        # i = 2, res[2] = res[2] (2) * postfix (6) => 12 / postfix = postfix (6) * nums[2] (4) => 24
        # i = 1, res[1] = res[1] (1) * postfix (24) => 24 / postfix = postfix (24) * nums[1] (2) => 48
        # i = 0, res[0] = res[0] (1) * postfix (48) => 48 / postfix = postfix (48) * nums[0] (1) => 48

        return res