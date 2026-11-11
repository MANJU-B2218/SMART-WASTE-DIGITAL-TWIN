try:
    import streamlit as st  # type: ignore[import-not-found]
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Streamlit is required to run this app. Install it with: pip install streamlit"
    ) from exc

# --- PAGE SETUP ---
st.set_page_config(page_title="Smart Waste Digital Twin", page_icon="♻️", layout="wide")

st.title("♻️ Smart Waste Management Digital Twin")
st.caption("Dayananda Sagar University - CodeClash Hackathon")

st.divider()

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.header("⚙️ Campus Controls")
    
    # Select different campus locations
    selected_zone = st.selectbox(
        "Select Campus Zone:",
        ["CSE Block (Main)", "Library & IT Center", "Cafeteria & Food Court", "Hostel Block A"]
    )
    
    detected_item = st.selectbox(
        "Detected Waste Item:",
        ["Plastic Bottle", "Paper Cup", "Food Waste", "Aluminum Can"]
    )
    
    bin_fill_level = st.slider(f"Fill Level for {selected_zone} (%)", 0, 100, 65)

# --- TOP METRICS DISPLAY ---
st.subheader(f"📊 Real-Time Status: {selected_zone}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Last Detected Material", value=detected_item)

with col2:
    st.metric(label="Current Capacity", value=f"{bin_fill_level}%")

with col3:
    if bin_fill_level > 80:
        st.metric(label="Bin Status", value="CRITICAL", delta="Action Required", delta_color="inverse")
    else:
        st.metric(label="Bin Status", value="NORMAL", delta="OK")

# Progress bar to visualize fill level
st.write("### 🔋 Live Capacity Level")
st.progress(bin_fill_level / 100)

if bin_fill_level > 80:
    st.error(f"🚨 **ALERT:** {selected_zone} bin is near capacity! Dispatching automated pickup request to maintenance crew.")
else:
    st.success(f"✅ {selected_zone} bin levels are within normal operating parameters.")

st.divider()

# --- MOCK / OFFLINE AI & MAINTENANCE LOG ---
st.subheader("📋 System Analytics & Audit Log")

tab1, tab2 = st.tabs(["AI Disposal Insights", "Collection History"])

with tab1:
    st.info("💡 **Smart Optimization Recommendation:**")
    if "Plastic" in detected_item or "Aluminum" in detected_item:
        st.write(f"- **Material Type:** Recyclable. Route material to the DSU Green Hub.")
        st.write(f"- **Action:** Schedule pickup once zone capacity hits 85%.")
    else:
        st.write(f"- **Material Type:** Organic/General Waste. Route to composting or municipal disposal.")
        st.write(f"- **Action:** Immediate collection recommended to prevent odor/spillage.")

with tab2:
    st.write("Recent automated triggers logged by the digital twin:")
    st.markdown("- `10:45 AM` - **CSE Block** bin checked (Fill: 45%) - *Normal*")
    st.markdown("- `09:15 AM` - **Cafeteria** bin checked (Fill: 88%) - *Dispatched Crew #2*")
    st.markdown("- `08:30 AM` - System initialized across 4 campus zones.")