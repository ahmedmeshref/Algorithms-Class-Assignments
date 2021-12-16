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

# Questions:
# 1- When you say write an algorithm, do you mean a pseudocode of each problem?
# 2- How do I show testing?
# 3- Where should I write the runtime?
# 4- Should I comment every command?
# 5- Input and output format for question 2?
# 6- Change the key to be 3 instead of 2, which algorithms among the two (the algorithm that has the key of 2 and the
#       algorithm that has the key of 3) will tend to run slow (and which one will tend to run fast). ***
