import pandas as pd

# Load property dataset
properties = pd.read_csv("data/properties.csv")

# Calculate gross rental yield
properties["gross_yield"] = (
    properties["annual_rent"] / properties["purchase_price"]
) * 100

# Calculate expected vacancy loss
properties["vacancy_loss"] = (
    properties["annual_rent"] * properties["vacancy_rate"]
)

# Calculate effective rental income after vacancy
properties["effective_rent"] = (
    properties["annual_rent"] - properties["vacancy_loss"]
)

# Calculate total annual expenses
properties["total_expenses"] = (
    properties["service_charges"] + properties["maintenance"]
)

# Calculate net rental income
properties["net_income"] = (
    properties["effective_rent"] - properties["total_expenses"]
)

# Calculate net rental yield
properties["net_yield"] = (
    properties["net_income"] / properties["purchase_price"]
) * 100

# Calculate monthly net income
properties["monthly_net_income"] = (
    properties["net_income"] / 12
)

# Calculate break-even period in years
properties["break_even_years"] = (
    properties["purchase_price"] / properties["net_income"]
)

print("UAE Real Estate Investment Analysis")

print("\nProperty Results:")
print(
    properties[
        [
            "area",
            "property_type",
            "purchase_price",
            "annual_rent",
            "gross_yield",
            "net_income",
            "net_yield",
            "monthly_net_income",
            "break_even_years"
        ]
    ]
)

# Find the best investment based on net rental yield
best_index = properties["net_yield"].idxmax()
best_property = properties.loc[best_index]

print("\nBest Investment Based on Net Yield:")
print("Area:", best_property["area"])
print("Property Type:", best_property["property_type"])
print("Purchase Price:", best_property["purchase_price"])
print("Annual Rent:", best_property["annual_rent"])
print("Net Yield:", round(best_property["net_yield"], 2), "%")
print(
    "Monthly Net Income:",
    round(best_property["monthly_net_income"], 2)
)
print(
    "Break-even Years:",
    round(best_property["break_even_years"], 2)
)