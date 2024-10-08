#Converting all uppercase to lowercase
#Removing all Non-Alphanumeric Characters
#Needs to be palindrom
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            if not s[r].isalnum():
                r -= 1
            if not s[l].isalnum():
                l += 1
            elif s[r].lower() == s[l].lower():
                r -= 1
                l += 1
            else:
                return False
        return True
