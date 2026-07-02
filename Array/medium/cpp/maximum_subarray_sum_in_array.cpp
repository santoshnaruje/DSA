//
// Created by santosh on 12/20/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxSubarraySum(vector<int>& nums)
    {
        int sum = 0;
        int maxSum = INT_MIN;
        int start = 0;
        int end = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (sum == 0)
            {
                start = i;
            }
            sum += nums[i];   
            if (sum > maxSum){
            {
                maxSum = sum;
                end = i;
            }

            if (sum < 0)
            {
                sum = 0;
            }
        }
        cout << start <<" " << end<< endl;
        return maxSum;
    };
};

int main()
{
    vector<int> nums = {2, 3, 5, -2, 7, -4};
    Solution obj;
    int maxSum = obj.maxSubarraySum(nums);
    cout << maxSum << endl;
}
