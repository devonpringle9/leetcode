class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		adds_to = {}
		for i_index, i in enumerate(nums):
			if i in adds_to:
				return [i_index, adds_to[i]]
			adds_to[target - i] = i_index

print(Solution().twoSum([2, 7, 11, 15], 9))