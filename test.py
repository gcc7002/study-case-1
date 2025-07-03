import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

#The dataset i used = supermarket_sales | source = kaggle 
Data = pd.read_csv("python pandas\study case 1\supermarket_sales new.csv", index_col=0)

#basic analisys of data
print(Data.head())
print(Data.tail())
print(Data.describe())

#parameters for matplot
x = Data.iloc[:,4]
y = Data.iloc[:,5] * Data.iloc[:,6] * Data.iloc[:,7] #the price of product times quantity times taxes

plt.title("total selling by categorie")
plt.figure(figsize=(16,8))
plt.bar(x,y)
plt.show()
