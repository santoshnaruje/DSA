# Leet code problem no 875 

import math

def calucalteTimeTakenToEatEachBanana(files,no_of_bananas):
    total_hours=0
    for bananas in files:
        total_hours += math.ceil(bananas/no_of_bananas)

    return total_hours


def getTheMinimumNoOfHoursToEatAllBananas(files, minimum_hours):

    low = 1;
    high = max(files)

    while(low < high):
        mid = int(low + (high-low)/2)

        time_taken = calucalteTimeTakenToEatEachBanana(files,mid)

        if(time_taken <= minimum_hours):
            high = mid;
        else:
            low = mid +1

    return low



if __name__ == '__main__':
    N = 4,
    a = [3,6,7,11]
    h = 8
    result = getTheMinimumNoOfHoursToEatAllBananas(a,h)
    print(result)



