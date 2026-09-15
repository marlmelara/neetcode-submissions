class Solution:
    def isPalindrome(self, s: str) -> bool:
        front_pointer = 0
        back_pointer = len(s) - 1

        while front_pointer < back_pointer:
            if not s[front_pointer].isalnum():
                front_pointer += 1
            elif not s[back_pointer].isalnum():
                back_pointer -= 1
            elif ( s[front_pointer].lower() != 
            s[back_pointer].lower() ):
                return False
            else:
                front_pointer += 1
                back_pointer -= 1

        return True