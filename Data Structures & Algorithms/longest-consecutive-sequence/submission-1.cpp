class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size()== 0)
        {return 0;}

        sort(nums.begin(),nums.end());
        int curr = 1;
        int max = 1;
        for (int i = 1; i<nums.size(); i++)
        {
            if (nums[i-1] + 1 == nums[i])
            {
                curr++;
                cout<<nums[i]<<" : "<<curr << "\n";
            }
            else if (nums[i-1] == nums[i])
            {continue;}

            else if (nums[i-1] != nums[i]+1)
            {
                max = std::max(curr, max);
                curr = 1;
            }
        }
        return std::max(max,curr);
        
    }
};
