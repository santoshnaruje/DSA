//
// Created by santosh on 12/5/25.
//

#include<bits/stdc++.h>
using namespace std;

int largestElement(vector<int>& nums) {


    int largestElement = INT_MIN;
    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i] > largestElement)
        {
            largestElement = nums[i];
        }
    }
    return largestElement;

}

int main()
{
    vector <int> v(1000);
    iota(v.begin(), v.end(), 0);

    int largest_element=largestElement(v);
    cout<<largest_element<<endl;
}