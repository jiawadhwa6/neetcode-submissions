class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int prev = 0;
        for (int i = 1; i< nums.size(); i++)
        {
            if (nums[prev] == nums[i])
            {
                return true;
            }
            prev++;
        }
    }
};
