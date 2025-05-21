import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
car_data = pd.read_csv("car_prices.csv")

# creating plots
fig, ax = plt.subplots()

# selecting 10 best sell brands
array = car_data['make'].value_counts()
best_sell_brands = array.head(10)

# Setting bars configs

ax.set_title('Top 10 Best Sales Brands')
ax.set_ylabel('SALES')

ax.bar(best_sell_brands.index, best_sell_brands.values)

plt.show()