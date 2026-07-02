//
// Created by santosh on 12/31/25.
//


#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long calculateTimeTakenToEatEachBanana(vector<int>& piles, int bananas_per_hour) {
        long long total_hours = 0;

        for (int bananas : piles) {
            // ceil(bananas / bananas_per_hour) using integer math
            total_hours += (bananas + bananas_per_hour - 1) / bananas_per_hour;
        }

        return total_hours;
    }

    int getTheMinimumNoOfHoursToEatAllBananas(vector<int>& piles, int minimum_hours) {
        int low = 1;
        int high = *max_element(piles.begin(), piles.end());

        while (low < high) {
            int mid = low + (high - low) / 2;

            long long time_taken = calculateTimeTakenToEatEachBanana(piles, mid);

            if (time_taken <= minimum_hours) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return low;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        return getTheMinimumNoOfHoursToEatAllBananas(piles, h);
    }
};


int main()
{
    Solution s;
    vector<int> piles={};
}