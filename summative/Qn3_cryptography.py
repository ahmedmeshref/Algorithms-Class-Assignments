import math


def encrypt(text: str, k: int) -> str:
    """
    encrypt takes in a string and an integer k and encrypts the string using k
    TIME COMPLEXITY: O(n) -> n is the length of text. This is because we loop over every char in text only once.
    SPACE COMPLEXITY: O(n) -> n is the length of text.
    """
    stack = []
    for ind in range(k):
        # Start with the obtained key index
        currCharInd = ind
        # While the index is valid in terms of length of text
        while currCharInd < len(text):
            # Add the char at currIndex to top of the stack
            stack.append(text[currCharInd])
            # Increase index by k
            currCharInd += k

    # Obtain the cipherText by combining stack elements
    return "".join(stack)


def decrypt(cipherText: str, k: int) -> str:
    """
    decrypt takes in a cipher text and an integer k and encrypts it to get the original text
    TIME COMPLEXITY: O(n) -> n is the length of cipherText. This is because we loop over every char in text only once.
    SPACE COMPLEXITY: O(n) -> n is the length of cipherText.
    """
    textArr = [""] * len(cipherText)
    # Calculate each key (portion) length
    portionLength = math.ceil(len(cipherText) / k)
    # Calculate the number of complete portions
    completePortions = len(cipherText) % k
    currInd = 0

    for key in range(k):
        originalCharInd = key
        # If not complete portion, deduct 1 from the original portion size
        if completePortions and completePortions <= key:
            numChars = portionLength - 1
        else:
            numChars = portionLength
        # For each key, add its chars in the right position in textArr
        for _ in range(numChars):
            textArr[originalCharInd] = cipherText[currInd]
            currInd += 1
            originalCharInd += k

    # Obtain the original text by combining stack elements
    return "".join(textArr)


if __name__ == "__main__":
    t = "Plain text"
    k = 2
    cipher_text = encrypt(t, k)
    original_text = decrypt(cipher_text, k)
    print(f"Encrypt => Text: '{t}', K: {k} = '{cipher_text}'")
    print(f"Decrypt => CipherText: '{cipher_text}', K: {k} = '{original_text}'")

    print("-----------------------------------------------------------------")

    t = "Plain text"
    k = 3
    cipher_text = encrypt(t, k)
    original_text = decrypt(cipher_text, k)
    print(f"Encrypt => Text: '{t}', K: {k} = '{cipher_text}'")
    print(f"Decrypt => CipherText: '{cipher_text}', K: {k} = '{original_text}'")
