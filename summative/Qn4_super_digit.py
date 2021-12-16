def calcSuperDigit(num: str) -> int:
    # base case: num has only one digit
    if len(num) == 1:
        return int(num)

    # Calculate the summation of all digits of num
    digitsSum = 0
    for digit in num:
        digitsSum += int(digit)
    # Recursively call calcSuperDigit on the summation obtained
    return calcSuperDigit(str(digitsSum))


def superDigit(num: str, k: int) -> int:
    """
    superDigit calculates the superDigit of a giving number
    string num: a string representation of an integer
    int k: the times to concatenate n to make p.
    TIME COMPLEXITY: O(n*k) -> n is the length of num
    SPACE COMPLEXITY: O(1)
    """
    # If nums has only 1 digit, return the number
    if len(num) == 1:
        return int(num)
    else:
        # Calculate p by combining num, k times.
        p = num * k
        # Compute super digits of the obtained p
        return calcSuperDigit(p)


if __name__ == "__main__":
    # Test case 1
    ans1 = superDigit("9875", 4)
    if ans1 == 8:
        print("Test Case 1: Successes")
    else:
        print(f"Test Case 1: Failed. Expected value: 8, Actual val: {ans1}")

    # Test case 2
    ans2 = superDigit("148", 3)
    if ans2 == 3:
        print("Test Case 2: Successes")
    else:
        print(f"Test Case 2: Failed. Expected value: 3, Actual val: {ans2}")
