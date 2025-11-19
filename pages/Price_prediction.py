import streamlit as st
import numpy as np
import pandas as pd
import pickle


st.set_page_config(page_title='Price Predictor')
# Access df and pipe from session_state
with open('Pickle_files/df.pkl', 'rb') as file:
    df = pickle.load(file)
with open('Pickle_files/pipeline.pkl', 'rb') as file:
    pipe = pickle.load(file)


st.header('Welcome to Gurgoan Properties, See your Dream house price')

st.title('Enter your inputs')

# Property_type
property_type = st.selectbox('Property_type', ['flat', 'house'])

# Sectors
with st.container():
    sector = st.selectbox('sector', np.sort(df.sector.unique()))

# No.of BedRooms
bedrooms = float(st.selectbox('Number of BedRooms', np.sort(df.bedRoom.unique())))

# No. of BathRooms
bathrooms = float(st.selectbox('Number of BathRooms', np.sort(df.bathroom.unique())))

# No. of balcony
balcony = st.selectbox('Number of Balcony', np.sort(df.balcony.unique()))

# Age of Property
property_age = st.selectbox('Age of Property', np.sort(df.agePossession.unique()))

# Area in Sqft
built_up_area = float(st.number_input('Built Up area'))

# Servant Room
servant_room = float(st.selectbox('Servant Room', np.sort(df['servant room'].unique())))

# Store Room
store_room = float(st.selectbox('Store Room', np.sort(df['store room'].unique())))

# Furnishing Type
furnishing_type = st.selectbox('Furnishing Type', np.sort(df['furnishing_type'].unique()))

# Luxury Category
luxury_category = st.selectbox('Luxury Category', np.sort(df['luxury_category'].unique()))

# Floor
floor_category = st.selectbox('Floor', np.sort(df['floor_category'].unique()))

# Predict the price
if st.button('Predict the Price'):

    # Form a DataFrame
     data = [property_type, sector, bedrooms, bathrooms, balcony, property_age, built_up_area, store_room, servant_room,
       furnishing_type, luxury_category, floor_category]
     columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'Built Up area', 'store room', 'servant room',
       'furnishing_type', 'luxury_category', 'floor_category']

     data = np.array(data).reshape(1, -1)
     test_df = pd.DataFrame(data=data, columns=columns)

     # Predict
     base_price = np.expm1(pipe.predict(test_df))[0]
     low = base_price - 0.22
     high = base_price + 0.22

     st.text(f"The price of the flat is between {low:.2f} cr and {high:.2f} cr")

else:
    st.write('The button is waiting to be clicked.')