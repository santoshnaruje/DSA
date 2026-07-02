//
// Created by santosh on 1/7/26.
//


#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> findTriplets(vector<int>& nums)
    {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;

        for (int i = 0; i < nums.size(); i++)
        {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1;
            int right = nums.size() - 1;

            while (left < right)
            {
                int tripletsum = nums[i] + nums[left] + nums[right];
                if (tripletsum == 0)
                {
                    ans.push_back({nums[i], nums[left], nums[right]});
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                }
                else if (tripletsum > 0)
                {
                    right--;
                }
                else
                {
                    left++;
                }
            }
        }

        return ans;
    }
};

int main()
{
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    Solution obj;
    const vector<vector<int>> ans = obj.findTriplets(nums);
    for (int i = 0; i < ans.size(); i++)
    {
        cout << "[";
        for (int j = 0; j < ans[i].size(); j++)
        {
            cout << ans[i][j] << " ";
        }
        cout << "]" << endl;
    }
}

