def check_adjacent_flowers_tomake_bouquets(roses_blooms_on_days, mid, k, m):
    count = 0
    bouquets = 0
    for rose in roses_blooms_on_days:
        if rose <= mid:
            count += 1
            if count == k:
                bouquets += 1
                count = 0
        else:
            count = 0
    return bouquets >= m


def get_min_no_of_days_to_make_bouquet(bloomDay, m, k):
    left = min(bloomDay)
    right = max(bloomDay)
    while left < right:

        mid = left + (right - left) // 2
        if check_adjacent_flowers_tomake_bouquets(bloomDay, mid, k,m):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    roses_blooms_on_days = [7, 7, 7, 7, 13, 11, 12, 7]
    no_of_bouquets = 2
    required_ajacent_roses = 3
    print(get_min_no_of_days_to_make_bouquet(roses_blooms_on_days, no_of_bouquets, required_ajacent_roses))
