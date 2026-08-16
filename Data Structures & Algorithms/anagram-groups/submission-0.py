# count = (1, 0, 1, 0, ..., 1, .. 0)

# result[tuple(count)].append(s)

# result = {(1, 0, 1, 0): ["cat"]}

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()


# defaultdict 를 쓰는 이유는 becasue you are unsure if the key already exists or not. 
# For example, if you don't use defaultdict and use dict(), then you have to make sure
# if there's key already in use before you APPEND the item. By using defaultdict, you 
# don't need to check everytime and it's very convenient. 

# Example Code:
# b = dict()
# if 'key' not in b:
#     b['key'] = []
# b['key'].append(1)
# print(b)  # Output: {'key': [1]}