import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(page_title="📊 Home Page", layout="centered")

import streamlit as st

st.set_page_config(page_title="📊 Home Page", layout="centered")

st.sidebar.title('House Page')

option = st.sidebar.selectbox('Select one', ['House price predictor', 'Analytics Apps', 'Recommender System'])

if option == 'House price predictor':
    st.switch_page("pages/Price_prediction.py")
elif option == 'Analytics Apps':
    st.switch_page("pages/Analytics_app.py")
elif option == 'Recommender System':
    st.switch_page("pages/Recommender_systems.py")
