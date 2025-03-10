import streamlit as st
#title
st.title('Unit Convertor By Osama Hassan')
st.sidebar.title('Customization')

#custom css
st.markdown("""
         <style>
/* Full screen and main container */
.stApp, .main, body, [data-testid="stAppViewContainer"] {
    background-color: #0A0A0A !important;
}

/* Sidebar specific styling */
[data-testid="stSidebar"] {
    background-color: #0A0A0A !important;
}

.css-1d391kg, [data-testid="stSidebarNav"] {
    background-color: #0A0A0A !important;
}

/* Sidebar text and elements */
.css-1d391kg .stMarkdown, 
.css-1d391kg p,
[data-testid="stSidebar"] .stMarkdown,
[data-testid="stSidebar"] p {
    color: #FFFFFF !important;
}


/* Rest of your existing styles */
.stTitle, h1 {
    color: #FFFFFF !important;
    font-weight: 600;
    letter-spacing: 0.5px;
}

h2, h3, .stSubheader {
    color: #E0E0E0 !important;
    font-weight: 500;
}
        
p, .stMarkdown {
    color: #CCCCCC !important;
}


/* Dropdown and input styling */
div[data-baseweb="select"], div[data-baseweb="input"] {
    background-color: #1A1A1A !important;
    border: 1px solid #333333 !important;
}

/* Dropdown options */
div[role="listbox"] {
    background-color: #1A1A1A !important;
}

div[role="option"] {
    color: #FFFFFF !important;
}

div[role="option"]:hover {
    background-color: #2D2D2D !important;
         }
         
/* Button styling */
.stButton > button {
    background-color: #2E2E2E !important;
    color: #FFFFFF !important;
    border: 1px solid #404040 !important;
    border-radius: 4px;
    padding: 0.5rem 1rem;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background-color: #2E2E2E !important;
    border-color: #505050 !important;
    transform: translateY(-2px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}
         </style>
     """,
  unsafe_allow_html=True)
#description
st.subheader('This is a unit convertor app that converts units from one unit to another.')

# Simplified unit categories
UNIT_CATEGORIES = {
    'Length': ['meters', 'feet', 'inches', 'centimeters'],
    'Weight': ['kilograms', 'pounds', 'grams'],
    'Temperature': ['celsius', 'fahrenheit', 'kelvin'],
    'Time': ['seconds', 'minutes', 'hours', 'days']
}
def convert_units(value, category, from_unit, to_unit):
    """Simple conversion function with formulas"""
    
    # Dictionary of conversion formulas
    conversions = {
        'Length': {
            'meters_to_feet': value * 3.28084,
            'meters_to_inches': value * 39.3701,
            'meters_to_centimeters': value * 100,
            'feet_to_meters': value * 0.3048,
            'feet_to_inches': value * 12,
            'feet_to_centimeters': value * 30.48,
            'inches_to_meters': value * 0.0254,
            'inches_to_feet': value / 12,
            'inches_to_centimeters': value * 2.54,
            'centimeters_to_meters': value / 100,
            'centimeters_to_feet': value / 30.48,
            'centimeters_to_inches': value / 2.54
        },
        'Weight': {
            'kilograms_to_pounds': value * 2.20462,
            'kilograms_to_grams': value * 1000,
            'pounds_to_kilograms': value * 0.453592,
            'pounds_to_grams': value * 453.592,
            'grams_to_kilograms': value / 1000,
            'grams_to_pounds': value * 0.00220462
        },
        'Temperature': {
            'celsius_to_fahrenheit': (value * 9/5) + 32,
            'celsius_to_kelvin': value + 273.15,
            'fahrenheit_to_celsius': (value - 32) * 5/9,
            'fahrenheit_to_kelvin': (value - 32) * 5/9 + 273.15,
            'kelvin_to_celsius': value - 273.15,
            'kelvin_to_fahrenheit': (value - 273.15) * 9/5 + 32
        },
        'Time': {
            'seconds_to_minutes': value / 60,
            'seconds_to_hours': value / 3600,
            'seconds_to_days': value / 86400,
            'minutes_to_seconds': value * 60,
            'minutes_to_hours': value / 60,
            'minutes_to_days': value / 1440,
            'hours_to_seconds': value * 3600,
            'hours_to_minutes': value * 60,
            'hours_to_days': value / 24,
            'days_to_seconds': value * 86400,
            'days_to_minutes': value * 1440,
            'days_to_hours': value * 24
        }
    }
    
    # If same unit, return the value
    if from_unit == to_unit:
        return value
    
    # Create conversion key
    conversion_key = f"{from_unit}_to_{to_unit}"
    
    # Return converted value
    return conversions[category].get(conversion_key, "Conversion not available")

# Sidebar inputs
category = st.sidebar.selectbox('Select Category', list(UNIT_CATEGORIES.keys()))

#length input
value = st.number_input(f'Enter value for {category} conversion:', value=0.0)

# Get units for selected category
units = UNIT_CATEGORIES[category]
from_unit = st.selectbox('From Unit', units)
to_unit = st.selectbox('To Unit', [u for u in units if u != from_unit])


if st.button('Convert'):
    result = convert_units(value, category, from_unit, to_unit)
    if isinstance(result, (int, float)):
        st.success(f'{value} {from_unit} = {result:.4f} {to_unit}')
    else:
        st.error(result)

# Add helpful examples
with st.sidebar.expander("**See Examples**"):
    st.write(f"Example conversions for {category}:")
    if category == "Length":
        st.write("1 meter = 3.28084 feet")
        st.write("1 foot = 12 inches")
    elif category == "Weight":
        st.write("1 kilogram = 2.20462 pounds")
        st.write("1 pound = 453.592 grams")
    elif category == "Temperature":
        st.write("0°C = 32°F")
        st.write("0°C = 273.15K")
    elif category == "Time":
        st.write("1 hour = 60 minutes")
        st.write("1 day = 24 hours")

