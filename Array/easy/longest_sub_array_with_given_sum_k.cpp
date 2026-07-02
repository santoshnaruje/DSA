//
// Created by santosh on 12/17/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int getLongestSubArrayWithSumkUsingHashMap(int nums[], int k, int n)
    {
        int max_sub_array = 0;
        int sum=0;
        unordered_map<int, int> mp;
        for (int i = 0; i < n; i++)
        {
            sum += nums[i];
            int remaining = sum - k ;
            if (sum==k)
            {
                max_sub_array = max(max_sub_array, i + 1);
            }
            if (mp.find(remaining) != mp.end())
            {
                max_sub_array=max(max_sub_array,i - mp[remaining]);
            }

            if (mp.find(sum) == mp.end())
            {
                mp[sum]=i;
            }


        }
        return max_sub_array;

    };

    int getLongestSubArrayWithSumK(int nums[], int k, int n)
    {
        int i = 0;
        int j = 0;
        int max_sub_array = 0;
        int sum = 0;
        while (j < n)
        {
            sum += nums[j];
            while ( i<j && sum > k)
            {
                sum -= nums[i];
                i++;
            }

            if (sum == k)
            {
                max_sub_array = max(max_sub_array, j - i + 1);
            }
            j++;
        }
        return max_sub_array;
    }

    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int , int> mp;
        for(int i=0 ; i<nums.size(); i++){
            int needed= target-nums[i];
            if(mp.find(needed) != mp.end()){
            return {mp[needed], i};
            };
            if(mp.find(nums[i])==mp.end()){
                mp[nums[i]]=i;
            }
        }
        return {-1,-1};

    }};


int main()
{
    Solution s;
    vector<int> nums = {2,7,11,15};
    int k = 9;
    int n = (sizeof(nums) / sizeof(nums[0]));
    vector<int>  res = s.twoSum(nums, k);

};


// Leet code related problems for the above approach
// storing prefix sum + frequency map count or index
// | NAME OF THE PROBLEM                                                    | LEETCODE # | APPROACH                                                                                         |
// | ---------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------ |
// | **Two Sum**                                                            | **1**      | Store number as **key** and **index** as value. For each number, check `target - num`.           |
// | **Subarray Sum Equals K**                                              | **560**    | Store **prefix sum → frequency**. Count how many times `(sum - k)` appears.                      |
// | **Maximum Size Subarray Sum Equals K**                                 | **325**    | Store **prefix sum → first index** to get longest length.                                        |
// | **Contiguous Array**                                                   | **525**    | Convert `0 → -1`. Store **prefix sum → first index** to get longest subarray with equal 0s & 1s. |
// | **Binary Subarrays With Sum**                                          | **930**    | Store **prefix sum → frequency** to count subarrays with sum = goal.                             |
// | **Subarray Sums Divisible by K**                                       | **974**    | Store **remainder → frequency** of prefix sums modulo `k`.                                       |
// | **Continuous Subarray Sum**                                            | **523**    | Store **remainder → first index**. If same remainder repeats with gap ≥ 2, answer exists.        |
// | **Make Sum Divisible by P**                                            | **1590**   | Store **remainder → index**. Find shortest subarray to remove.                                   |
// | **Longest Well-Performing Interval**                                   | **1124**   | Convert hours > 8 → +1 else −1. Store **prefix sum → index**.                                    |
// | **Maximum Number of Non-Overlapping Subarrays With Sum Equals Target** | **1546**   | Prefix sum + hashmap + greedy reset after match.                                                 |

