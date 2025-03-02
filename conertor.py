# import streamlit as st

# def convert_units(category, unit_from, unit_to, value):
#     conversions = {
#         "Length": {
#             "Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084
#         },
#         "Weight": {
#             "Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274
#         },
#         "Temperature": {
#             "Celsius": lambda x: x, 
#             "Fahrenheit": lambda x: (x * 9/5) + 32, 
#             "Kelvin": lambda x: x + 273.15
#         }
#     }
    
#     if category == "Temperature":
#         return conversions[category][unit_to](value) if unit_from == "Celsius" else value
#     else:
#         return value * conversions[category][unit_to] / conversions[category][unit_from]

# # Streamlit UI Styling
# st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
# st.title("🔄 Smart Unit Converter")
# st.markdown("Convert **Length, Weight, and Temperature** easily!")

# # Dropdown for categories
# category = st.selectbox("Select a category:", ["Length", "Weight", "Temperature"])

# # Units based on category
# units = {
#     "Length": ["Meters", "Kilometers", "Miles", "Feet"],
#     "Weight": ["Grams", "Kilograms", "Pounds", "Ounces"],
#     "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
# }

# unit_from = st.selectbox("Convert from:", units[category])
# unit_to = st.selectbox("Convert to:", units[category])
# value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# if st.button("Convert Now 🚀"):
#     result = convert_units(category, unit_from, unit_to, value)
#     st.success(f"{value} {unit_from} = {result:.2f} {unit_to}")





import streamlit as st

def convert_units(category, unit_from, unit_to, value):
    conversions = {
        "Length": {
            "Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084, "Inches": 39.3701
        },
        "Weight": {
            "Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274, "Tons": 0.000001
        },
        "Temperature": {
            "Celsius": lambda x: x, 
            "Fahrenheit": lambda x: (x * 9/5) + 32, 
            "Kelvin": lambda x: x + 273.15
        },
        "Time": {
            "Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400, "Weeks": 1/604800
        },
        "Data Storage": {
            "Bytes": 1, "Kilobytes": 1/1024, "Megabytes": 1/(1024**2), "Gigabytes": 1/(1024**3), "Terabytes": 1/(1024**4)
        },
        "Speed": {
            "Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Feet per second": 3.28084
        },
        "Area": {
            "Square Meters": 1, "Square Kilometers": 0.000001, "Square Miles": 3.861e-7, "Square Feet": 10.7639
        },
        "Volume": {
            "Liters": 1, "Milliliters": 1000, "Cubic Meters": 0.001, "Cubic Inches": 61.0237, "Gallons": 0.264172
        }
    }
    
    if category == "Temperature":
        return conversions[category][unit_to](value) if unit_from == "Celsius" else value
    else:
        return value * conversions[category][unit_to] / conversions[category][unit_from]

# Streamlit UI Styling
st.set_page_config(page_title="Advanced Unit Converter", page_icon="🔄", layout="centered")
st.title("🔄 Smart Unit Converter")
st.markdown("Convert **Length, Weight, Temperature, Time, Data Storage, Speed, Area, and Volume** easily!")

# Category icons
category_icons = {
    "Length": "📏 Length",
    "Weight": "⚖️ Weight",
    "Temperature": "🌡️ Temperature",
    "Time": "⏳ Time",
    "Data Storage": "💾 Data Storage",
    "Speed": "🚀 Speed",
    "Area": "📐 Area",
    "Volume": "🧪 Volume"
}

# Dropdown for categories
category = st.selectbox("Select a category:", list(category_icons.keys()), index=0, format_func=lambda x: category_icons[x])

# Units based on category
units = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
    "Weight": ["Grams", "Kilograms", "Pounds", "Ounces", "Tons"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Seconds", "Minutes", "Hours", "Days", "Weeks"],
    "Data Storage": ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"],
    "Speed": ["Meters per second", "Kilometers per hour", "Miles per hour", "Feet per second"],
    "Area": ["Square Meters", "Square Kilometers", "Square Miles", "Square Feet"],
    "Volume": ["Liters", "Milliliters", "Cubic Meters", "Cubic Inches", "Gallons"]
}

unit_from = st.selectbox("Convert from:", units[category])
unit_to = st.selectbox("Convert to:", units[category])
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

if st.button("Convert Now 🚀"):
    result = convert_units(category, unit_from, unit_to, value)
    st.success(f"{value} {unit_from} = {result:.2f} {unit_to}")
