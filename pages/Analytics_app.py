import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

# -------------------------------
# 🌍 Page setup
# -------------------------------
st.set_page_config(page_title="📊 Gurgaon Property Analytics", layout="centered")

# -------------------------------
# 🏠 Page title
# -------------------------------
st.title("📊 Gurgaon Property Analytics")
st.markdown("### Visual Insights of Property Prices in Gurgaon")

# -------------------------------
# 📁 Load dataset
# -------------------------------
try:
    df = pd.read_csv("Datasets/complete_df_viz1")
    st.success("✅ Dataset loaded successfully!")
except FileNotFoundError:
    st.error("❌ Could not find 'Datasets/complete_df_viz1.csv'. Please check the file path.")
    st.stop()

# -------------------------------
# 🧹 Data Cleaning (optional safety)
# -------------------------------
cols_to_numeric = ['price_in_crores', 'price_per_sqft', 'Built Up area', 'Latitude', 'Longitude']
df[cols_to_numeric] = df[cols_to_numeric].apply(pd.to_numeric, errors='coerce')
df = df.dropna(subset=['Latitude', 'Longitude'])

# -------------------------------
# 🧮 Summary stats (optional)
# -------------------------------
with st.expander("📈 Dataset Overview"):
    st.write(df.describe(include='all'))
    st.dataframe(df.head(10))

# -------------------------------
# 🗺️ Plot Map Visualization
# -------------------------------
st.markdown("### 🗺️ Property Distribution Map")

fig = px.scatter_map(
    df,
    lat="Latitude",
    lon="Longitude",
    color="price_per_sqft",
    size="Built Up area",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    map_style="open-street-map",
    hover_name="sector",
    hover_data=["price_in_crores", "price_per_sqft"]
)

# Center the chart nicely below title
col1, = st.columns([1])  # notice the comma — it unpacks the single-item list
with col1:
    st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# 🧠 Insights Section
# -------------------------------
st.markdown("---")
st.subheader("💡 Insights:")
st.write("""
- **High price_per_sqft** clusters are concentrated around key premium sectors and expressways.  
- **Sohna Road** and **Golf Course Extension** zones show higher pricing density.  
- Newer constructions with higher `Built Up area` generally drive up prices.  
""")

# -------------------------------
#  feature text
# -------------------------------
try:
    # Open the pickle file
    with open("Pickle_files/feature_text.pkl", "rb") as file:
        data = pickle.load(file)
    st.success("✅ Dataset loaded successfully!")
except FileNotFoundError:
    st.error("❌ Could not find 'Pickle_files/feature_text.pkl'. Please check the file path.")
    st.stop()


# -------------------------------
# 🗺️ Plot Map Visualization
# -------------------------------
st.markdown("### 🗺️ Wordcloud for Ammenities Provided!")
# Font setting
plt.rcParams["font.family"] = "Arial"  # ✅ correct spelling

# Generate word cloud
wordcloud = WordCloud(
    width=800,
    height=800,
    background_color="white",
    stopwords=set(["s"]),
    min_font_size=10
).generate(data)

# Plot Word Cloud inside Streamlit
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
col1, = st.columns([1])  # notice the comma — it unpacks the single-item list
with col1:
    st.pyplot(fig, use_container_width=True)

# Plot area vs price graph inside Streamlit
st.markdown("### 🗺️ Area vs price Graph!")

outlier_removed_df = df[(df['Built Up area'] < 12000) & (df['price_in_crores'] > 1)]

property_type = st.selectbox('select property type', ['flat','house'])

if property_type == "house":
    fig = px.scatter(outlier_removed_df[outlier_removed_df["property_type"]== 'house'], x="Built Up area", y="price_in_crores", color="bedRoom", title="Area Vs Price")
    # show the plot
    col1, = st.columns([1])  # notice the comma — it unpacks the single-item list
    with col1:
        st.plotly_chart(fig, use_container_width=True)
else :
    fig = px.scatter(outlier_removed_df[outlier_removed_df["property_type"] == 'flat'], x="Built Up area",
                     y="price_in_crores", color="bedRoom", title="Area Vs Price")
    # show the plot
    col1, = st.columns([1])  # notice the comma — it unpacks the single-item list
    with col1:
        st.plotly_chart(fig, use_container_width=True)

st.markdown("### 🗺️ BedRoom Pie Chart!")
import re

def sector_sort_key(s):
    # extract the number if it exists, else use a high fallback
    match = re.search(r'\d+', str(s))
    return int(match.group()) if match else float('inf')

sector_name = sorted(df['sector'].unique().tolist(), key=sector_sort_key)
sector_name.insert(0, 'overall')

selected_sector = st.selectbox("select sector", sector_name)

if selected_sector == "overall":
    fig = px.pie(df, names="bedRoom", title="Bedroom Distribution in Gurgaon")
    col1, = st.columns([1])  # notice the comma — it unpacks the single-item list
    with col1:
        st.plotly_chart(fig, use_container_width=True)
else :
    fig = px.pie(df[df['sector']== selected_sector], names="bedRoom", title="Bedroom Distribution in Gurgaon")
    col1, = st.columns([1])  # notice the comma — it unpacks the single-item list
    with col1:
        st.plotly_chart(fig, use_container_width=True)



temp_df = df[df["bedRoom"]<=5]

# Create side by side boxplots of the total bill amounts by day
fig = px.box(temp_df, x="bedRoom", y="price_in_crores", title="BHK Price Range")
# Show the plot
col1, = st.columns([1])  # notice the comma — it unpacks the single-item list
with col1:
    st.plotly_chart(fig, use_container_width=True)
import seaborn as sns
import matplotlib.pyplot as plt

st.markdown("### 🏠 Distribution Plot for House and Flat Prices")

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(8, 5))

# Plot distribution for 'house'
sns.histplot(
    data=df[df['property_type'] == "house"],
    x="price_in_crores",
    color="blue",
    label="House",
    kde=True,
    stat="density",
    alpha=0.4,
    ax=ax
)

# Plot distribution for 'flat'
sns.histplot(
    data=df[df['property_type'] == "flat"],
    x="price_in_crores",
    color="orange",
    label="Flat",
    kde=True,
    stat="density",
    alpha=0.4,
    ax=ax
)

# Add labels, title, and legend
ax.legend(title="Property Type")
ax.set_title("Price Distribution: House vs Flat", fontsize=14)
ax.set_xlabel("Price (in Crores)")
ax.set_ylabel("Density")

# Display inside Streamlit
st.pyplot(fig)


# -------------------------------
# 👣 Footer
# -------------------------------
st.markdown("---")
st.caption("Developed with ❤️ by Hemant — Gurgaon Price Prediction Project")
