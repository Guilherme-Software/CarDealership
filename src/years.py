import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
def read_data():
    return pd.read_csv("car_prices.csv")

# selecting 10 best sell brands
def top_sellers():
    array = read_data()['make'].value_counts()
    best_sell_brands = array.head(10)

    # Setting bars configs
    # creating plots
    fig, ax = plt.subplots()
    ax.set_title('Top 10 Best Sales Brands')
    ax.set_ylabel('SALES')

    ax.bar(best_sell_brands.index, best_sell_brands.values)

    plt.show()



