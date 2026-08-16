class Solution:
    def isPalindrome(self, s: str) -> bool:
        # test_string = ''.join(letter for letter in s if letter.isalnum())
        # print(type(test_string))
        newString = s.replace(" ", "").lower()
        resultString = ""
        for c in newString:
            if c.isalnum():
                resultString += c

        
        left = 0
        right = -1
        print(resultString)
        print(len(resultString)/2)
        while left < (len(resultString)/2):
            if resultString[left] == resultString[right]:
                left += 1
                right -=1
            else:
                return False
            

        return True