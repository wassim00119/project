import streamlit as st

# Vehicle Management
def create_vehicle(vehicle_id, make, model, year, fuel_level, efficiency, status="Available"):
    return {"ID": vehicle_id, "Make": make, "Model": model, "Year": year, "Fuel": fuel_level, "Efficiency": efficiency, "Status": status}

# Initialize session state for vehicles
if "vehicles" not in st.session_state:
    st.session_state.vehicles = {}

# Sidebar for menu selection
menu = st.sidebar.selectbox("Menu", ["Add Vehicle", "View Vehicles", "Update Fuel"])

if menu == "Add Vehicle":
    st.header("Add a New Vehicle")
    vehicle_id = st.text_input("Vehicle ID")
    make = st.text_input("Make (Brand)")
    model = st.text_input("Model")
    year = st.text_input("Year")
    fuel_level = st.slider("Fuel Level", 0, 100, 50)
    efficiency = st.number_input("Efficiency (km/l)", min_value=0.1, value=10.0)
    if st.button("Add Vehicle"):
        if vehicle_id in st.session_state.vehicles:
            st.error("Vehicle ID already exists!")
        else:
            st.session_state.vehicles[vehicle_id] = create_vehicle(vehicle_id, make, model, year, fuel_level, efficiency)
            st.success("Vehicle added successfully!")

elif menu == "View Vehicles":
    st.header("All Vehicles")
    if st.session_state.vehicles:
        for v_id, vehicle in st.session_state.vehicles.items():
            st.write(f"*ID:* {vehicle['ID']}, *Make:* {vehicle['Make']}, *Model:* {vehicle['Model']}, "
                     f"*Year:* {vehicle['Year']}, *Fuel:* {vehicle['Fuel']}%, *Efficiency:* {vehicle['Efficiency']} km/l, "
                     f"*Status:* {vehicle['Status']}")
    else:
        st.info("No vehicles to display.")

elif menu == "Update Fuel":
    st.header("Update Vehicle Fuel")
    if st.session_state.vehicles:
        vehicle_id = st.selectbox("Select Vehicle ID", list(st.session_state.vehicles.keys()))
        fuel_change = st.slider("Fuel Change (negative to decrease)", -50, 50, 0)
        if st.button("Update Fuel"):
            vehicle = st.session_state.vehicles[vehicle_id]
            vehicle["Fuel"] = max(0, min(100, vehicle["Fuel"] + fuel_change))
            st.success(f"Fuel updated to {vehicle['Fuel']}% for Vehicle ID: {vehicle_id}")
    else:
        st.info("No vehicles available.")
