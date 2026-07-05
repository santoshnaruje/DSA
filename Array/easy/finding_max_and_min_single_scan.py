# Find min and max in a single scan
# Created by santosh

def get_min_and_max_in_an_array(arr: list[int]) -> tuple[int, int]:
    mn = float('inf')
    mx = float('-inf')
    for val in arr:
        if val > mx:
            mx = val
        elif val < mn:
            mn = val
    return mn, mx


if __name__ == "__main__":
    arr = [6, 3, 8, 10, 16, 7, 5, 2, 9, 14]
    mn, mx = get_min_and_max_in_an_array(arr)
    print("MINIMUM", mn)
    print("MAXIMUM", mx)
