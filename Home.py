import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="NestWise | Smart Real Estate",
    page_icon="🏡",
    layout="wide"
)

# ------------------ TITLE & SUBTITLE ------------------
st.markdown("## 🏡 NestWise")
st.markdown("#### Smart Real Estate Price Prediction & Analytics Platform")

st.markdown("""
Welcome to **NestWise**, your intelligent assistant for exploring, analyzing, and predicting real estate prices across Gurugram.  
Whether you're a buyer, investor, or data analyst, this platform helps you make informed property decisions using data-driven insights.
""")

# ------------------ HERO SECTION ------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🚀 What You Can Do")
    st.markdown("""
    - 💸 **Predict property prices** using intelligent ML models  
    - 🗺️ **Visualize prices across sectors** with interactive maps  
    - 📊 **Compare BHK trends**, floor types, and amenities  
    - ☁️ **Explore listing keywords** via feature wordcloud  
    """)

    st.markdown("###")
    st.markdown("👉 Use the sidebar to navigate to:")
    st.markdown("- 🧮 **Price Predictor**")
    st.markdown("- 📈 **Analytics Dashboard**")

    st.markdown("###")
    if st.button("Start Predicting Now 🚀"):
        st.switch_page("pages/price_prediction.py")  # adjust path if different

with col2:
    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
             caption="Data-Driven Gurugram Real Estate",
            use_container_width=True)

# ------------------ FEATURE HIGHLIGHTS ------------------
st.markdown("### 🔧 Platform Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📍 **Geo Insights**\n\nVisualize property prices and trends sector-wise on a live map.")

with col2:
    st.success("📈 **Smart Price Prediction**\n\nAccurate ML-powered predictions using property features.")

with col3:
    st.warning("☁️ **Listing Analysis**\n\nExplore word clouds of property features that affect pricing.")

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("Made with ❤️ by **Garvit Singh** | M.Tech @ IIIT Delhi  \n© 2025 NestWise")


