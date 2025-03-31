import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

students_name=['Keshav', "Ajay", "Vinod", "Swami", "Rohit", "Pankaj", "Meghna", "David", "Lisa", "Mohit"]
students_marks=[100, 92,31,41,54,64,31,54,86,100]

marks_perc=[]
for x in students_marks:
    res=(x/100)*100
    marks_perc.append(res)
print(marks_perc)

def marks_line_chart():
    plt.plot(students_name, students_marks)
    plt.title('Marks of Students')
    plt.xlabel('Name')
    plt.ylabel('Marks')
    plt.xticks(rotation=45)
    plt.show()

marks_line_chart()

def perc_bar_graph():
    plt.bar(students_name, marks_perc)
    plt.title('Percentage of Students')
    plt.xlabel('Name')
    plt.ylabel('Percentage')
    plt.xticks(rotation=45)
    plt.show()

perc_bar_graph()























# xPoints=np.array([0,6])
# yPoints=np.array([0,250])
# plt.plot(xPoints, yPoints)
# plt.show()

# xPoints=np.array([0, 3, 5,2,7,8])
# plt.plot(xPoints, 'o', c='g', )
# plt.show()

# xPoints=np.array([0, 3, 5,2,7,8])
# yPoints=np.array([2,7,4,8,1,5])
# plt.plot(xPoints, yPoints, 'o', c='g', marker='o', ms=20, mec='r', linestyle='dashed')
# plt.show()

# xPoints=np.array([1,2,3,4])
# yPoints=np.array([1,2,3,4])
# plt.plot(xPoints,yPoints, linestyle='--')
# plt.title("Graph of Speed vs Time")
# plt.xlabel("Time")
# plt.ylabel("Speed")
# plt.show()


# y1=np.array([3,8,1,10])
# y2=np.array([6,2,7,4])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()
