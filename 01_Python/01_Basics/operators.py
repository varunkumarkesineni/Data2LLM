# Arithmetic operators

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# Comparison operators

x = 25
y = 20

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# Logical operators

age = 20
python_score = 85

print("Both conditions:", age > 18 and python_score > 80)
print("Either condition:", age > 18 or python_score > 90)
print("Not condition:", not age < 18)

# Assignment operators

total = 100

total += 50
print("After +=:", total)

total -= 20
print("After -=:", total)

total *= 2
print("After *=:", total)

total /= 2
print("After /=:", total)

# Data analysis example

sales_january = 50000
sales_february = 65000

sales_difference = sales_february - sales_january
growth_percentage = (sales_difference / sales_january) * 100

print("January Sales:", sales_january)
print("February Sales:", sales_february)
print("Sales Difference:", sales_difference)
print("Growth Percentage:", growth_percentage, "%")