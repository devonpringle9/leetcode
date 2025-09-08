class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		x_str = str(x) if x > 0 else str(x)[1:]
		new_x_str = ""
		length = len(x_str)
		for i, chr in enumerate(x_str):
			new_x_str += x_str[length-i-1]
		return int(new_x_str) if x > 0 else -int(new_x_str)

print(Solution().reverse(-321))
print(Solution().reverse(321))
print(Solution().reverse(120))
