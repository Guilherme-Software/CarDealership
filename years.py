import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
car_data = pd.read_csv("car_prices.csv")

car_data["saledate"] = pd.to_datetime(car_data["saledate"], errors='coerce', utc=True)

days = car_data.groupby(
    [car_data["saledate"].dt.day])["sellingprice"].mean().plot()

print(days)
plt.show()
## fazer uma limpeza nos dados depois.