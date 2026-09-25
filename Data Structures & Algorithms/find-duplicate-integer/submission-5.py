class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's cycle detection algorithm
        slow = nums[0]
        fast = nums[0]

        # Find that a cycle is occuring
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # Find beginning of cycle
        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow