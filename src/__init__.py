import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from code import top_sellers, top_models, quarterly_sales

# shows the grafics
top_sellers()
top_models()
quarterly_sales(2015, ["January", "February", "March"])

plt.show()