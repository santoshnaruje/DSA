//
// Created by santosh on 12/20/25.
//

#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    vector<int> rearrangeArray(vector<int> &nums)
    {
        vector<int> ans(nums.size());
        int pos = 0, neg = 1;

        for (int x : nums) {
            if (x > 0) {
                ans[pos] = x;
                pos += 2;
            } else {
                ans[neg] = x;
                neg += 2;
            }
        }
        return ans;

    }

};

int main()
{
    Solution s;
    vector<int> nums ={3,1,-2,-5,2,-4};
    vector<int> res=s.rearrangeArray(nums);
    for (int num:res)
    {
        cout<<num<<" ";
    }
    cout<<endl;
}
