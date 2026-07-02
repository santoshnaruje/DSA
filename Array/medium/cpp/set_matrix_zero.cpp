//
// Created by santosh on 12/20/25.
//

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    void setMatrixZeroBruteForce(vector<vector<int> > &matrix)
    {
        int m= matrix.size();
        int n = matrix[0].size();
        vector<pair<int,int>> zeros;
        for (int i=0; i<m; i++)
        {
            for (int j=0; j<n; j++)
            {
                if (matrix[i][j]==0)
                {
                    zeros.push_back({i,j});
                }
            }
        }

        for (int i=0 ; i<zeros.size() ; i++)
        {
            int row = zeros[i].first;
            int col = zeros[i].second;

            for (int k=0; k<n; k++)
            {
                matrix[row][k]=0;
            }

            for (int k=0; k<m; k++)
            {
                matrix[k][col]=0;
            }
        }

    }
};

int main()
{
    vector<vector<int>> matrix = {
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1}
    };

    Solution s;
    s.setMatrixZeroBruteForce(matrix);

    for (int i=0; i<matrix.size(); i++)
    {
        for (int j=0; j<matrix[0].size(); j++)
        {
            cout<<matrix[i][j]<<" ";
        }
        cout<<endl;
    }
}