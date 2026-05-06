#include <iostream>
#include <vector>

class Solution {
public:
  std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::vector<int> indices = {0, 1};
    for (int i = 0; i < nums.size(); i++) {
      for (int j = 0; j < nums.size(); j++) {
        if (i == j) {
          continue;
        } else {
          if (nums[i] + nums[j] == target) {
            indices[0] = i;
            indices[1] = j;
          }
        }
      }
    }
		return indices;
  }
};

int main() {
  std::vector<int> nums = {2,7,11,15};
  int target = 9;
  Solution ret;

  for (int i : ret.twoSum(nums, target)) {
    std::cout << i;
  }
};