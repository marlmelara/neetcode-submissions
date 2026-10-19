class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringX = str(x)

        left, right = 0, len(stringX) - 1

        while left < right:
            if stringX[left] != stringX[right]:
                return False

            left += 1
            right -= 1

        return True