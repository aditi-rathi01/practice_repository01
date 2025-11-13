import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

years = [2019, 2020, 2021, 2022, 2023]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

np.random.seed(10)
s_data = {year: np.random.randint(10000, 100000, size=12) for year in years }
sales_data = pd.DataFrame(s_data, index=months)
print(sales_data)
for year in years:
    plt.plot(months, sales_data[year], marker = "o" ,label=str(year))   # This is for to visualize the Data Graphically

plt.legend()
plt.show()

