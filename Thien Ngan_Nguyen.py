import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# 1. Initial loading 
# 1.1 read in the data to a Pandas DataFrame
DF=pd.read_csv('seoul_bike_data.csv')
print("Data loaded successfully.")
print (DF)

## 1.2 Write code to print out the column headings provided in the datasets
print("Column headings:")
print(DF.columns)
print(" ")


# 2. Data cleaning 
# Find null values using boolean mask
print("Check for missing values:")
print (DF.isnull())
print(" ")

# Create a mask to select rows that contain any null values
print("Rows containing null values:")
mask1=DF.isnull().any(axis=1)
print(DF[mask1]) #find out 630 rows with null values
print(" ")

# Remove all rows containing null values
DF1= DF.dropna()
print("Rows remaining after removing nulls:", len(DF1))
print (DF1) #8130 rows remaining
print(" ")

# Remove duplicates 
DF2=DF1.drop_duplicates()
print("Rows remaining after removing duplicates:", len(DF2))
print (DF2) #8130 rows remaining
print(" ")

# Check if data are valid (positive values)
print("Check for invalid data in Rented Bike Count:")
a=DF2['Rented Bike Count'] <0
print (DF2[a])
print(" ")

print("Check for invalid data in Hour:")
b=DF2['Hour'] <0
print (DF2[b])
print(" ")

print("Check for invalid data in Humidity(%):")
c=DF2['Humidity(%)'] <0
print (DF2[c])
print(" ")

print("Check for invalid data in Wind speed (m/s):")
d=DF2['Wind speed (m/s)'] <0
print (DF2[d])
print(" ")

print("Check for invalid data in Visibility (10m):")
e=DF2['Visibility (10m)'] <0
print (DF2[e])
print(" ")

print("Check for invalid data in Solar Radiation (MJ/m2):")
f=DF2['Solar Radiation (MJ/m2)'] <0
print (DF2[f])
print(" ")

print("Check for invalid data in Rainfall(mm) (m/s):")
g=DF2['Rainfall(mm)'] <0
print (DF2[g])
print(" ")

print("Check for invalid data in Snowfall (cm) (m/s):")
h=DF2['Snowfall (cm)'] <0
print (DF2[h])
print(" ")

# Check categorical consistency
print("Unique categorical values check:")
print("Seasons:", DF2['Seasons'].unique())
print("Holiday:", DF2['Holiday'].unique())
print("Functioning Day:", DF2['Functioning Day'].unique())
print("Data cleaning completed successfully.")
print(" ")

# Reset index
print("Reset index:")
DF2.reset_index(inplace=True, drop=True)
print (DF2)



# 3. Numerical analysis 
# Find the mean, median and standard deviation 
print("Numerical Analysis")

mean1=np.mean(DF2['Rented Bike Count'])
median1=np.median(DF2['Rented Bike Count'])
std1=np.std(DF2['Rented Bike Count'])
print("Rented Bike Count")
print("Mean:", mean1)
print("Median:", median1)
print("Standard Deviation:", std1)
print(" ")

mean2=np.mean(DF2['Hour'])
median2=np.median(DF2['Hour'])
std2=np.std(DF2['Hour'])
print("Hour")
print("Mean:", mean2)
print("Median:", median2)
print("Standard Deviation:", std2)
print(" ")

mean3=np.mean(DF2['Temperature(deg C)'])
median3=np.median(DF2['Temperature(deg C)'])
std3=np.std(DF2['Temperature(deg C)'])
print("Temperature(deg C)")
print("Mean:", mean3)
print("Median:", median3)
print("Standard Deviation:", std3)
print(" ")


# 4. Simple plot [10 marks]
#plotting the rental count as a function of temperature or humidity
plt.figure(figsize=(12,5))
plt.scatter(DF2['Temperature(deg C)'], DF2['Rented Bike Count'], s=15, c=DF2['Temperature(deg C)'], cmap='coolwarm', alpha=0.5, label='Rented Bikes')
plt.xlabel('Temperature (deg C)')
plt.ylabel('Rented Bike Count')
plt.title('Bike Rentals as a Function of Temperature')
plt.legend()
plt.colorbar(label='Temperature (deg C)')
plt.show()

# 5. Multi-variable plot [10 marks]
# Mean rent per hour
mean_rent = DF2.groupby('Hour')['Rented Bike Count'].mean()
plt.figure (figsize=(12,8))
plt.scatter(DF2['Hour'], DF2['Rented Bike Count'], s=30, c=DF2['Temperature(deg C)'], cmap='coolwarm', alpha=0.5)

# Add a line to illustrate mean rent per hour
plt.plot(mean_rent.index, mean_rent.values, color='black', linewidth=2, label='Mean Rent by Hour')

plt.xlabel('x: Hour')
plt.ylabel('y: Rented Bike Count')
plt.xticks(range(0,24,1))
plt.legend()
plt.colorbar(label='Temperature(deg C)')
plt.title("Hourly Bike Rentals and Average Rental Trend Affected by Temperature (deg C)")
plt.show()


#6 Extension task
colors = {'Winter':'blue', 'Spring':'green', 'Summer':'red', 'Autumn':'orange'}

fig = plt.figure(figsize=(20, 8))
ax = fig.add_subplot(111, projection='3d')

for season in colors.keys():
    subset = DF2[DF2['Seasons']==season]
    ax.scatter(subset['Hour'], subset['Rented Bike Count'], subset['Temperature(deg C)'], s=5, c=colors[season], alpha=0.5, label=season)

ax.set_xlim(0, 23)  # X = Hour from 0 to 23
ax.set_xticks(range(0, 24, 2))  # arrange the ticks
ax.set_ylim(0, DF2['Rented Bike Count'].max())  
ax.set_zlim(DF2['Temperature(deg C)'].min(), DF2['Temperature(deg C)'].max())

ax.set_title("Bike Rentals by Season, Analyzed Across Hour and Temperature", pad=20)
ax.set_xlabel('x: Hour')
ax.set_ylabel('y: Rented Bike Count')
ax.set_zlabel('z: Temperature (deg C)')
ax.legend(title='Seasons', loc='upper right')
plt.show()



