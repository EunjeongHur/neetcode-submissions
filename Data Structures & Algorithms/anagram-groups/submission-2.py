class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}

        for string in strs:
            count = [0] * 26
            for s in string:
                index=ord(s) - 97
                count[index] = count[index] + 1
            
            key = tuple(count)
            if key in group:
                group[key].append(string)
            else:
                group[key] = [string]

        all_values = list(group.values())
        return all_values
