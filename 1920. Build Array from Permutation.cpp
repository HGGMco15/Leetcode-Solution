#include <vector>

class Solution {
public:
    std::vector<int> buildArray(const std::vector<int>& nums) {
        std::vector<int> ls;
        for (int x = 0; x < nums.size(); ++x) {
            ls.push_back(nums[nums[x]]);
        }
        return ls;
    }
};
