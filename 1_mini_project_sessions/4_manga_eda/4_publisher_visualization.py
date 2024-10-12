# Importing Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("/storage/3136-3633/Projects/2. Datasets/1. Anime & Manga/best-selling-manga.csv")

# Data Cleaning

# Rename Columns
df = df.rename(columns = {'Manga series': 'manga', 'Author(s)':'mangaka', 'Publisher':'publisher', 'Demographic':'demographic', 'No. of collected volumes': 'total_volumes', 'Serialized': 'serialized', 'Approximate sales in million(s)': 'sales_mio', 'Average sales per volume in million(s)': 'sales_per_volume'})


# Simplify value names
df['publisher'] = df['publisher'].fillna("Other")


df['publisher'] = df['publisher'].replace(['Enix (2001–2003), Square Enix (2003–2010)', 'Square Enix', 'Square Enix, Ichijinsha', 'Enix'], "Enix")

df['publisher'] = df['publisher'].replace(['Akita Shoten', 'Ushio Shuppansha', 'Futabasha', 'Shōnen Gahōsha', 'Hakusensha', 'Nihon Bungeisha','Jitsugyo no Nihon Sha', 'Shueisha/Kodansha', 'Shinchosha, Tokuma Shoten', 'Kadokawa Shoten', 'Ushio Shuppan', 'Shueisha/Shogakukan/Leed'], "Other")

# Plotting
df_publisher = df['publisher'].value_counts().to_frame()

sns.set_theme(style = 'ticks')
sns.barplot(data = df_publisher, x = 'count', y = 'publisher', hue = 'count', palette = 'flare')
plt.title("Best Selling Manga Publishers")
plt.ylabel("Publishers")
plt.show()