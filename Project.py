import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(layout="wide", page_title='Startup Analysis')


df = pd.read_csv('startup_cleaned.csv')
def load_investor_details(investor):
    st.title(investor)
    #load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains('investor')].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)


    col1, col2 = st.columns(2)
    with col1:
        #biggest investments
        big_series= df[df['investors'].str.contains('investor')].groupby('startup')['amount'].sum().sort_values(ascending = False).head()
        st.subheader('Most Recent Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)



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



