//
// Created by santosh on 12/8/25.
//


#include<bits/stdc++.h>
using namespace std;

bool checkArrayIsSorted(vector<int>& nums)
{
    bool ascending = true;
    bool descending = true;
    for (int i = 0; i < nums.size() - 1; i++)
    {
        if (nums[i] > nums[i + 1])
        {
            ascending = false;
        }
        if (nums[i] < nums[i + 1])
        {
            descending = false;
        }
    }
    return ascending || descending;
}

int main()
{
    vector<int> nums = {5, 4, 6, 7, 8};
    bool ans = checkArrayIsSorted(nums);
    cout << ans << endl;
}

