//
// Created by santosh on 12/30/25.
//

#include<iostream>
#include<vector>
using namespace std;

class Solution
{
    public:
    int getHowManyTimesArrayIsSorted(vector<int> nums)
    {

        int low = 0, high = nums.size()-1;
        while (low<high)
        {
            int mid = low + (high-low)/2;
            if (nums[mid] > nums[high])
            {
                low = mid+1;
            } else
            {
                high = mid;
            }
        }

        return low;

    }
};

int main()
{
    Solution s;
    vector<int> nums = {4,5,6,7,0,1,2,3};
    cout << s.getHowManyTimesArrayIsSorted(nums) << endl;
}