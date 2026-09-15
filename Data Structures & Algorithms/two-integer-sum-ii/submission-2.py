class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        res = []

        while left_pointer < right_pointer:
            if (numbers[left_pointer] + numbers[right_pointer]) > target:
                right_pointer -= 1
                continue
            elif (numbers[left_pointer] + numbers[right_pointer]) < target:
                left_pointer += 1
                continue
            elif (numbers[left_pointer] + numbers[right_pointer]) == target:
                res.append(left_pointer + 1)
                res.append(right_pointer + 1)

                return res

        return []