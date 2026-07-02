//
// Created by santosh on 12/21/25.
//

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int lower_bound(vector<int>& nums, int target, int low, int high)
    {
        if (low > high)
        {
            return low;
        }

        int mid = low + (high - low) / 2;

        if (nums[mid] >= target)
        {
            return lower_bound(nums, target, low, mid - 1);
        }
        return lower_bound(nums, target, mid + 1, high);
    }

    int upper_bound(vector<int>& nums, int target, int low, int high)
    {
        if (low > high)
        {
            return low;
        }
        int mid = low + (high - low) / 2;
        if (nums[mid] > target)
        {
            return upper_bound(nums, target, low, mid - 1);
        }
        return upper_bound(nums, target, mid + 1, high);
    }

    int searchInsert(vector<int>& nums, int target,int low, int high)
    {
        if (low > high)
        {
            return low;
        }

        int mid= low + (high - low) / 2;

        if (nums[mid]>=target)
        {
            return lower_bound(nums, target, low, mid - 1);
        }
        return lower_bound(nums, target, mid + 1, high);

    }

    int floorValue(vector<int>& nums, int target, int low, int high)
    {
       return  nums[this->upper_bound(nums, target, low, high)-1];
    }

    int ceilValue(vector<int>& nums, int target, int low, int high)
    {
        return  nums[this->lower_bound(nums, target, low, high)];
    }

    int lastOccurenceInSortedArray(vector<int>& nums, int target, int low, int high)
    {
        int lastOccurenceIndex = this->lower_bound(nums, target, low, high);
        if (nums[lastOccurenceIndex] >= target)
        {
            return lastOccurenceIndex;
        }
        else return -1;

    }



};


int main()
{
    vector<int> nums = {3, 4, 13, 13, 13, 20, 40};
    int target = 60;
    int low =0;
    int high = nums.size()-1;
    Solution s;
    // cout << "Lower bound is "<<  s.lower_bound(nums,target,low,high)<<endl;
    // cout << "Upper bound is " << s.upper_bound(nums,target,low,high)<<endl;
    // cout<< "Search insert is " << s.searchInsert(nums, 5, low,high ) << endl;
    // cout << "ceil value is "<< s.ceilValue(nums, target, low, high) << endl;
    // cout << "floor Value is "<< s.floorValue(nums, target, low, high) << endl;
    cout << "Last occurence of index " <<s.lastOccurenceInSortedArray(nums, target, low, high) << endl;

}