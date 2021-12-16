"""
function encrypt(text and k):
    create empty stack
    loop i in range(0 to k):
        currCharInd <= i
        while currCharInd is less than the length of text:
            add text[currCharInd] to stack
            currCharInd += k
    cipherText = join the stack elements into a string
    return cipherText


function decrypt(cipherText and k):
    we need to create a new array and loop over each char we have in cipherText and map it to its original index
        in the original text
    create empty array of len(cipherText)
    calculate portion length of each index in range(k)
    calculate the number of complete portions; if a string has 10 chars and k = 3, then only the first portion will
        have 4 chars
    create a variable, currInd <= 0, to map to the index of the current char in cipherText
    loop over key in range(k):
        currOrigialChar <= key to map to the original char of the curr cipherText char
        if there is any completePortions and completePortions is less than current key:
            numChars in the current portion is portionLength - 1
        else:
            numChars = portionLength
        loop j in the range of range(numChars):
            replace textArr[originalCharInd] <= cipherText[currInd]
            currInd += 1
            originalCharInd += k
    originalText = join the stack elements into a string
    return originalText
"""
import math


def encrypt(text: str, k: int) -> str:
    """
    encrypt takes in a string and an integer k and encrypts the string using k
    TIME COMPLEXITY: O(n) -> n is the length of text. This is because we loop over every char in text only once.
    SPACE COMPLEXITY: O(n) -> n is the length of text.
    """
    stack = []
    for ind in range(k):
        currCharInd = ind
        while currCharInd < len(text):
            stack.append(text[currCharInd])
            currCharInd += k

    return "".join(stack)


def decrypt(cipherText: str, k: int) -> str:
    """
    decrypt takes in a cipher text and an integer k and encrypts it to get the original text
    TIME COMPLEXITY: O(n) -> n is the length of cipherText. This is because we loop over every char in text only once.
    SPACE COMPLEXITY: O(n) -> n is the length of cipherText.
    """
    textArr = [""] * len(cipherText)
    portionLength = math.ceil(len(cipherText) / k)
    completePortions = len(cipherText) % k
    currInd = 0

    for key in range(k):
        originalCharInd = key
        if completePortions and completePortions <= key:
            numChars = portionLength - 1
        else:
            numChars = portionLength
        for _ in range(numChars):
            textArr[originalCharInd] = cipherText[currInd]
            currInd += 1
            originalCharInd += k

    return "".join(textArr)


t = "Plain text"
k = 2
cipher_text = encrypt(t, k)
original_text = decrypt(cipher_text, k)
print(f"Encrypt => Text: '{t}', K: {k} = '{cipher_text}'")
print(f"Decrypt => CipherText: '{cipher_text}', K: {k} = '{original_text}'")

t = "Plain text"
k = 3
cipher_text = encrypt(t, k)
original_text = decrypt(cipher_text, k)
print(f"Encrypt => Text: '{t}', K: {k} = '{cipher_text}'")
print(f"Decrypt => CipherText: '{cipher_text}', K: {k} = '{original_text}'")
