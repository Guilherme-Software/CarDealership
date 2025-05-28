import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
def read_data():
    return pd.read_csv("car_prices.csv")

df = read_data()

# selecting 10 best sell brands
def top_sellers():
    array = df['make'].value_counts()
    best_sell_brands = array.head(10)

    # creating plots
    fig, ax = plt.subplots()
    ax.set_title('Top 10 Best Sales Brands')
    ax.set_ylabel('SALES')

    ax.bar(best_sell_brands.index, best_sell_brands.values)


# top 10 most saled cars models.
def top_models():
    array = df["model"].value_counts()
    best_sell_models = array.head(10)

    # config of plots:
    fig, ax = plt.subplots()
    ax.set_title("Top 10 Most Saled Models")
    ax.set_ylabel("Sales")

    ax.bar(best_sell_models.index, best_sell_models.values)

# sales per year:
def monthly_sales_2014():
    df["saledate"] = pd.to_datetime(df["saledate"], errors='coerce', utc=True)
    df["year"] = df["saledate"].dt.year
    df["month"] = df["saledate"].dt.to_period("M")

    selected_year = 2014
    df_selected_year = df[df["year"] == selected_year]

    monthly_sales = df_selected_year.groupby("month")["sellingprice"].sum()

    # config of plots:
    fig, ax = plt.subplots()
    ax.set_title("Monthly Sales 2014")
    ax.set_ylabel("Sales")

    ax.bar(monthly_sales.index, monthly_sales.values)



