#1.
name = 'Mohammad Obaid'
age = 22
is_student = True

print(type(name))
print(type(age))
print(type(is_student))

#2.
age_addition = age + 8
age_subtraction = age - 2
age_multiplication = age * 5
age_division = age/2

print(age_addition)
print(age_subtraction)
print(age_multiplication)
print(age_division)

#3.
print(age == 18)
print(age != 18)
print(age > 18)


#4.
and_condition = (age > 18) and (age < 20)
or_condition = (age > 18) or (age < 20)
not_condition = not((age > 18) or (age < 20))

print(and_condition)
print(or_condition)
print(not_condition)

#5.
marks = 50

marks += 40
print(marks)
marks -= 3
print(marks)
marks *= 2
print(marks)
marks /= 1
print(marks)

#6.
a = 4
b = 6
print(a is b)
print(a is not b)


#7.
class_eight_rolls = [3,4,6,35]

print(35 in class_eight_rolls)
print(1 in class_eight_rolls)