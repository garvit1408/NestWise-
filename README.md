# 🏘️ NestWise: Smarter Real Estate Insights with ML + Streamlit

**NestWise** is a data-driven real estate analytics and recommendation platform built using **Streamlit**, **scikit-learn**, and **Plotly**. It empowers users—home buyers, investors, and analysts—with smart tools to analyze, compare, and predict real estate trends in regions like **Gurgaon** and **Dwarka Expressway**.

---

## 🚀 Features

### 📈 1. **Price Analytics Dashboard**
- Interactive charts showing area-wise price trends.
- Price per sqft comparisons across sectors.
- Visualizations like scatter maps, bar charts, choropleths, and time series plots.
- Identify undervalued and high-growth zones.

### 🧠 2. **House Price Prediction**
- Predict house prices based on:
  - Location
  - Number of bedrooms/bathrooms
  - Floor category
  - Built-up area
  - Furnishing type
  - Age and luxury category
- Trained using advanced regression models like **Random Forest**.

### 🧭 3. **Smart Property Recommendation System**
- Find similar properties using cosine similarity (NLP + vector-based approach).
- Personalized scoring combining multiple models.
- Ranking based on similarity + geographic distance.

### 🗺️ 4. **Geospatial Insights**
- Map visualizations using **Plotly Mapbox**.
- Clustering of properties by price, area, and segment.

---

## 🧑‍💻 Tech Stack

| Layer          | Tools Used                                           |
|----------------|------------------------------------------------------|
| Frontend       | [Streamlit](https://streamlit.io/)                   |
| Backend        | Python, Pandas, Scikit-learn                         |
| Visualization  | Plotly, Matplotlib, Seaborn                          |
| ML Models      | Random Forest, Cosine Similarity                     |
| Data Handling  | Pickle, Joblib, Preprocessing Pipelines              |

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/garvit1408/NestWise-.git
cd NestWise-

# Create and activate virtual environment
python -m venv nestwise-env
source nestwise-env/bin/activate  # or use .\nestwise-env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run Home.py
```
---

## 📊 Example Use Cases
- 📍 “How much does a 3BHK in Sector 66 cost?”
- 🔍 “Which sectors offer high value for money in Gurgaon?”
- “Give me similar listings to DLF The Arbour with high similarity scores.”

## 🎯 Roadmap & Future Work
- Add user authentication and session tracking.
- Expand coverage to more cities (Delhi NCR, Noida, Pune, etc.).
- Integrate live listing APIs (99acres, Magicbricks).
- Real-time price alerts and user dashboards.


- **Garvit Singh** – [@garvit1408](https://github.com/garvit1408)  
  M.Tech CSE @ IIIT-Delhi | Data Science Enthusiast  
  🌐 [My Bento Profile](https://bento.me/garvit14)
