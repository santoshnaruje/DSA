//
// Created by santosh on 12/10/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maximumConsecutiveOnes(vector<int>& nums)
    {
        int maxCount = 0;
        int count = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == 0)
            {
                maxCount = max(maxCount, count);
                count = 0;
            }
            else
            {
                count++;
                maxCount = max(maxCount, count);
            }
        }
        return maxCount;
    }
};

int main()
{
    // vector<int> nums = {1, 0, 1, 1, 0, 1};
    vector<int> nums= {1, 1, 0, 1, 1, 1};
    Solution s;

    int res = s.maximumConsecutiveOnes(nums);
    cout << res << endl;
}
