def secondlow(students):
    grades = []
    for student in students: 
        grades.append(student[1])
    sort_grades = sorted(grades)
    seclow_grade = sort_grades[0]
    for grade in sort_grades:
        if grade != seclow_grade:
            seclow_grade = grade
            break
    seclow_stud = []
    for student in students: 
        if student[1] == seclow_grade:
            seclow_stud.append(student[0])
    for name in sorted(seclow_stud): 
        print(name)



students = []
for pupil in range(int(input())):
    new_stud = [input(), float(input())]
    students.append(new_stud)
secondlow(students)
