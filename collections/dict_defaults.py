student_grades = {}

# Try to  add a grade for 'math' for a student that doesnt exist
math_grades = student_grades.get('Alice', {})
math_grades['math'] = 90
print(student_grades)

# Now try to add a grade for 'english' for 'Alice' using setdefault()
english_grades = student_grades.setdefault('Alice', {})
english_grades['english'] = 85
print(student_grades)
