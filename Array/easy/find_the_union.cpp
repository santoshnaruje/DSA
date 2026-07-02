//
// Created by santosh on 12/10/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> unionByMap(vector<int>& m, vector<int>& n)
    {
        map<int, int> freq;
        vector<int> Union;
        for (auto element : m)
        {
            freq[element]++;
        }
        for (auto element : n)
        {
            freq[element]++;
        }

        for (auto element : freq)
        {
            Union.push_back(element.first);
        }

        return Union;
    }

    vector<int> unionBySet(vector<int>& m, vector<int>& n)
    {
        set<int> res;
        vector<int> Union;
        for (auto element : m)
        {
            res.insert(element);
        }
        for (auto element : n)
        {
            res.insert(element);
        }
        for (auto element : res)
        {
            Union.push_back(element);
        }

        return Union;
    }

    vector<int> unionBy2Pointers(const vector<int>& arr1, const vector<int>& arr2)
    {
        vector<int> Union;
        int i = 0, j = 0;

        while (i < arr1.size() && j < arr2.size())
        {
            if (arr1[i] < arr2[j])
            {
                if (Union.empty() || Union.back() != arr1[i])
                {
                    Union.push_back(arr1[i]);
                }
                i++;

            }
            else if (arr1[i] > arr2[j])
            {
                if (Union.empty() || Union.back() != arr2[j])
                {
                    Union.push_back(arr2[j]);

                };
                j++;
            }
            else
            {
                Union.push_back(arr1[i]);
                i++;
                j++;
            }
        }
        for (i; i < arr1.size(); i++)
        {
            Union.push_back(arr1[i]);
        }
        for (j; j < arr2.size(); j++)
        {
            Union.push_back(arr2[j]);
        }
        return Union;
    }

};


int main()
{
    vector<int> m = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    vector<int> n = {2, 3, 4, 4, 5, 11, 12};

    Solution s;
    vector<int> mapRes = s.unionByMap(m, n);
    for (auto element : mapRes)
    {
        cout << element << " ";
    }
    cout << endl;
    vector<int> setRes = s.unionBySet(m, n);
    for (auto element : setRes)
    {
        cout << element << " ";
    }
    cout << endl;
    vector<int> twoPointersRes = s.unionBy2Pointers(m, n);
    for (auto element : twoPointersRes)
    {
        cout << element << " ";
    }
}


// Output: {1,2,3,4,5,6,7,8,9,10,11,12}

//These problem can be solved in 3 ways

// MAP
// 1.Create a frequency ordered map and and loop over each array to store the elements in a frequency map it will insert thr elements in a sorted array
// at the end loop over the frequency map and insert into the union array
// TIME COMPLEXITY inserting an element into a ordered map takes O(logn) times
// so here O(m+n)log(m+n)
// space complexity o(max(m,n)) for map and O(m+n) for unique array

// SET
// Insert the elements in a set from both the first array and second array
// insertion of element in a ordered set takes the O(log n) times
// so here the 2 array means O(m+n)log(m+n)
// space complexity o(max(m,n)) for set and O(m+n) for unique array




