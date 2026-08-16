class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in map_dict:
                stack.append(c)
                continue
            if not stack or stack[-1] != map_dict[c]:
                return False
            stack.pop()
        
        return not stack
        

            