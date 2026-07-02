//
// Created by santosh on 12/1/25.
//


#include<bits/stdc++.h>
using namespace std;

pair<int, int> getMinAndMaxInAnArray(const vector<int>& arr)
{
    auto mn = INT_MAX;
    auto mx = INT_MIN;
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] > mx)
        {
            mx = arr[i];
        }
        else if (arr[i] < mn)
        {
            mn = arr[i];
        }
    }
    return {mn, mx};
};

int main()
{
    auto arr = {6, 3, 8, 10, 16, 7, 5, 2, 9, 14};
    auto [mn, mx] = getMinAndMaxInAnArray(arr);
    cout << "MINIMUM" <<  mn << endl;
    cout << "MAXIMUM" << mx << endl;
}
