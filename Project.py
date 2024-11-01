import numpy as np
import pandas as pd
import streamlit as st
df = pd.read_csv('startup_cleaned.csv')
def load_investor_details(investor):
    st.title(investor)

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Start Up', 'Investor'])
if option == 'Overall Analysis':
   st.title('Overall Analysis')

   

elif option == 'Start Up':
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Start Up Details')
    st.title('Start Up Analysis')
else:
    df['investors'] = df['investors'].fillna('Undisclosed')  # data filtered gareko
    selected_investor = st.sidebar.selectbox('Select Startup', sorted(set(df['investors'].str.split(',').sum())))
    bt2 = st.sidebar.button('Find Investors Details')
    if bt2:
        load_investor_details(selected_investor)



