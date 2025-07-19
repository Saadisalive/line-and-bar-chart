import matplotlib.pyplot as plt

student_names = ['sanjay','Goku','vegeta','wasim','Naruto','Ajay','daya','Fredey']
students_marks = [35,50,20,45,25,49,26,40]

marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)
    
print(marks_perc)

def marks_line_chart():
    plt.plot(student_names,students_marks)
    plt.title('Students marks graph')
    plt.xlabel('Students names')
    plt.ylabel('Students marks')
    plt.show()

marks_line_chart()

def percentage_bar_chart():
    plt.bar(student_names,marks_perc)
    plt.title('Students percentage graph')
    plt.xlabel('Students names')
    plt.ylabel('Students marks')
    plt.show()
percentage_bar_chart()