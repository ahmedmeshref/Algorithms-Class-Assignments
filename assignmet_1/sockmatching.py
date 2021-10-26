def matchingSocks(n, colors_arr):
    total_matched = 0
    one_pair = set()

    for pair in colors_arr:
        if pair in one_pair:
            total_matched += 1
            one_pair.remove(pair)
        else:
            one_pair.add(pair)

    return total_matched


# Test Cases
if __name__ == '__main__':
    # Test Case #1
    arr = [1, 2, 1, 3, 4, 2, 5, 4, 1, 3]
    ans = matchingSocks(10, arr)
    print(f"Answer for test #1: arr of colors= {arr}, total paris found= {ans}")

    # Test Case #2
    arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    ans = matchingSocks(9, arr)
    print(f"Answer for test #2: arr of colors= {arr}, total paris found= {ans}")

    # Test Case #3
    arr = [1, 2, 1, 2, 1, 3, 2]
    ans = matchingSocks(7, arr)
    print(f"Answer for test #3: arr of colors= {arr}, total paris found= {ans}")

    # Test Case #4
    arr = [1, 2]
    ans = matchingSocks(2, arr)
    print(f"Answer for test #3: arr of colors= {arr}, total paris found= {ans}")
