# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np
# import joblib

# st.set_page_config(page_title="Viz Demo")


# with open('df.pkl','rb') as file:
#     df = pickle.load(file)

# pipeline = joblib.load('pipeline_compatible.joblib')

# print("Pipeline loaded successfully!")

# st.header('Enter your inputs')

# # property_type
# property_type = st.selectbox('Property Type',['flat','house'])

# # sector
# sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

# bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

# bathroom = float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist())))

# balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))

# property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

# built_up_area = float(st.number_input('Built Up Area'))

# servant_room = float(st.selectbox('Servant Room',[0.0, 1.0]))
# store_room = float(st.selectbox('Store Room',[0.0, 1.0]))

# furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))
# luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))
# floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

# if st.button('Predict'):

#     # form a dataframe
#     data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
#     columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
#                'agePossession', 'built_up_area', 'servant room', 'store room',
#                'furnishing_type', 'luxury_category', 'floor_category']

#     # Convert to DataFrame
#     one_df = pd.DataFrame(data, columns=columns)

#     #st.dataframe(one_df)

#     # predict
#     base_price = np.expm1(pipeline.predict(one_df))[0]
#     low = base_price - 0.22
#     high = base_price + 0.22

#     # display
#     st.text("The price of the flat is between {} Cr and {} Cr".format(round(low,2),round(high,2)))


import streamlit as st
import pickle
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="🏠 Price Predictor", layout="centered")

# === Load Data ===
with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

pipeline = joblib.load('pipeline_compatible.joblib')

# === Page Title ===
st.title("💰 Real Estate Price Predictor")
st.markdown("Predict the property price based on key attributes.")

# === Input Section ===
st.subheader("🏗️ Property Details")

col1, col2 = st.columns(2)

with col1:
    property_type = st.selectbox('🏠 Property Type', ['flat', 'house'])
    sector = st.selectbox('📍 Sector', sorted(df['sector'].unique().tolist()))
    bedrooms = float(st.selectbox('🛏️ Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))
    bathroom = float(st.selectbox('🚿 Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))
    balcony = st.selectbox('🏖️ Number of Balconies', sorted(df['balcony'].unique().tolist()))
    property_age = st.selectbox('📆 Property Age', sorted(df['agePossession'].unique().tolist()))

with col2:
    built_up_area = float(st.number_input('📐 Built Up Area (sqft)', min_value=1200.0))
    servant_room = float(st.selectbox('🧹 Servant Room', [0.0, 1.0]))
    store_room = float(st.selectbox('🗄️ Store Room', [0.0, 1.0]))
    furnishing_type = st.selectbox('🛋️ Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
    luxury_category = st.selectbox('🌟 Luxury Category', sorted(df['luxury_category'].unique().tolist()))
    floor_category = st.selectbox('🏢 Floor Category', sorted(df['floor_category'].unique().tolist()))

# === Prediction Logic ===
if st.button("🔍 Predict Price"):
    # Input to DataFrame
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age,
             built_up_area, servant_room, store_room, furnishing_type,
             luxury_category, floor_category]]

    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    # Predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = round(base_price - 0.22, 2)
    high = round(base_price + 0.22, 2)

    # Display as metric cards
    st.subheader("💸 Predicted Price Range")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Low Estimate", value=f"₹ {low} Cr")
    with col2:
        st.metric(label="High Estimate", value=f"₹ {high} Cr")

    st.success("Prediction complete! 🎯")