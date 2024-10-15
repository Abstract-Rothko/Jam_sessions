# Importing Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("/.../best-selling-manga.csv")

# Data Cleaning

# Rename Columns
df = df.rename(columns = {'Manga series': 'manga', 'Author(s)':'mangaka', 'Publisher':'publisher', 'Demographic':'demographic', 'No. of collected volumes': 'total_volumes', 'Serialized': 'serialized', 'Approximate sales in million(s)': 'sales_mio', 'Average sales per volume in million(s)': 'sales_per_volume'})

# Demographic Colu
# Simplify value names
df['demographic'] = df['demographic'].fillna("Other")  # Fill None/NaN values with 'Other'
df['demographic'] = df['demographic'].replace(['—', 'Shōjo/Josei', 'Children', 'Shōnen/Seinen', 'Shōnen/shōjo/Josei'], "Other")


# Plotting Demographic
df_demographic = df['demographic'].value_counts().to_frame()

sns.set_theme(style = 'ticks')
sns.barplot(data = df_demographic, x = 'count', y = 'demographic', hue = 'count', palette = 'dark:b_r')
plt.title("Demographics of Best Selling Manga")
plt.xlabel("Total Counts")
plt.ylabel("Demographics")
plt.show()
