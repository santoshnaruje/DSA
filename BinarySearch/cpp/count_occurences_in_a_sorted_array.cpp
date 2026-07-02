//
// Created by santosh on 12/22/25.
//

#include<bits/stdc++.h>
using namespace std;


class Solution
{
    public:

    int countOfOccurencesInASortedArray(vector<int>& nums, int target)
    {
        int firstOccurence = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        int lastOccurence = upper_bound(nums.begin(), nums.end(), target) - nums.begin();
        return (lastOccurence - firstOccurence);
    };

};

int main()
{
    Solution s;
    vector<int> nums{2, 2 , 3 , 3 , 3 , 3 , 4};
    int target = 3;
    cout<<s.countOfOccurencesInASortedArray(nums, target);
}