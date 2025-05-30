import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the data
def read_data():
    return pd.read_csv("car_prices.csv")

df = read_data()

# selecting 10 best sell brands
def top_sellers():

    # count and select the 10 brands that sell the most.
    array = df['make'].value_counts()
    best_sell_brands = array.head(10)

    # creating plots
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.set_title('Top 10 Best Sales Brands')
    ax.set_xlabel("BRANDS")
    ax.set_ylabel('SALES')

    ax.bar(best_sell_brands.index, best_sell_brands.values)


# top 10 most saled cars models.
def top_models():

    # count and select the 10 best-selling models.
    array = df["model"].value_counts()
    best_sell_models = array.head(10)

    # config of plots:
    fig, ax = plt.subplots(figsize=(12, 4))

    ax.set_title("Top 10 Most Saled Models")
    ax.set_xlabel("MODELS")
    ax.set_ylabel("SALES")

    ax.bar(best_sell_models.index, best_sell_models.values)

# sales per quarter:
def quarterly_sales(selected_year, trimester):

    # transforms data into dates
    df["saledate"] = pd.to_datetime(df["saledate"], errors='coerce', utc=True)
    df["year"] = df["saledate"].dt.year
    df["month"] = df["saledate"].dt.month_name()

    df_selected_year = df[df["year"] == selected_year]

    # count how many sales had in each month
    monthly_sales = df_selected_year.groupby("month")["sellingprice"].count()

    # reindex months by selected quarter
    monthly_sales = monthly_sales.reindex(trimester)

    # config of plots:
    fig, ax = plt.subplots(figsize=(6, 4))
    monthly_sales.plot(kind="bar", ax=ax, color="blue", rot=0)

    ax.set_title(f'{selected_year} Quarterly Sales')
    ax.set_xlabel("MONTHS")
    ax.set_ylabel("SALES")

