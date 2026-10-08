import os
import pandas as pd
import matplotlib.pyplot as plt

# Create images folder if it does not exist
os.makedirs("images", exist_ok=True)

# Load property dataset
properties = pd.read_csv("data/properties.csv")

# Calculate investment metrics
properties["vacancy_loss"] = (
    properties["annual_rent"] * properties["vacancy_rate"]
)

properties["effective_rent"] = (
    properties["annual_rent"] - properties["vacancy_loss"]
)

properties["total_expenses"] = (
    properties["service_charges"] + properties["maintenance"]
)

properties["net_income"] = (
    properties["effective_rent"] - properties["total_expenses"]
)

properties["net_yield"] = (
    properties["net_income"] / properties["purchase_price"]
) * 100

properties["monthly_net_income"] = (
    properties["net_income"] / 12
)

properties["break_even_years"] = (
    properties["purchase_price"] / properties["net_income"]
)

# Create labels for charts
properties["label"] = (
    properties["area"] + " - " + properties["property_type"]
)

# Net yield chart
properties.plot(
    x="label",
    y="net_yield",
    kind="bar",
    legend=False
)

plt.title("Net Rental Yield by Property")
plt.xlabel("Property")
plt.ylabel("Net Yield (%)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("images/net_yield_by_property.png")
plt.close()

# Monthly net income chart
properties.plot(
    x="label",
    y="monthly_net_income",
    kind="bar",
    legend=False
)

plt.title("Monthly Net Income by Property")
plt.xlabel("Property")
plt.ylabel("Monthly Net Income (AED)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("images/monthly_net_income.png")
plt.close()

# Break-even period chart
properties.plot(
    x="label",
    y="break_even_years",
    kind="bar",
    legend=False
)

plt.title("Break-Even Period by Property")
plt.xlabel("Property")
plt.ylabel("Break-Even Years")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("images/break_even_years.png")
plt.close()

print("Charts saved successfully in the images folder.")