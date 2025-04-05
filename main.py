import streamlit as st


st.markdown("""
<meta name="google-site-verification" content="VebOAZoLLdJYWbe2385pD5lqofiR1BI-uGVFsqmBkao" />
""", unsafe_allow_html=True)


st.markdown('<meta name="description" content="Best Online Unit Converter for Length, Weight, Temperature, Time, and Volume. Convert meters to kilometers, Celsius to Fahrenheit, and more instantly!">', unsafe_allow_html=True)

st.markdown("""
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Ultimate Unit Converter",
    "url": "https://konverter.streamlit.app",
    "description": "Convert Length, Weight, Temperature, Time, and Volume easily!",
    "applicationCategory": "Utility"
}
</script>
""", unsafe_allow_html=True)

st.title("🔄 Ultimate Unit Converter")

def convert_units(value, from_unit, to_unit):
    conversion = {
        'meter_kilometer': 0.001, 'kilometer_meter': 1000,
        'gram_kilogram': 0.001, 'kilogram_gram': 1000,
        'celsius_fahrenheit': lambda c: (c * 9/5) + 32,
        'fahrenheit_celsius': lambda f: (f - 32) * 5/9,
        'mile_kilometer': 1.60934, 'kilometer_mile': 0.621371,
        'pound_kilogram': 0.453592, 'kilogram_pound': 2.20462,
        'inch_centimeter': 2.54, 'centimeter_inch': 0.393701,
        'yard_meter': 0.9144, 'meter_yard': 1.09361,
        'liter_gallon': 0.264172, 'gallon_liter': 3.78541,
        'second_minute': 1/60, 'minute_second': 60,
        'minute_hour': 1/60, 'hour_minute': 60,
        'hour_day': 1/24, 'day_hour': 24
    }
    
    key = f"{from_unit}_{to_unit}"
    if key in conversion:
        factor = conversion[key]
        return factor(value) if callable(factor) else value * factor
    else:
        return "Conversion not supported"

unit_categories = {
    "Length": ["meter", "kilometer", "mile", "inch", "centimeter", "yard"],
    "Weight": ["gram", "kilogram", "pound"],
    "Temperature": ["celsius", "fahrenheit"],
    "Volume": ["liter", "gallon"],
    "Time": ["second", "minute", "hour", "day"]
}

st.sidebar.header("Select Conversion Categories")
selected_categories = [category for category in unit_categories.keys() if st.sidebar.checkbox(category, value=True)]

if selected_categories:
    category = st.selectbox("Select Category", selected_categories)
    options = unit_categories[category]
    
    from_unit = st.selectbox("Convert from", options)
    to_unit = st.selectbox("Convert to", options)
    
    value = st.number_input("Enter the value to convert", step=1.0, min_value=0.0)
    
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"{value} {from_unit} is equal to {result} {to_unit}")

st.markdown("### Why Use This Converter? 🔥")
st.markdown("- **Supports most searched conversions** (Length, Weight, Temperature, Volume, Time)")
st.markdown("- **Fast & Accurate Calculations ⚡**")
st.markdown("- **Super Simple & Easy to Use 🎯")



