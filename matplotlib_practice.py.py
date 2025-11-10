# Learning Data visulaization
# working with Matplotlib

import matplotlib.pyplot as plt

Subject = ["mathematics", "c_programing", "cyber_security", "COA"]
Marks = [78,90,70,88]

plt.bar(Subject, Marks, color = "pink", label = "subject vs marks", width = 0.3, edgecolor = "blue" )
plt.legend()     # Note : If we want to print label. it is neccesary to pass legend code
plt.xlabel("SUbjet Name")
plt.ylabel("marks of subject")
plt.title("compaing subject marks")
 plt.show()

            


# Code for writting the bar hieght on the top of bar
import matplotlib.pyplot as plt

month = ["jan", "feb", "march", "april", "may", "june"]
sales = [12000, 45000, 34345, 5656, 7878,12353]

plt.bar(month, sales, color = "purple")
plt.grid(axis = "y", linestyle = "--")
plt.title("styled Bar Graph", fontsize = 14, alpha = 0.6)
plt.show()