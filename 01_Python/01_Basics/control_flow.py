# Control flow
# if statement

age = 20

if age >= 18:
    print("Eligible to vote")


# if-else statement

marks = 75

if marks >= 50:
    print("Pass")
else:
    print("Fail")


# if-elif-else statement

score = 85

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)


# Nested if statement

age = 20
python_score = 85

if age >= 18:
    if python_score >= 80:
        print("Eligible for advanced Python training")
    else:
        print("Improve Python skills")
else:
    print("Not eligible")


# Logical operators with conditions

age = 20
sql_score = 90

if age >= 18 and sql_score >= 80:
    print("Good performance in SQL")


if age >= 18 or sql_score >= 95:
    print("At least one condition is true")


if not age < 18:
    print("Adult")


# Data analysis example

sales = 65000

if sales >= 100000:
    performance = "Excellent"
elif sales >= 75000:
    performance = "Good"
elif sales >= 50000:
    performance = "Average"
else:
    performance = "Low"

print("Sales:", sales)
print("Sales Performance:", performance)


# Student performance example

python_score = 85
sql_score = 90
tableau_score = 80

average_score = (python_score + sql_score + tableau_score) / 3

if average_score >= 85:
    performance = "Excellent"
elif average_score >= 70:
    performance = "Good"
elif average_score >= 50:
    performance = "Average"
else:
    performance = "Needs Improvement"

print("Average Score:", average_score)
print("Overall Performance:", performance)