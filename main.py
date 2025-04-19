#MapPlot.py
#Name:
#Date:
#Assignment:

import billionaires
import pandas
import matplotlib.pyplot as plt
billionaire = billionaires.get_billionaire()

#print(billionaire[0]["wealth"]["worth in billions"])
moneys = []
places = []
for data in billionaire:
    money = data["wealth"]["worth in billions"]
    place = data["location"]["country code"]
    if place == "USA" or place == "CHN" or place == "RUS" or place == "CAN" or place == "JPN":
        moneys.append(money)
        places.append(place)


    #print(money, places)
df = pandas.DataFrame({"money": moneys,
                        "place": places})

#print(df)
df.plot(kind = 'scatter', x = 'money', y = 'place')
plt.plot(moneys, places, 'gx', markersize = 10)
plt.savefig("output")

#Every X in this graph represents how many billionaires are not only in each country but also how many billions they have. 
#I have limited the results to only 5 country's (USA, canada, china, russia and japan)
#The graph shows that although there are many billionaires around the world there are a lot more in the USA
#the graph also shows that there more billionaires in the USA that are worth over $20 billion then in other countries
#The graph makes this obvious by the fact that there are a lot more X's in the USA and the density of where those x's are located