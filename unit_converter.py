import streamlit as st

# Define conversion functions
def convert_units(value, from_unit, to_unit, category):
    try:
        if category == "Length":
            conversions = {
                "Meter": 1.0,
                "Kilometer": 1000.0,
                "Centimeter": 0.01,
                "Millimeter": 0.001,
                "Mile": 1609.34,
                "Yard": 0.9144,
                "Foot": 0.3048,
                "Inch": 0.0254,
            }

        elif category == "Mass":
            conversions = {
                "Kilogram": 1.0,
                "Gram": 0.001,
                "Milligram": 0.000001,
                "Pound": 0.453592,
                "Ounce": 0.0283495,
            }

        elif category == "Temperature":
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    return (value * 9/5) + 32
                elif to_unit == "Kelvin":
                    return value + 273.15
                else:
                    return value
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    return (value - 32) * 5/9
                elif to_unit == "Kelvin":
                    return ((value - 32) * 5/9) + 273.15
                else:
                    return value
            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    return value - 273.15
                elif to_unit == "Fahrenheit":
                    return ((value - 273.15) * 9/5) + 32
                else:
                    return value

        elif category == "Time":
            conversions = {
                "Second": 1.0,
                "Minute": 60.0,
                "Hour": 3600.0,
                "Day": 86400.0,
            }

        else:
            return "Invalid category"

        # General formula for non-temperature conversions
        return value * conversions[from_unit] / conversions[to_unit]

    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit App UI
st.set_page_config(page_title="Google Unit Converter", layout="centered")
st.title("🔄 Google Unit Converter")

category = st.selectbox("Select Conversion Category", ["Length", "Mass", "Temperature", "Time"])

unit_options = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Mass": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Second", "Minute", "Hour", "Day"]
}

from_unit = st.selectbox("From", unit_options[category])
to_unit = st.selectbox("To", unit_options[category])

value = st.number_input("Enter value to convert", format="%.6f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
