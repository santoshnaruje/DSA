//
// Created by santosh on 12/21/25.
//

#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    int search(vector<int> &nums, int target)
    {
        int l = 0, r = nums.size() - 1;
        while (l <= r)
        {
            int mid = l+(r-l)/2;
            if (nums[mid] == target)
            {
                return mid;
            }
            if (nums[mid] < target)
            {
                l = mid + 1;
            }
            else
            {
                r = mid - 1;
            }
        }
        return -1;
    }
};

int main()
{
    vector<int> arr{1,2,3,4,5,6,7,8,8,8,9,10};
    Solution s;
    int result = s.search(arr,8);
    cout << result << endl;

}