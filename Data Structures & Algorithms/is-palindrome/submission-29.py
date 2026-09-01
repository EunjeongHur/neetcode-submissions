class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        fi = 0
        li = len(s) - 1

        while fi < li:
            while fi < li and not s[fi].isalnum():
                fi += 1
            while li > fi and not s[li].isalnum():
                li -= 1
            
            if s[fi].lower() != s[li].lower():
                return False
            fi += 1
            li -= 1

        return True
                