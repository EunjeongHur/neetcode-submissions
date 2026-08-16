class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)
        for num in nums:
            ans[num] += 1

        sorted_by_values_desc = dict(sorted(ans.items(), key=lambda item: item[1], reverse=True))
        final_result = []
        for i in range(k):
            key_at_index = list(sorted_by_values_desc.keys())[i]
            final_result.append(key_at_index)

        return final_result