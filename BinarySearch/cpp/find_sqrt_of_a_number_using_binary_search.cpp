//
// Created by santosh on 12/31/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    int findSqrt(int n)
    {

        int left = 1;
        int right = n/2;
        int ans = -1;

        while(left<=right)
        {
            int mid = left+(right-left)/2;

            if (mid*mid <=n)
            {
                ans=mid;
                left=mid+1;
            }
            if (mid*mid>n)
            {
                right = mid-1;
            }
        }

        return ans;

    };
};

int main()
{
    int n = 36;
    Solution obj;
    cout<<obj.findSqrt(n/2)<<endl;


}