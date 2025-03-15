def notes(*grades, value=False):
    """
        This function returns the average of a list of grades.
        param grades:
        List of grades: floats
        Value: True or False
    """
    bigger = 0
    lower = 0
    average = 0
    numberOfGrades = len(grades)

    for index, grade in enumerate(grades):
        average = average + grade
        if index == 0:
            bigger = grade
            lower = grade
        else:
            if grade >= bigger:
                bigger = grade
            if grade <= lower:
                lower = grade
    average = average/numberOfGrades
    if value:
        if 5 < average <= 7:
            feedback = "ok"
        elif average < 5:
            feedback = "bad"
        else:
            feedback = "Good"
        return f' Number of students: {numberOfGrades}\n Grade Average: {average}\n Lowest Grade: {lower}\n Highest Grade: {bigger}\n Final Thoughts: {feedback}\n'
    else:
        return f' Number of students: {numberOfGrades}\n Grade Average: {average}\n Lowest Grade: {lower}\n Highest Grade: {bigger}\n'


print(notes(5.6, 7.8, 8.7, 9.5, 9, 5.6, value=True))
print(notes(5.6, 7.8, 1, 3, 4, 2, value=False))