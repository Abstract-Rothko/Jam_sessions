# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("/.../best-selling-manga.csv")

# Data Cleaning

# Rename Columns
df = df.rename(columns = {'Manga series': 'manga', 'Author(s)':'mangaka', 'Publisher':'publisher', 'Demographic':'demographic', 'No. of collected volumes': 'total_volumes', 'Serialized': 'serialized', 'Approximate sales in million(s)': 'sales_mio', 'Average sales per volume in million(s)': 'sales_per_volume'})

# Simplify value names
df['serialized'] = df['serialized'].replace(['1997–present', '1968–present', '1994–present', '1987–present','1989–present', '1992–present', '2006–present', '1981–present', '1991–present', '2014–present', '2018–present', '1990–present', '1993–present', '1983–present','1985–present', '1976–present', '2015–present','2007–present', '2012–present', '2019–present', '2008–present', '1979–present', '2009–present', '2004–present', '1996–present', '1995–present'], "Active") 

df['serialized'] = df['serialized'].replace(['1984–1995', '1969–1996','1999–2014', '1990–1996', '1976–2016', '2016–2020', '2001–2016', '2009–2021', '1952–1968', '1983–1988', '1981–1986', '1946–1974', '2001–2010', '1971–1986', '1990–1994', '2006–2017', '1994–1999','2017–2022', '1992–2003', '1999–2008', '1988–1997', '1995–2013', '2003–2019', '1988–1996', '1992–1999', '2012–2020', '1987–1996', '1973–1983', '1985–1991', '1978–1984', '1972–1973', '1989–1996', '1997–2002', '1996–2008', '1986–1990', '1990–2003', '1972–1981', '2011–2018', '1990–1998', '1991–1997', '1988–2013','2006–2022', '1983–2003', '1996–2004','2001–2009', '1998–2004', '1999–2006','1980–1984', '1990–1999', '1994–2016', '1978–1987', '2002–2013', '1987–2002','1991–2021', '2005–2017', '1986–2018', '2008–2014', '2003–2006', '1998–2006', '1974–1980', '1978–1997', '1988–2019','2004–2012', '1982–1994', '1986–1993', '1982–1988', '1978–2014', '2007–2022','1977–2019', '1982–2002', '1983–1991','2001–2017', '1968–1973', '2012–2016','1990–2004', '1995–2002', '1998–2003', '1993–1999', '2009–2017', '1980–1987', '1994–2013', '1988–2014', '1988–1995', '1993–1996', '2008–2016', '2000–2013', '2014–2022', '2001–2007', '1999–2005', '1972–2014', '1973–2014', '1996–2000', '2015–2022', '1987–1993', '2003–2009', '2004–2019', '1981–2018', '1975–1985', '1972–1983', '1981–1984', '1997–2005', '2002–2009', '2012–2019', '1991–1996', '2004–2018', '2004–2017', '1984–1987', '1998–2001', '1988–1994', '1994–2001', '2003–2012', '1985–2019', '2017–2020', '1976–1982', '1976–1981', '1980–1993', '1992–2001', '1999–2009'], "Completed")

df['serialized'] = df['serialized'].replace(['1983–2014 (on hiatus)', '1998–present (on hiatus)', '1998–2015 (on hiatus)', '1976–2012 (on hiatus)', '2000–2009 (on hiatus)', '1986–2016 (on hiatus)', '1988–2012 (on hiatus)', '2004–2019 (on hiatus)','2011–2018 (on hiatus)'], "Hiatus")

df['serialized'] = df['serialized'].replace('1979–1987, 2011–present', "Other")

# Plotting
df_serialized = df['serialized'].value_counts().to_frame()

sns.set_theme(style = 'ticks')
sns.barplot(data = df_serialized, x = 'count', y = 'serialized', hue = 'count')
sns.dark_palette("#69d", reverse=True, as_cmap=True)
plt.title("Publication Status")
plt.ylabel("Status")
plt.show()
