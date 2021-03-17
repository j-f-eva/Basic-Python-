# input from the user

name = input("What is your name?")

#string concatanation
print("hello " +name)

birth_year = input("Enter your birth Year: ")
int(birth_year)
age = 2020 - int(birth_year)

print(age)


#float in function

first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum: " +str(sum))

#create an object

course = 'python for me'
print(course.upper())
print(course.lower())

#index of course string-y
print(course.find('me'))

#replace the string
print(course.replace('for', '4'))

#using of boolean type "in"
print('python' in course)
print('Eva' in course)



