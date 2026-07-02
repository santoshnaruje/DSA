//
// Created by santosh on 12/1/25.
//

// finding a pair of elements in a sorted array

#include<bits/stdc++.h>
using namespace std;

vector<pair<int, int>> pairOfElementsWithSum(vector<int> nums, int k)
{
    vector<pair<int, int>> res;
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = i + 1; j < nums.size(); j++)
        {
            if (nums[i] + nums[j] == k)
            {
                res.emplace_back(nums[i], nums[j]);
            }
        }
    }
    return res;
}

vector<pair<int, int>> pairOfElementsWithSumUsing2Pointer(vector<int> nums, int k)
{
    vector<pair<int, int>> res;
    int i = 0, j = nums.size() - 1;
    while (i <= j)
    {
        if (nums[i] + nums[j] == k)
        {
            res.emplace_back(nums[i], nums[j]);
            i++;
            j--;
        }
        else if (nums[i] + nums[j] > k)
        {
            j--;
        }
        else
        {
            i++;
        }
    }
    return res;
}

vector<vector<int>> pairOfElementsUsingHashMap(vector<int> nums, int k)
{
    vector<vector<int>> res;
    unordered_set<int> seen;
    for (int i = 0; i < nums.size(); i++)
    {
        int x = nums[i];
        int target = k - x;
        if (seen.find(target) != seen.end())
        {
            res.push_back({x, target});
        }
        else
        {
            seen.insert(x);
        }
    }
    return res;
}

template <typename A, typename B>
ostream& operator<<(ostream& os, const pair<A, B>& p)
{
    os << "(" << p.first << ", " << p.second << ")";
    return os;
}

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& v)
{
    os << "[ ";
    for (const auto& x : v) os << x << " ";
    os << "]";
    return os;
}


int main()
{
    vector<int> arr = {6, 3, 8, 10, 16, 7, 5, 2, 9, 14};
    sort(arr.begin(), arr.end());
    int sum = 15;
    // vector<pair<int, int>> res = pairOfElementsWithSumUsing2Pointer(arr, sum);
    vector<vector<int>> res = pairOfElementsUsingHashMap(arr, sum);

    cout << res << endl;
}
