from __future__ import annotations


def roundGrade(grade: int) -> int:
    # Invalid input. grade value not in the range of 0 to 100.
    if not (0 <= grade <= 100):
        return -1

    # No rounding if grade < 38
    if grade < 38:
        return grade

    for addition in range(1, 4):
        if (grade + addition) % 5 == 0:
            return grade + addition
    return grade


def roundGrades(grades: list[int]) -> list[int]:
    """
    roundGrade rounds given grades if in range 0 to 100 and greater than 38
    TIME COMPLEXITY: O(n) -> n is the number of grades
    SPACE COMPLEXITY: O(n) -> n is the number of grades
    """
    return [roundGrade(grade) for grade in grades]


if __name__ == "__main__":
    originalGrades = [-100, 84, 29, 57, 71]
    roundedGrades = roundGrades(originalGrades)
    for ind in range(0, len(roundedGrades)):
        # Invalid grade
        if roundedGrades[ind] == -1:
            print(f"Student {ind + 1} received {originalGrades[ind]}, grade is invalid!")
        elif roundedGrades[ind] == originalGrades[ind]:
            print(f"Student {ind + 1} received {originalGrades[ind]}, grade will not be modified and the "
                  f"student's final grade is {roundedGrades[ind]}")
        else:
            print(f"Student {ind + 1} received {originalGrades[ind]}, the student's final grade is rounded to {roundedGrades[ind]}")
