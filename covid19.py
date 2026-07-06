import pandas as pd
import matplotlib.pyplot as plt

# Load file with proper separator
covid = pd.read_csv("covid19.txt", sep=",")

# Rename columns for convenience
covid = covid.rename(columns={
    "dateRep": "Date",
    "countriesAndTerritories": "Country",
    "cases": "New_Cases",
    "deaths": "New_Deaths"
})

# Convert Date column to datetime
covid["Date"] = pd.to_datetime(covid["Date"], dayfirst=True)

# Example: filter for one country
country = "Italy"
country_data = covid[covid["Country"] == country].sort_values("Date")

# Plot daily new cases and deaths
plt.figure(figsize=(12,6))
plt.plot(country_data["Date"], country_data["New_Cases"], label="Daily New Cases")
plt.plot(country_data["Date"], country_data["New_Deaths"], label="Daily New Deaths")
plt.title(f"COVID-19 Daily New Cases & Deaths in {country}")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.show()

# Print peak days
peak_cases = country_data.loc[country_data["New_Cases"].idxmax()]
peak_deaths = country_data.loc[country_data["New_Deaths"].idxmax()]
print(f"Peak daily new cases: {peak_cases['New_Cases']} on {peak_cases['Date'].date()}")
print(f"Peak daily new deaths: {peak_deaths['New_Deaths']} on {peak_deaths['Date'].date()}")
