total = 0
gradeCounter = 0

while 1:
    grade = input("Enter grade, -1 to end:")
    grade = int( grade )

    if grade == -1:
        break

    total += grade
    gradeCounter += 1

if gradeCounter != 0:
    average = float( total ) /gradeCounter
    print("Class average is %.2f" % average)
else:
    print("No grades were entered")