class Solution(object):
    def isPalindrome(self, x):
        i = 0
        rem = 0
        if x < 0:
            return False
        digit = 0
        temp = x
        while temp != 0:
            rem = temp % 10
            digit = digit * 10 + rem
            temp = temp // 10
        if x == digit:
            return True
        else:
            return False
