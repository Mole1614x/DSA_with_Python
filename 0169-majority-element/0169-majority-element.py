class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for i in freq:
            if freq[i] > len(nums) / 2:
                return i