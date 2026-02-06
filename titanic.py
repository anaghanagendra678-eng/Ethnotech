# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Titanic dataset
# You can download CSV from: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)

# Step 3: Take a quick look at the data
print(data.head())
print("\nColumns:", data.columns)

# Step 4: Basic survival statistics
print("\nTotal passengers:", len(data))
print("Number of survivors:", data['Survived'].sum())
print("Survival rate:", data['Survived'].mean()*100, "%")

# Step 5: Survival by gender
print("\nSurvival by Gender:")
print(data.groupby('Sex')['Survived'].mean()*100)

# Step 6: Survival by passenger class
print("\nSurvival by Class:")
print(data.groupby('Pclass')['Survived'].mean()*100)

# Step 7: Visualize survival by gender
sns.countplot(x='Sex', hue='Survived', data=data)
plt.title("Survival Count by Gender")
plt.show()

# Step 8: Visualize survival by class
sns.countplot(x='Pclass', hue='Survived', data=data)
plt.title("Survival Count by Class")
plt.show()

print()

