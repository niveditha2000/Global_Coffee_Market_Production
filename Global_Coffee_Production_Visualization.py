#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[10]:


#Data Framing

global_coffee_production = pd.read_csv("total-production.csv").T
global_coffee_production.columns = global_coffee_production.iloc[0]
global_coffee_production = global_coffee_production.drop("total_production")

global_coffee_production.head()


# In[11]:


#To check data type information about dataframe
global_coffee_production.info()


# In[20]:


#Checking Top Ten Coffee Producers

top_ten_coffee_producers = global_coffee_production.sum().sort_values(ascending=False).iloc[:15]

top_ten_coffee_producers.head()


# In[21]:


top_ten_coffee_producers


# In[15]:


#Creating Pandas Dataframe with top six countries

topsix = global_coffee_production.loc[:, ["Brazil", "Viet Nam", "Colombia", "Indonesia", "Ethiopia","India"]]
topsix.index = topsix.index.astype("datetime64[ns]")
topsix.head()


# In[31]:


figure, axis = plt.subplots()

axis.plot(topsix.index, global_coffee_production["Brazil"] / 1000, label="Brazil")
axis.plot(topsix.index, global_coffee_production["Viet Nam"] / 1000, label="Viet Nam")
axis.plot(topsix.index, global_coffee_production["Colombia"] / 1000, label="Colombia")
axis.plot(topsix.index, global_coffee_production["Indonesia"] / 1000, label="Indonesia")
axis.plot(topsix.index, global_coffee_production["Ethiopia"] / 1000, label="Ethiopia")
axis.plot(topsix.index, global_coffee_production["India"] / 1000, label="India")

axis.set_title("Top Six Coffee Producing Countries")
axis.set_xlabel("Year")

axis.set_ylabel("manufacture (Sixty kg Thousand Bags)")


axis.legend()
plt.show()


# In[24]:




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


# In[29]:


#Pie Chart
figure, axis = plt.subplots()

axis.pie(global_coffee_production_topsix[::-1],
       autopct="%.0f%%",
       labels=list(global_coffee_production_topsix.index[::-1]),
       startangle=45
      )
plt.show()


# In[35]:


#Build a chart that global coffee total production as well as Brazil and Viet Nam
#contribution to global coffee production over time.


brazil_vs_remainingworldwide = (global_coffee_production
                    .assign(worldwide = global_coffee_production
                            .drop("Brazil", axis=1).sum(axis=1))
                    .loc[:, ["Brazil", "worldwide"]]
                    .astype({"Brazil": "float64"})
                   )

brazil_vs_remainingworldwide


# In[57]:


figure, axis = plt.subplots()

axis.stackplot(
    brazil_vs_remainingworldwide.index.astype("datetime64[ns]"), 
    brazil_vs_remainingworldwide["Brazil"], 
    brazil_vs_remainingworldwide["worldwide"],colors =['b', 'c'],
    labels=["Brazil", "World Total"]
)


axis.set_title("Share of Brazil for Global Coffee Production Over Time")
axis.set_xlabel("Year", fontsize=12)

axis.set_ylabel("Manufacture (Sixty kg Bags)", fontsize=12)

axis.legend(loc="upper left")

plt.show()


# In[53]:



vietnam_vs_remainingworldwide = (global_coffee_production
                    .assign(worldwide = global_coffee_production
                            .drop("Viet Nam", axis=1).sum(axis=1))
                    .loc[:, ["Viet Nam", "worldwide"]]
                    .astype({"Viet Nam": "float64"})
                   )


# In[54]:


vietnam_vs_remainingworldwide


# In[60]:


figure, axis = plt.subplots()

axis.stackplot(
    vietnam_vs_remainingworldwide.index.astype("datetime64[ns]"), 
    vietnam_vs_remainingworldwide["Viet Nam"], 
    vietnam_vs_remainingworldwide["worldwide"],colors =['r', 'c'],
    labels=["Viet Nam", "World Total"]
)


axis.set_title("Share of Viet Nam for Global Coffee Production Over Time")
axis.set_xlabel("Year", fontsize=12)

axis.set_ylabel("Manufacture (Twenty kg Bags)", fontsize=12)

axis.legend(loc="upper left")

plt.show()


# In[ ]:





# In[ ]:




