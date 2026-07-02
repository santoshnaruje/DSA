
//
// Created by santosh on 12/31/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    static int singleNonDuplicate(const vector<int>& nums)
    {

        if (nums.size()==1)
        {
            return nums[0];
        }

        if (nums[0] != nums[1])
        {
            return nums[0];
        }

        if (nums[nums.size()-1] != nums[nums.size()-2])
        {
            return nums[nums.size()-1];
        }

        int low = 1;
        int high = nums.size()-2;

        while (low<=high)
        {
            int mid = low + (high-low)/2;

            if (nums[mid]!= nums[mid-1] && nums[mid]!= nums[mid+1])
            {
                return nums[mid];
            }

            if ( (mid%2==0 && nums[mid]== nums[mid+1]) || (mid%2==1 && nums[mid]== nums[mid-1]) )
            {
                low = mid+1;
            }
            else
            {
                high = mid-1;
            }

        }
        return -1;

    }
};
int main()
{
    vector<int> nums = {3,3,7,7,10,11,11
};
    Solution s;
    cout<< s.singleNonDuplicate(nums)<<endl;


}
