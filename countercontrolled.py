total = 0
gradeCounter = 1

while gradeCounter <= 10:
    grade = input("Enter grade: ")
    grade = int( grade )
    total = total + grade
    gradeCounter = gradeCounter + 1

average = total / 10
print("Class average is %d" % average)