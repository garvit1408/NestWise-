import plotly.express as px
import streamlit as st
import pandas as pd
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Real Estate Dashboard", layout="wide")

st.title("🏡 Real Estate Analytics Dashboard")
st.markdown("Analyze property trends in **Gurugram** — pricing, BHK distribution, amenities, and more.")

# Load Data
new_df = pd.read_csv("/Users/garvit/Desktop/website/datasets/data_viz1.csv")
group_df = new_df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']].mean()

# ---------------------- GeoMap Section ----------------------
with st.expander("🗺️ View Geo Map of Property Prices", expanded=True):
    st.subheader("📍 Sector-wise Map")
    fig_map = px.scatter_map(
        group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
        color_continuous_scale=px.colors.cyclical.IceFire, zoom=10, width=1200, height=600, hover_name=group_df.index
    )
    st.plotly_chart(fig_map, use_container_width=True, key='mapbox_price_map')

# ---------------------- Wordcloud Section ----------------------
with st.expander("☁️ Amenities Wordcloud", expanded=False):
    st.subheader("🛠️ Common Features in Listings")
    with open('/Users/garvit/Desktop/website/datasets/feature_text.pkl', 'rb') as file:
        feature_text = pickle.load(file)

    wordcloud = WordCloud(width=800, height=800, background_color='white',
                          stopwords=set(['s']), min_font_size=10).generate(feature_text)

    fig_wc, ax = plt.subplots(figsize=(8, 8), facecolor=None)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(fig_wc)

# ---------------------- Price vs Area ----------------------
st.subheader("📐 Built-up Area vs Price")
property_type = st.radio("Select Property Type", ['Flat', 'House'], horizontal=True)

if property_type == 'House':
    df_filtered = new_df[new_df['property_type'] == 'house']
else:
    df_filtered = new_df[new_df['property_type'] == 'flat']

fig_scatter = px.scatter(df_filtered, x='built_up_area', y="price", color="bedRoom",
                         title=f"{property_type} — Area vs Price", labels={"built_up_area": "Area (sqft)", "price": "Price (INR)"})
st.plotly_chart(fig_scatter, use_container_width=True, key='scatter_area_price')

# ---------------------- BHK Pie Charts ----------------------
st.subheader("🏠 BHK Distribution")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔄 Overall BHK Ratio")
    fig_bhk_overall = px.pie(new_df, names='bedRoom', title="BHK Distribution (Overall)")
    st.plotly_chart(fig_bhk_overall, use_container_width=True, key='pie_bhk_overall')

with col2:
    st.markdown("### 🏘️ Sector-wise BHK Ratio")
    sector_options = new_df['sector'].unique().tolist()
    sector_options.insert(0, 'Overall')
    selected_sector = st.selectbox('Select Sector', sector_options)

    if selected_sector == 'Overall':
        fig_bhk_sector = px.pie(new_df, names='bedRoom', title="BHK in Overall Sector")
    else:
        fig_bhk_sector = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom',
                                title=f"BHK in Sector: {selected_sector}")
    st.plotly_chart(fig_bhk_sector, use_container_width=True, key='pie_bhk_sector')

# ---------------------- BHK Price Boxplot ----------------------
st.subheader("💸 Price Distribution by BHK")
fig_box = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price',
                 title='BHK-wise Price Distribution', labels={"bedRoom": "BHK", "price": "Price (INR)"})
st.plotly_chart(fig_box, use_container_width=True, key='bhk_price_box')

# ---------------------- Distribution Plot ----------------------
st.subheader("📊 Price Distribution by Property Type")
fig_dist = plt.figure(figsize=(10, 4))
sns.histplot(new_df[new_df['property_type'] == 'house']['price'], label='House', kde=True, color='skyblue')
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], label='Flat', kde=True, color='salmon')
plt.legend()
plt.title("Price Distribution: House vs Flat")
plt.xlabel("Price (INR)")
plt.ylabel("Count")
st.pyplot(fig_dist)

