#import matplotlib.pyplot as plt 

#students = ["aditi", "shivam", "riya", "ram"]
#marks = [55, 87, 99, 46]

#plt.bar(students, marks, color = "pink", edgecolor = "blue", width=0.5)
#for i, value in enumerate(marks):

 #   plt.text(i, value +1, 
  #          str(value),
   #         ha = "center",
    #        va = "bottom")

#plt.xlabel("students Marks")
#plt.ylabel("marks of Subject")
#plt.title("student with thier marks")
#plt.show()


import matplotlib.pyplot as plt
import numpy as np

months = ["jan", "feb", "mar", "april", "may", "june"]
sales_2025 = [10,45,22,34,43,66]
sales_2026 = [67,32,12,56,87,55]

x = np.arange(len(months))
width = 0.25

plt.bar(x - width/2, sales_2025, width, label = "sales 2025", color = "pink")
plt.bar(x + width/2, sales_2026, width, label = "sales of 2026", color = "red")

for i, value  in enumerate(sales_2025):
    plt.text(i - width/2, value+3, str(value), ha = "center", fontsize = 8)

for i, value in enumerate(sales_2026):
    plt.text(i +width, value+3, str(value), ha = "center", fontsize = 8)
        
    
             

plt.xlabel("months")
plt.ylabel("monthly sales 2025 vs 2026")
plt.title("sales comparison of two years")
plt.grid()
plt.legend()
plt.show()