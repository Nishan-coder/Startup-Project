import numpy as np
import pandas as pd
import streamlit as st
df = pd.read_csv('startup_funding.csv')
st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Start Up', 'Investor'])
if option == 'Overall Analysis':
   st.title('Overall Analysis')
elif option == 'Start Up':
    st.sidebar.selectbox('Select Startup', sorted(df['Startup Name'].unique().tolist()))
    btn1 = st.sidebar.button('Find Start Up Details')
    st.title('Start Up Analysis')
else:
    df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')  # data filtered gareko
    st.sidebar.selectbox('Select Startup', sorted(df['Investors Name'].unique().tolist()))
    bt2 = st.sidebar.button('Find Investors Details')
    st.title('Inverstor Analysis')

