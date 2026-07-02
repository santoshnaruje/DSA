//
// Created by santosh on 12/30/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:

    static int getMinimumElementInArotatedSortedArrayWithDuplicates(vector<int> nums)
    {
        int low = 0, high = nums.size()-1;
        while (low<high)
        {
            int mid= low + (high-low)/2;

            if (nums[low] == nums[mid] && nums[mid] == nums[high])
            {
                low++;
                high--;
                continue;
            }

            if (nums[mid] > nums[high])
            {
                low = mid+1;
            } else
            {
                high = mid;
            }
        }

        return nums[low];

    };


    static int getMinimumElementInArotatedSortedArray(vector<int> nums)
    {
        int low = 0, high = nums.size()-1;
        while (low<high)
        {
            int mid= low + (high-low)/2;
            if (nums[mid]>nums[high])
            {
                low = mid+1;
            } else
            {
                high = mid;
            }
        }

        return nums[low];

    };
};

int main()
{
    vector<int> nums = {4,5,1,2,3};
    Solution s;
    cout<<s.getMinimumElementInArotatedSortedArray(nums)<< endl;
}

