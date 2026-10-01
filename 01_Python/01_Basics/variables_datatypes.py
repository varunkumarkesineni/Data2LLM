# Variables and data types

name = "Varun"
age = 20
height = 160.5
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# Checking data types

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Type conversion

age_text = "20"
age_number = int(age_text)

print("Age:", age_number)
print("Data type:", type(age_number))

marks = 85
marks_float = float(marks)

print("Marks:", marks_float)
print("Data type:", type(marks_float))

score = 95
score_text = str(score)

print("Score:", score_text)
print("Data type:", type(score_text))

# Simple data analysis example

student_name = "Varun"
python_score = 85
sql_score = 90
tableau_score = 80

average_score = (python_score + sql_score + tableau_score) / 3

print("Student:", student_name)
print("Python:", python_score)
print("SQL:", sql_score)
print("Tableau:", tableau_score)
print("Average Score:", average_score)