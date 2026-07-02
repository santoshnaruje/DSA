//
// Created by santosh on 12/21/25.
//

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxCount(vector<int>& nums) {
        int n = nums.size();

        // Find first positive index
        int left = 0, right = n - 1;
        int firstPos = n;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > 0) {
                firstPos = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        // Find first zero index
        left = 0, right = n - 1;
        int firstZero = n;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >=0) {
                firstZero = mid;
                right = mid - 1;
            } else if (nums[mid] < 0) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return max(firstZero, n-firstPos);
    }
};


int main()
{
    Solution s;
    vector<int> nums = {-2, -1, -1, 1, 2, 3};
    cout << s.maxCount(nums) << endl;
}
