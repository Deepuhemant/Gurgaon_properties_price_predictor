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
st.set_page_config(page_title="📊 Recommend Apartments", layout="centered")

location_df = pickle.load(open("Pickle_files/location_dist.pkl", 'rb'))

st.title("Select Location and Radius")

selected_location = st.selectbox("Location", sorted(location_df.columns.to_list()))

import streamlit as st

# Display a number input widget
distance = st.number_input(
    label="Enter a number:",
    step=1
)

if st.button("search"):
    x = location_df[location_df[selected_location] < distance][selected_location].sort_values()
    y = x.items()
    for location, distance in x.items():
        st.text(f"{location} {distance} kms")


# importing cosine similarity

cosine_sim1 = pickle.load(open("Pickle_files/cosine_sim1.pkl", 'rb'))
cosine_sim2 = pickle.load(open("Pickle_files/cosine_sim2.pkl", 'rb'))
cosine_sim3 = pickle.load(open("Pickle_files/cosine_sim3.pkl", 'rb'))


def recommend_property_with_scores(property_name, top_n=5):
    # cosine_sim_matrix = cosine_sim1 + cosine_sim2 + 8*cosine_sim3
    cosine_sim_matrix = cosine_sim1 + 41 * cosine_sim2 + 10 * cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a DataFrame with the result
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df

st.title("Recommend Apartments")
selected_location = st.selectbox("select an apartment", sorted(location_df.index.to_list()))

if st.button("Recommend"):
        st.dataframe(recommend_property_with_scores(selected_location))


