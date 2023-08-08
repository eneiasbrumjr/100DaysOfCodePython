# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

cont=0
total_height=0
#Write your code below this row 👇
for stu_height in student_heights:
    cont+=1
    total_height+=int(stu_height)

print(round(total_height/cont))
