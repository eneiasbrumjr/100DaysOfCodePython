# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maxs=0
for stu_score in student_scores:
    if maxs<stu_score:
        maxs=stu_score

print("The highest score in the class is: "+str(maxs))
