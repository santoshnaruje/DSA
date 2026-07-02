//
// Created by santosh on 12/1/25.
//
#include<bits/stdc++.h>
using namespace std;

vector<int> missing_elements_method1(vector<int> nums)
{
    vector<int> result;
    for (int i = 0; i < nums.size() - 1; i++)
    {
        if (nums[i + 1] - nums[i] != 1)
        {
            int j = nums[i] + 1;
            while (j < nums[i + 1])
            {
                result.push_back(j);
                j++;
            }
        }
    }

    return result;
}

vector<int> missing_elements_method2(vector<int> nums)
{
    vector<int> result;
    int max_el = *max_element(nums.begin(), nums.end());
    int min_el = *min_element(nums.begin(), nums.end());
    vector<int> hash_map(max_el + 1, 0); // all initialized to 0
    for (int i = 0; i < nums.size() - 1; i++)
    {
        hash_map[nums[i]]++;
    }

    for (int i = min_el; i < hash_map.size()-1; i++)
    {
        if (hash_map[i] == 0)
        {
            result.push_back(i);
        }
    }
    return result;
}

int main()
{
    vector<int> nums = {1, 2, 3, 6, 7, 8, 12, 24};
    vector<int> all_Missing_elements_from_method1 = missing_elements_method1(nums);
    cout << "Missing elements are method 1: ";
    for (int all_Missing_element : all_Missing_elements_from_method1)
    {
        cout << all_Missing_element << " ";
    }
    cout << endl;

    vector<int> all_Missing_elements_from_method2 = missing_elements_method2(nums);
    cout << "Missing elements are meethod 2 : ";
    for (int all_Missing_element : all_Missing_elements_from_method2)
    {
        cout << all_Missing_element << " ";
    }
}


// Time complexity - o(n+m)
// n - is all the elements in an array
// m - missing elements in an array
// worst case {0,10000) - o(m)

//Space Complexity:
//➡️ O(M)
// Where M is the number of missing elements.
//Except that, I only use a few extra variables → constant space.

