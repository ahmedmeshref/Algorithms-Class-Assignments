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


original_grades = [101, 84, 29, 57]
print(roundGrades(original_grades))
