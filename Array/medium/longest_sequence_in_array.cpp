//
// Created by santosh on 12/21/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:

    int getLongestSequence(vector<int> &nums)
    {
        unordered_set<int> uniqueElements;
        int longestSequence=INT_MIN;
        int count=0;

        for(auto num:nums){
            uniqueElements.insert(num);
        }

        for(auto num : uniqueElements){
            if(uniqueElements.find(num-1)==uniqueElements.end()){
                count=1;
                int x=num;
                while(uniqueElements.find(x+1)!=uniqueElements.end()){
                    count++;
                    x+=1;
                }
                longestSequence= max(longestSequence, count);
            }
        }

        return longestSequence;

    }

};


int main()
{
    Solution s;
    vector<int> nums={100,4,200,1,3,2};
    cout<< s.getLongestSequence(nums);
}