//
// Created by santosh on 12/20/25.
//

#include<bits/stdc++.h>
using namespace std;


class Solution
{
    public:
    vector<int> getLeadersInArray(vector<int>& nums)
    {
        vector<int> result;

        result.push_back(nums[nums.size()-1]);
        int lastElement=nums[nums.size()-1];
        int right=nums.size()-1;
        while (right>=0)
        {
            if (nums[right]>lastElement)
            {
                result.push_back(nums[right]);
                lastElement=nums[right];
            }
            right--;
        }

        reverse(result.begin(), result.end());

        return result;

    }
};
int main()
{
    Solution s;
    vector<int> nums={10, 22, 12, 3, 0, 6};
    vector<int> result = s.getLeadersInArray(nums);
    for (int i=0; i<result.size(); i++)
    {
         cout<<result[i]<<" ";
    }
}