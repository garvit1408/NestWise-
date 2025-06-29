import plotly.express as px
import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Plotting Demo")

st.title('Analytics')

new_df = pd.read_csv("/Users/garvit/Desktop/website/datasets/data_viz1.csv")

group_df = new_df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']].mean()

fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)


# word cloud eminites

