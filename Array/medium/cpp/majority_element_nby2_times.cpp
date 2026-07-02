//
// Created by santosh on 12/20/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    int majorityElement(vector<int>& nums)
    {
        int count = 0;
        int majorityElement=nums[0];

        for (int i=0; i<nums.size(); i++)
        {
            if (count==0)
            {
                majorityElement=nums[i];
            }
            if (nums[i]==majorityElement)
            {
                count++;
            } else
            {
                count--;
            }
        }

        for (int i=0; i<nums.size(); i++)
        {
            if (nums[i]==majorityElement)
            {
                count++;
            }
        }

        if (count>nums.size()/2)
        {
            return majorityElement;
        }

        return -1;
    }
};

int main ()
{
    // vector<int> nums={7, 0, 0, 1, 7, 7, 2, 7, 7};
    vector<int> nums={1, 1, 1, 2, 1, 2};
    Solution s;

    cout<<s.majorityElement(nums)<<endl;

}