import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the data
def read_data():
    return pd.read_csv("car_prices.csv")

df = read_data()
df = df.dropna()

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

def color_sales():
    # select most sold colors and filter car withoout colors name.
    filtered_colors = df["color"].dropna()
    filtered_colors = filtered_colors[filtered_colors != "—"]
    colors = filtered_colors.value_counts().head(10)

    # config of plots.
    fig, ax = plt.subplots(figsize = (8, 6))

    ax.set_title("Most Sold Car Per Colors")

    # plot pie and put the colors in the grafic.
    colors.plot(kind="pie", ax=ax, colors=[
        'black', 
        "#ECECEC", 
        '#C0C0C0', 
        'gray', 
        'blue', 
        'red', 
        '#FFD700', 
        'green', 
        '#800020', 
        '#F5F5DC', 
        ], autopct = '%1.1f%%', 
        textprops={'color':"#473D3D"})
    
    ax.set_ylabel('')
