//
// Created by santosh on 12/4/25.
//

#include<bits/stdc++.h>
using namespace std;

vector<int> leftRotateArrayByK(vector<int>& nums, int k)
{
    int n = nums.size();
    k = k % n;
    vector<int> res(k);
    for (int i = 0; i < k; i++)
    {
        res[i] = nums[i];
    }
    int j = 0;
    int i = k;
    for (; i < n; i++)
    {
        nums[j] = nums[i];
        j++;
    }
    for (const int el : res)
    {
        nums[j] = el;
        j++;
    }
    return nums;
}

vector<int> rightRotatreArrayByK(vector<int>& nums, int k)
{
    int n = nums.size();
    k = k % n;
    vector<int> res(k);

    for (int i = 0, j = n - k; i < k; i++, j++)
    {
        res[i] = nums[j];
    }

    for (int i = n - k - 1; i >= 0; i--)
    {
        nums[i + k] = nums[i];
    }

    for (int i = 0; i < k; i++)
    {
        nums[i] = res[i];
    }

    return nums;
}

void optimalRotateArrayByK(vector<int>& nums, int k)
{
    int n = nums.size();
    k = k % n;
    // Step 1: Reverse entire array
    reverse(nums.begin(), nums.end());

    // Step 2: Reverse first k elements
    reverse(nums.begin(), nums.begin() + k);

    // Step 3: Reverse last n-k elements
    reverse(nums.begin() + k, nums.end());
}

// Left rotate by k
void optimalLeftRotateArrayByK(vector<int>& nums, int k)
{
    int n = nums.size();
    if (n == 0) return;

    k = k % n; // handle large k

    // Step 1: Reverse first k elements
    reverse(nums.begin(), nums.begin() + k);

    // Step 2: Reverse last n-k elements
    reverse(nums.begin() + k, nums.end());

    // Step 3: Reverse the whole array
    reverse(nums.begin(), nums.end());
}


void swapByPointer(int* firstPointer, int* secondPointer)
{
    int temp = *firstPointer;
    *firstPointer = *secondPointer;
    *secondPointer = temp;
}

void reverseByIterators(int* firstPointer, int* lastPointer)
{
    while (firstPointer != lastPointer && firstPointer != --lastPointer)
    {
        swapByPointer(firstPointer, lastPointer);
        firstPointer++;
    }
}

void swap(int& a, int& b) noexcept
{
    int temp = a;
    a = b;
    b = temp;
}

void reverseWholeArray(vector<int>& nums)
{
    int n = nums.size();
    int i = 0, j = n - 1;
    while (i < j)
    {
        swap(nums[i], nums[j]);
        i++;
        j++;
    }
}

void reversePartOfArray(vector<int>& nums, int start, int end)
{
    while (start < end)
    {
        swap(nums[start], nums[end]);
        start++;
        end++;
    };
}

int main()
{
    vector<int> nums = {1, 2, 3, 4};
    int k = 3;
    reverseByIterators(nums.data(), nums.data() + 4);
}


// int main()
// {
//     vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
//     int k = 3;
//
//     const vector<int> res = rightRotatreArrayByK(nums, k);
//     for (int re : res)
//     {
//         cout << re << " ";
//     }
// }

// left or right rotate an array by applying the brute force method always gives the
// Time complexity of O(k)+O(n-k)+o(k) -> O(n+k)
// Space complexity O(k) as we are storing the k elements in a separate array
