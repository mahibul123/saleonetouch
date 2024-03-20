import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt
st.title("MADSMART SALE FROM 1ST TO 15TH MARCH")
st.markdown("-----")
df=pd.read_excel("Book1.xlsx")
st.write(df.head())
OPENING =round(df['OPENING SALE'].sum(),1)
CLOSING=round(df['CLOSING SALE'].sum(),1)
col1, col2=st.columns(2)



with col1:
    st.subheader('OPENING:')
    st.subheader(f' UNIT {OPENING:},')


with col2:
        st.subheader('CLOSING:')
        st.subheader(f'UNIT {CLOSING}')

col3, col4=st.columns(2)

product_sale=pd.pivot_table(df, index='ITEM', values='OPENING SALE', aggfunc='sum').sort_values(by='OPENING SALE')
    
fig = px.bar(product_sale, x='OPENING SALE', y=product_sale.index)
st.plotly_chart(fig,use_container_width=True)

product_sale=pd.pivot_table(df, index='ITEM', values='CLOSING SALE', aggfunc='sum').sort_values(by='CLOSING SALE')
    
fig = px.bar(product_sale, x='CLOSING SALE', y=product_sale.index)
st.plotly_chart(fig,use_container_width=True)

