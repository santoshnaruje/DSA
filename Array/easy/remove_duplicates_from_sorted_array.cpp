//
// Created by santosh on 12/9/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    static int removeDuplicates(vector<int>& nums)
    {
        int index = 0;
        unordered_set<int> seen;
        for (auto num : nums)
        {
            if (seen.find(num) == seen.end())
            {
                seen.insert(num);
                nums[index] = num;
                index++;
            }
        }
        return index;
    }

    // Time complexity O(n) traversing over the array of elements
    // unordered set lookup and insert takes O(1) time
    // space complexity o(k) for storing the unique elements in set
    // if all the elements are unique then it would go up to O(n)

    static int removeDuplicatesOptimal(vector<int>& nums)
    {
        int i, j;
        i = 0;
        j = 1;
        while (j < nums.size())
        {
            if (nums[i] == nums[j])
            {
                j++;
            }
            else
            {
                i++;
                nums[i] = nums[j];
                j++;
            }
        }
        return i + 1;
    }
};

int main()
{
    vector<int> nums = {1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4};
    Solution s;
    // int k = s.removeDuplicates(nums);
    // cout << k << endl;
    // cout << "Array after removing duplicates" << endl ;
    // for (int i = 0 ; i<k;i++)
    // {
    //     cout << nums[i] << " ";
    // }

    int m = s.removeDuplicatesOptimal(nums);
    cout << m << endl;
    cout << "Array after removing duplicates" << endl;
    for (int i = 0; i < m; i++)
    {
        cout << nums[i] << " ";
    }
}
