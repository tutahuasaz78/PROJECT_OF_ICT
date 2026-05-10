import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mechanical Unit Converter", page_icon="⚙️")

# --- CUSTOM CSS FOR MECHANICAL THEME ---
# This injects a gear background and styles the text for an engineering feel
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/carbon-fibre.png"), 
                          url("https://img.freepik.com/free-vector/mechanical-gears-background-blue-style_1017-30676.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    
    h1, h2, h3, p, label {
        color: #e0e0e0 !important;
        font-family: 'Courier New', Courier, monospace;
    }

    .stSelectbox, .stNumberInput {
        background-color: rgba(50, 50, 50, 0.8);
        border-radius: 10px;
        border: 1px solid #777;
    }

    .user-info {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 15px;
        border-left: 5px solid #ffcc00;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("⚙️ Mechanical Unit Converter & Density Checker")

st.markdown(f"""
<div class="user-info">
    <h3>Developer Information:</h3>
    <p><b>Name:</b> Muhammad Hamza Malik</p>
    <p><b>Roll No:</b> 25-ME-152</p>
</div>
""", unsafe_allow_html=True)

# --- APP TABS ---
tab1, tab2 = st.tabs(["📏 Unit Converter", "🧱 Density Checker"])

with tab1:
    st.subheader("Mechanical Unit Converter")
    category = st.selectbox("Select Category", ["Length", "Pressure", "Energy"])
    
    col1, col2 = st.columns(2)
    
    if category == "Length":
        val = col1.number_input("Enter Value", value=1.0)
        unit = col2.selectbox("Convert to", ["Meters to Feet", "Feet to Meters", "Inches to mm", "mm to Inches"])
        
        conversions = {
            "Meters to Feet": val * 3.28084,
            "Feet to Meters": val / 3.28084,
            "Inches to mm": val * 25.4,
            "mm to Inches": val / 25.4
        }
        st.metric("Result", f"{round(conversions[unit], 4)}")

    elif category == "Pressure":
        val = col1.number_input("Enter Value", value=1.0)
        unit = col2.selectbox("Convert to", ["PSI to Bar", "Bar to PSI", "Pascal to PSI"])
        
        conversions = {
            "PSI to Bar": val * 0.0689476,
            "Bar to PSI": val * 14.5038,
            "Pascal to PSI": val * 0.000145038
        }
        st.metric("Result", f"{round(conversions[unit], 4)}")

with tab2:
    st.subheader("Material Density Checker")
    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Titanium": 4506,
        "Cast Iron": 7200
    }
    
    selected_material = st.selectbox("Select Material", list(materials.keys()))
    density = materials[selected_material]
    
    st.write(f"The density of **{selected_material}** is approximately:")
    st.header(f"{density} kg/m³")
    
    # Simple Mass Calculator
    st.info("Quick Mass Calculator (Mass = Density × Volume)")
    volume = st.number_input("Enter Volume (m³)", value=0.1, step=0.01)
    mass = density * volume
    st.success(f"Calculated Mass: {round(mass, 2)} kg")
