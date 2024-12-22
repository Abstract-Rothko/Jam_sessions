
import json
import matplotlib.pyplot as plt

# Open file
with open('records.json') as file:
    data = json.load(file)

# Filter data    
percentage = data['pass_percentage']
name = data['name']
title = f"{name}: Pass Percentage (%)"


def custom_pie_chart(data):
    plt.pie(
    x = data,
    autopct = '%1.2f%%',
    textprops = {'fontsize': 14},
    colors = ['#77BFE2', 'tomato'],
    startangle = 90,
    counterclock = False
    )
    plt.title(
    label = title,
    fontdict = {'fontsize': 16},
    pad = 20
    )
    plt.show()
    
    
if __name__ == "__main__":
    custom_pie_chart([percentage, 100 - percentage])
