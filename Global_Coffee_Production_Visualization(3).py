#Imports

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Data Framing

global_coffee_production = pd.read_csv("total-production.csv").T
global_coffee_production.columns = global_coffee_production.iloc[0]
global_coffee_production = global_coffee_production.drop("total_production")
global_coffee_production.head()

#To check data type information about dataframe
global_coffee_production.info()

#Checking Top Ten Coffee Producers

top_ten_coffee_producers = global_coffee_production.sum().sort_values(ascending=False).iloc[:15]

top_ten_coffee_producers.head()

top_ten_coffee_producers


#Creating Pandas Dataframe with top six countries

topsix = global_coffee_production.loc[:, ["Brazil", "Viet Nam", "Colombia", "Indonesia", "Ethiopia","India"]]
topsix.index = topsix.index.astype("datetime64[ns]")
topsix.head()

# function for generating the line plot of the data
def generate_lineplt():
 figure, axis = plt.subplots()

 axis.plot(topsix.index, global_coffee_production["Brazil"] / 1000, label="Brazil")
 axis.plot(topsix.index, global_coffee_production["Viet Nam"] / 1000, label="Viet Nam")
 axis.plot(topsix.index, global_coffee_production["Colombia"] / 1000, label="Colombia")
 axis.plot(topsix.index, global_coffee_production["Indonesia"] / 1000, label="Indonesia")
 axis.plot(topsix.index, global_coffee_production["Ethiopia"] / 1000, label="Ethiopia")
 axis.plot(topsix.index, global_coffee_production["India"] / 1000, label="India")

 axis.set_title("Top Six Coffee Producing Countries")
 axis.set_xlabel("Years")

 axis.set_ylabel("Thousand Kg bags")


 axis.legend()
 plt.show()


#Creating new column called 'worldwide'

global_coffee_production["worldwide"] = global_coffee_production.drop(["Brazil", 
                                                             "Viet Nam", 
                                                             "Colombia", 
                                                             "Indonesia",
                                                             "Ethiopia",
                                                              "India"], axis=1).sum(axis=1)

global_coffee_production_topsix = global_coffee_production.loc['2018', ["Brazil", 
                                                             "Viet Nam", 
                                                             "Colombia", 
                                                             "Indonesia",
                                                             "Ethiopia",
                                                             "India",
                                                             "worldwide"
                                                            ]
                                                   ]

global_coffee_production_topsix

 # function for generating the pie plot of the data 
def generate_pieplt():
 figure, axis = plt.subplots()

 axis.pie(global_coffee_production_topsix[::-1], # function for generating the box plot of the data 
       autopct="%.0f%%",
       labels=list(global_coffee_production_topsix.index[::-1]),
       startangle=45
      )
 plt.show()

# function for generating the box plot of the data 
def generate_boxplt():
 # Create List 'box' with the top six and remaining world countries
 box= [ global_coffee_production["worldwide"],global_coffee_production_topsix ]
 fields = ["Remaining world", "Top Six"]
 
 # Plot the Box plot with the above defined List
 plt.boxplot(box, labels = fields)
 
 # Add the Labels and Titile of the Box Plot
 plt.ylabel("Kg bags")
 plt.title("Comparison")
 plt.tight_layout()
 plt.show()
 

# Call the functions to generate respective plots for the Data
generate_lineplt()
generate_pieplt()
generate_boxplt()

