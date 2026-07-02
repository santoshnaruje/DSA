//
// Created by santosh on 12/19/25.
//


#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    void selectionSort(vector<int>& nums)
    {

        for (int i =0; i<nums.size(); i++)
        {
            for (int j=i+1; j<nums.size(); j++)
            {
                if (nums[i] > nums[j])
                {
                    swap(nums[i], nums[j]);
                }
            }
        }
    }


    void dutchNationalFlagAlgorithm(vector<int>& nums)
    {



        int left = 0;
        int high = nums.size()-1;
        int mid= 0;

        while (mid<=high)
        {
            if (nums[mid] ==0)
            {
                swap(nums[left],nums[mid]);
                left++;
                mid++;
            }
            else if (nums[mid] ==1)
            {
                mid++;
            }
            else if (nums[mid] ==2)
            {
                swap(nums[mid],nums[high]);
                high--;
            }
        }
    }
};


int main()
{
    Solution s;
    vector<int> nums={2,0,2,1,1,0};

    s.dutchNationalFlagAlgorithm(nums);
    for (int i=0; i<nums.size(); i++)
    {
        cout<<nums[i]<<" ";
    }
}