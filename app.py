import streamlit as st
from pint import UnitRegistry

# Set page configuration
st.set_page_config(page_title="Unit & Currency Converter", layout="wide")

# Initialize unit registry
ureg = UnitRegistry()

# Define CSS Styling
st.markdown("""
    <style>
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .header-container {
            padding: 25px;
            margin-bottom: 50px;
            text-align: center;
            font-size: 38px;
            font-weight: bold;
            color: white;
            border-radius: 12px;
            background: linear-gradient(45deg, #D61A3C, #C40233, #A4861A);
            background-size: 400% 400%;
            animation: gradientAnimation 5s ease infinite;
            box-shadow: 0px 0px 15px rgba(198, 2, 51, 0.8);
        }

        .success-box {
            padding: 15px;
            border-radius: 10px;
            background: linear-gradient(to right, #A4861A, #D61A3C);
            color: white;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0px 0px 15px rgba(214, 26, 60, 0.7);
        }
    </style>
    """, unsafe_allow_html=True)

# Animated Heading
st.markdown("<div class='header-container'>😎 Unit & Currency Converter</div>", unsafe_allow_html=True)

# Unit Converter Section
st.markdown("## 📏 Unit Converter")
unit_categories = {
    "Length": ["kilometer", "meter", "centimeter", "millimeter", "micrometer", "nanometer", "mile", "yard", "foot", "inch", "nautical_mile"],
    "Mass": ["kilogram", "gram", "milligram", "metric_ton", "pound", "ounce"],
    "Speed": ["meter_per_second", "kilometer_per_hour", "mile_per_hour", "knot"],
    "Area": ["square_meter", "square_kilometer", "square_centimeter", "square_millimeter", "hectare", "acre", "square_mile", "square_yard", "square_foot", "square_inch"],
    "Time": ["second", "minute", "hour", "day", "week", "month", "year"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Liquid Volume": ["liter", "milliliter", "cubic_meter", "cubic_centimeter", "gallon_us", "gallon_uk", "pint_us", "pint_uk", "fluid_ounce_us", "fluid_ounce_uk"],
}
category = st.selectbox("Select a Category", options=list(unit_categories.keys()))
units = unit_categories[category]

col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    value = st.number_input("Enter Value", min_value=0.0, format="%.6f")
    from_unit = st.selectbox("From Unit", options=units)
with col3:
    to_unit = st.selectbox("To Unit", options=units)

def convert_units(value, from_unit, to_unit):
    try:
        converted_value = (value * ureg(from_unit)).to(to_unit)
        return f"{value} {from_unit} = {converted_value.magnitude:.6f} {to_unit}"
    except Exception as e:
        return f"Conversion Error: {str(e)}"

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.markdown(f"<div class='success-box'>✅ {result}</div>", unsafe_allow_html=True)

# Currency Converter Section
st.markdown("## 💰 Currency Converter")
currencies = ["USD", "EUR", "GBP", "INR", "JPY", "CAD", "AUD", "CNY", "SGD", "PKR"]

col4, col5, col6 = st.columns([2, 1, 2])
with col4:
    amount = st.number_input("Enter Amount", min_value=0.0, format="%.2f")
    from_currency = st.selectbox("From Currency", options=currencies)
with col6:
    to_currency = st.selectbox("To Currency", options=currencies)

conversion_rates = {
    "USD": {"EUR": 0.91, "GBP": 0.76, "INR": 83.2, "PKR": 278.5, "CAD": 1.35},
    "EUR": {"USD": 1.10, "GBP": 0.85, "INR": 90.0, "PKR": 300.0, "CAD": 1.48},
}

def convert_currency(amount, from_currency, to_currency):
    try:
        if from_currency == to_currency:
            return f"{amount} {from_currency} = {amount:.2f} {to_currency}"
        rate = conversion_rates.get(from_currency, {}).get(to_currency, None)
        if rate is not None:
            return f"{amount} {from_currency} = {amount * rate:.2f} {to_currency}"
        else:
            return "Conversion rate unavailable"
    except Exception as e:
        return f"Conversion Error: {str(e)}"

if st.button("Convert", key="currency_convert"):
    currency_result = convert_currency(amount, from_currency, to_currency)
    st.markdown(f"<div class='success-box'>💸 {currency_result}</div>", unsafe_allow_html=True)
