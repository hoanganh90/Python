def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        elif grade >= 38:
            if  grade%5 > 2:
                result.append( grade + 5 -grade%5)
            else:
                result.append(grade)
    return result
gradingStudents([73,67,38,33])
        
    