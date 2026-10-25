class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftWindow = 0
        rightWindow = 1

        answer = -10_000_001

        while answer != target:
            answer = nums[leftWindow] + nums[rightWindow]
            if answer == target:
                return [leftWindow, rightWindow]
            
            if rightWindow < len(nums) - 1:
                rightWindow += 1
            else:
                leftWindow += 1
                rightWindow = leftWindow + 1
                