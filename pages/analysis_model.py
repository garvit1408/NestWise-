import plotly.express as px
import streamlit as st
import pandas as pd
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title = "Plotting Demo")

st.title('Analytics')

st.header("GeoMap")
new_df = pd.read_csv("/Users/garvit/Desktop/website/datasets/data_viz1.csv")

group_df = new_df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']].mean()


fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)


# word cloud eminites

with open('/Users/garvit/Desktop/website/datasets/feature_text.pkl', 'rb') as file:
    feature_text = pickle.load(file)
# feature_text = pickle.load(open('/Users/garvit/Desktop/website/datasets/data_viz1.csv','rb'))

st.header('Features Wordcloud')

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)


fig, ax = plt.subplots(figsize=(8, 8), facecolor=None)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)

# Pass the figure explicitly
st.pyplot(fig)
# plt.figure(figsize = (8, 8), facecolor = None)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.tight_layout(pad = 0)
# st.pyplot()

# Scatter plot area vs price

st.header('Area v/s Price')

property_type = st.selectbox('Select Property Type',['Flat','House'])

if property_type == 'House':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x = 'built_up_area', y = "price", color = "bedRoom",title="Area v/s prcie")
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x = 'built_up_area', y = "price", color = "bedRoom",title="Area v/s prcie")

st.plotly_chart(fig1,use_container_width=True)