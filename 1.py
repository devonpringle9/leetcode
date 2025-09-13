class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		for i_index, i in enumerate(nums):
			for j_index, j in enumerate(nums):
				if i_index == j_index:
					continue
				if i + j == target:
					return [i_index, j_index]

print(Solution().twoSum([2, 7, 11, 15], 9))