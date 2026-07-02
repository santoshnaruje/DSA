//
// Created by santosh on 12/9/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    void moveZerosTotheEnd(vector<int>& nums)
    {
        vector<int> res;
        int count = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] != 0)
            {
                res.push_back(nums[i]);
                count++;
            }
        }

        for (int i = 0; i < count; i++)
        {
            nums[i] = res[i];
        }
        for (int i = count; i < nums.size(); i++)
        {
            nums[i] = 0;
        }
    }

    void movezerosTotheEndByOptimal(vector<int>& nums)
    {
        int i, j;
        i = 0;
        j = 0;
        while (j < nums.size())
        {
            if (nums[j] == 0)
            {
                j++;
            }
            else
            {
                swap(nums[i], nums[j]);
                i++;
                j++;
            }
        }
    }
};

int main()
{
    vector<int> nums = {1, 0, 2, 3, 0, 4, 0, 1};
    Solution s;
    s.movezerosTotheEndByOptimal(nums);
}
