class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sum_map={}

        for i, num in enumerate(nums):
            find_val=target - num
            if find_val in sum_map:
                i2=sum_map.get(find_val)
                return [i2, i]
            else:
                sum_map[num] = i
        

