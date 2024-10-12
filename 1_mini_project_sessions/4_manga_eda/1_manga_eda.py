# Import libraries
import pandas as pd

# Load dataset
df = pd.read_csv("/storage/3136-3633/Projects/2. Datasets/1. Anime & Manga/best-selling-manga.csv")

print(df.shape)   # (187, 8)

print(df['No. of collected volumes'].describe())

"""
count    187.000000
mean      46.048128
std       34.678288
min        5.000000
25%       23.500000
50%       34.000000
75%       56.500000
max      207.000000
Name: No. of collected volumes, dtype: float64
"""
df = df.rename_axis("fields", axis = 'columns')

print(df.axes)

"""
[RangeIndex(start=0, stop=187, step=1), Index(['Manga series', 'Author(s)', 'Publisher', 'Demographic',
       'No. of collected volumes', 'Serialized',
       'Approximate sales in million(s)',
       'Average sales per volume in million(s)'],
      dtype='object', name='fields')]
"""

print(df['Demographic'].unique())

"""
['Shōnen' 'Seinen' 'Children' 'Shōnen/Seinen' '—' 'Shōjo' 'Josei'
 'Shōjo/Josei' 'Shōnen/shōjo/Josei']
"""

print(df["Approximate sales in million(s)"].describe())

"""
count    187.000000
mean      50.764332
std       57.178028
min       20.000000
25%       24.500000
50%       31.000000
75%       50.500000
max      516.600000
Name: Approximate sales in million(s), dtype: float64
"""

print(df.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 187 entries, 0 to 186
Data columns (total 8 columns):
 #   Column                                  Non-Null Count  Dtype  ---  ------                                  --------------  -----   0   Manga series                            187 non-null    object  1   Author(s)                               187 non-null    object  2   Publisher                               187 non-null    object  3   Demographic                             187 non-null    object  4   No. of collected volumes                187 non-null    int64   5   Serialized                              187 non-null    object  6   Approximate sales in million(s)         187 non-null    float64 7   Average sales per volume in million(s)  187 non-null    float64dtypes: float64(2), int64(1), object(5)
memory usage: 8.1+ KB
None
"""

print(df["Publisher"].unique())

"""
['Shueisha' 'Shogakukan' 'Kodansha' 'Kobunsha' 'Akita Shoten'
 'Enix (2001–2003), Square Enix (2003–2010)' 'Ushio Shuppansha'
 'Futabasha' 'Shōnen Gahōsha' 'Hakusensha' 'Nihon Bungeisha'
 'Jitsugyo no Nihon Sha' 'Shueisha/Kodansha' 'Square Enix'
 'Shinchosha, Tokuma Shoten' 'Kadokawa Shoten' 'Square Enix, Ichijinsha'
 'Gakken' 'Enix' 'Ushio Shuppan' 'Shueisha/Shogakukan/Leed']
"""

# Highest Selling Manga
df_highest_selling = df[df['Approximate sales in million(s)'] == df['Approximate sales in million(s)'].max()]
 print(df_highest_selling[['Manga series', 'Author(s)']])
 
"""
fields Manga series     Author(s)
0         One Piece  Eiichiro Oda

"""

# Lowest Selling Manga
df_lowest_selling = df[df['Approximate sales in million(s)'] == df['Approximate sales in million(s)'].min()]
print(df_lowest_selling[['Manga series', 'Author(s)']])

"""
fields                    Manga series                                          Author(s)
160                          750 Rider                                        Isami Ishii
161                             Buddha                                       Osamu Tezuka
162                          Cat's Eye                                       Tsukasa Hojo
163      Cuffs - Kizu Darake no Chizu                                            Jin Tojo
164                       Eyeshield 21                    Riichiro Inagaki, Yusuke Murata
165                          The Fable                                   Katsuhisa Minami
166                         Fire Force                                     Atsushi Ohkubo
167      Food Wars!: Shokugeki no Soma                           Yūto Tsukuda, Shun Saeki
168                       Fushigi Yûgi                                         Yuu Watase
169                      Giant Killing                        Masaya Tsunamoto, Tsujitomo
170                    Haruhi Suzumiya          Makoto Mizuno, Gaku Tsugano, Puyo, Eretto
171           Hayate the Combat Butler                                       Kenjiro Hata
172               Kimagure Orange Road                                    Izumi Matsumoto
173                Tasogare Ryūseigun                                     Kenshi Hirokane
174                          Love Hina                                       Ken Akamatsu
175                      Master Keaton  Naoki Urasawa, Hokusei Katsushika, Takashi Nag...
176                            Monster                                      Naoki Urasawa
177         Negima! Magister Negi Magi                                       Ken Akamatsu
178                       Peacock King                                       Makoto Ogino
179     The Quintessential Quintuplets                                        Negi Haruba
180                          Red River                                     Chie Shinohara
181                      Shōnen Ashibe                                   Hiromi Morishita
182                       Sukeban Deka                                        Shinji Wada
183                               Swan                                     Kyoko Ariyoshi
184                  The Tale of Genji                                        Waki Yamato
185           Tokyo Daigaku Monogatari                                      Tatsuya Egawa
186                               Weed                                Yoshihiro Takahashi

"""

# Highest Selling Manga, per volume
df_highest_selling_per_volume = df[df['Average sales per volume in million(s)'] == df['Average sales per volume in million(s)'].max()]
print(df_highest_selling_per_volume[['Manga series', 'Author(s)']])

print("Max: ", df['Average sales per volume in million(s)'].max())
print("Min: ", df["Average sales per volume in million(s)"].min())

"""
fields Manga series Author(s)
50         Devilman  Go Nagai

"""


# Lowest Selling Manga, per volume
df_lowest_selling_per_volume = df[df['Average sales per volume in million(s)'] == df['Average sales per volume in million(s)'].min()]
print(df_lowest_selling_per_volume[['Manga series', 'Author(s)']])

"""
fields     Manga series                                          Author(s)
146     Himitsu Series   Yasuko Uchiyama, Tokuo Yokota, Terumi Fujiki, ...

"""

df_demographic = df['Demographic'].value_counts().to_frame()

print(df_demographic)

print(df['Serialized'].unique())

"""
['1997–present' '1968–present' '1994–present' '1984–1995' '1969–1996'
 '1999–2014' '1990–1996' '1976–2016' '2016–2020' '1983–2014 (on hiatus)'
 '2001–2016' '1987–present' '2009–2021' '1952–1968' '1983–1988'
 '1989–present' '1992–present' '1981–1986' '2006–present' '1981–present'
 '1946–1974' '1991–present' '2014–present' '1998–present (on hiatus)'
 '1998–2015 (on hiatus)' '2001–2010' '1971–1986' '1990–1994'
 '1979–1987, 2011–present' '2006–2017' '1994–1999' '2018–present'
 '2017–2022' '1992–2003' '1999–2008' '1988–1997' '1990–present'
 '1995–2013' '2003–2019' '1988–1996' '1992–1999' '2012–2020' '1987–1996'
 '1993–present' '1973–1983' '1985–1991' '1978–1984' '1972–1973'
 '1989–1996' '1976–2012 (on hiatus)' '1997–2002' '1996–2008'
 '2000–2009 (on hiatus)' '1986–1990' '1990–2003' '1972–1981'
 '1983–present' '2011–2018' '1990–1998' '1991–1997' '1988–2013'
 '2006–2022' '1983–2003' '1985–present' '1976–present' '2015–present'
 '1996–2004' '2001–2009' '1998–2004' '1999–2006' '1986–2016 (on hiatus)'
 '1980–1984' '1990–1999' '1994–2016' '1978–1987' '2002–2013' '1987–2002'
 '1991–2021' '2005–2017' '1986–2018' '2007–present' '2008–2014'
 '1988–2012 (on hiatus)' '2003–2006' '1998–2006' '1974–1980' '1978–1997'
 '1988–2019' '2012–present' '2004–2012' '2019–present' '1982–1994'
 '1986–1993' '1982–1988' '1978–2014' '2007–2022' '2008–present'
 '1977–2019' '1982–2002' '1983–1991' '1979–present' '2001–2017'
 '1968–1973' '2012–2016' '2009–present' '2004–present' '1990–2004'
 '1995–2002' '1998–2003' '1993–1999' '2009–2017' '1980–1987' '1994–2013'
 '1988–2014' '1988–1995' '1993–1996' '2008–2016' '2004–2019 (on hiatus)'
 '2000–2013' '2014–2022' '2001–2007' '1999–2005' '1972–2014' '1973–2014'
 '1996–present' '1996–2000' '2015–2022' '2011–2018 (on hiatus)'
 '1987–1993' '2003–2009' '2004–2019' '1981–2018' '1975–1985' '1972–1983'
 '1981–1984' '1997–2005' '2002–2009' '2012–2019' '1991–1996' '2004–2018'
 '2004–2017' '1984–1987' '1995–present' '1998–2001' '1988–1994'
 '1994–2001' '2003–2012' '1985–2019' '2017–2020' '1976–1982' '1976–1981'
 '1980–1993' '1992–2001' '1999–2009']

"""