def sumNumbers(n: int) -> int:
    """
    sumNumbers returns the sum of all numbers in range 1 to n
    TIME COMPLEXITY: O(n) -> n
    SPACE COMPLEXITY: O(1) -> constant time
    """
    currSum = 0
    for num in range(1, n+1):
        currSum += num
    return currSum


print(f"Input 10, Sum = {sumNumbers(10)}")
print(f"Input 10000, Sum = {sumNumbers(10000)}")
print(f"Input 1000000, Sum = {sumNumbers(1000000)}")
print(f"Input 1000000000, Sum = {sumNumbers(1000000000)}")