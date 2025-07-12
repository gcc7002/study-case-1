import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

#The dataset i used = supermarket_sales | source = kaggle 
Market_data = pd.read_csv("python pandas\study case 1\supermarket_sales new.csv", index_col=0, parse_dates= True)

#basic analisys of data
print(Market_data.head())
print(Market_data.tail())
print(Market_data.describe())

#parameters for matplot
product = Market_data["Product line"]
income = Market_data.iloc[:,5] * Market_data.iloc[:,6] +( Market_data.iloc[:,5] * Market_data.iloc[:,6] * Market_data.iloc[:,7]) #the price of product times quantity times taxes

plt.title("total selling by categorie")
plt.figure(figsize=(16,8))
sns.barplot(data = Market_data, x= income, hue = product)

plt.show()
