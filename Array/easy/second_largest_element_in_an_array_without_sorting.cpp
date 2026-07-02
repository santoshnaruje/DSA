//
// Created by santosh on 12/5/25.
//

#include<bits/stdc++.h>
using namespace std;

int secondLargestElement(vector<int>& nums)
{
    int smallest = INT_MAX;
    int second_smallest = -1;
    int largest = INT_MIN;
    int second_largest = -1;
    for (int i = 0; i < nums.size(); i++)
    {
        // largest and second largest
        if (nums[i] > largest)
        {
            second_largest = largest;
            largest = nums[i];
        }
        else if (nums[i] < largest && nums[i] > second_largest)
        {
            second_largest = nums[i];
        }
        // smallest and second smallest

        if (nums[i] < smallest)
        {
            second_smallest = smallest;
            smallest = nums[i];
        }
        if (nums[i] > smallest && nums[i] < second_smallest)
        {
            second_smallest = nums[i];
        }
    }

}

int main()
{
    vector<int> nums = {
        3, 4, 7, 7, 5, 3, 0,2
    };
    int second_largest = secondLargestElement(nums);
    cout << second_largest << endl;
}
