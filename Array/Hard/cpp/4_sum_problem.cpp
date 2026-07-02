//
// Created by santosh on 1/7/26.
//

#include<bits/stdc++.h>
using namespace std;

// TODO : Write a generic K sum problem
class Solution
{
public:
    vector<vector<int>> findQuadrants(vector<int>& nums,int target)

    {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for (int i = 0; i < nums.size(); i++)
        {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (j>i+1 && nums[j] == nums[j - 1]) continue;

                int left = j + 1;
                int right = nums.size() - 1;

                while (left < right)
                {
                    long long sum = nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target)
                    {
                        result.push_back({nums[i], nums[j], nums[left], nums[right]});
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        left++;
                        right--;
                    }

                    else if (sum > target)
                    {
                        right--;
                    }
                    else
                    {
                        left++;
                    }
                }
            }
        }
        return result;
    }
};

int main()
{
    vector<int> nums = {2,2,2,2,2};
    int target = 8;
    vector<vector<int>> result = Solution().findQuadrants(nums,target);
    for (int i = 0; i < result.size(); i++)
    {
        cout << "[";
        for (int j = 0; j < result[i].size(); j++)
        {
            cout << result[i][j] << " ";
        }
        cout << "]" << endl;
    }
}
