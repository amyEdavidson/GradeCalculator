assignmentWeight = 50
midtermWeight = 15
tutorialWeight = 5
finalWeight = 30

print("Please enter your assignment grade")
assignment = input()
assignment = float(assignment)
assignmentGrade = assignment*assignmentWeight

print("Please enter your midterm grade")
midterm = input()
midterm = float(midterm)
midtermGrade = assignment*midtermWeight

print("Please enter your tutorial grade")
tutorial = input()
tutorial = float(tutorial)
tutorialGrade = assignment*tutorialWeight

print("Please enter your final grade")
final = input()
final = float(final)
finalGrade = assignment*finalWeight

totalGrade = assignmentGrade+midtermGrade+tutorialGrade+finalGrade
totalGrade = totalGrade/100

if totalGrade >= 60:
    print("You passed with a final of {0} %\n".format(totalGrade))
else:
    print("You failed with a final of {0} %\n".format(totalGrade))