import streamlit as st 
import streamlit as st 
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import plotly.express as px

# import data
madsmart=pd.read_excel("DSR MADSAMRT.xlsx")

optival=pd.read_excel("DSR OPTIVAL.xlsx")


# join data sheet


# page title
custom_css = """
<style>
.custom-title {
    position: sticky;
    border-style: soild;
    bottom: 0; 
    right: 5px;
     background-color: black;
    font-size: 30px;
    text-align: laft;
    font-weight: bold;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
st.markdown('<div class="custom-title"> LIFE SCAN APRIL MONTH DSR EDA</div>', unsafe_allow_html=True)





# CREATE SIDER






st.sidebar.header("Please Filter Here:")
city= st.sidebar.multiselect(
    "Select the APOLLO:",
    options=madsmart["CITY"].unique(),
    default=madsmart["CITY"].unique()[:3]
)

filtered_data = madsmart[
        (madsmart["CITY"].isin(city))]
    
col1, col2 = st.columns(2)
with col1:
   st.markdown(
    f'<div style="font-size: 30px;text-align: center; border-style: double;background-color: black; color: blue;">APOLLO TOTAL UNIT {round(filtered_data["Extended Amount"].sum()):.2f}</div>',
    unsafe_allow_html=True
)

with col2:
   
   st.markdown(
    f'<div style="font-size: 30px;text-align: center; border-style: double;background-color: black; color: blue;">APOLLO TOTAL UNIT {round(filtered_data["Quantity"].sum()):.2f}</div>',
    unsafe_allow_html=True
)



st.sidebar.header("Please Filter Here:")
city= st.sidebar.multiselect(
    "Select the optival:",
    options=optival["CITY"].unique(),
    default=optival["CITY"].unique()[:3]
)

filtered_df = optival[ 
        (optival["CITY"].isin(city))]
        
col1, col2 = st.columns(2)

with col1:
    st.markdown(
    f'<div style="font-size: 30px;text-align: center; border-style: double;background-color: black; color: blue;">OPTIVAL TOTAL UNIT {round(filtered_df["Extended Amount"].sum()):.2f}</div>',
    unsafe_allow_html=True
)

with col2:
    st.markdown(
    f'<div style="font-size: 30px;text-align: center; border-style: double;background-color: black; color: blue;">OPTIVAL TOTAL UNIT {round(filtered_df["Quantity"].sum()):.2f}</div>',
    unsafe_allow_html=True
)

# crete bar chart..abs



pivot_table = pd.pivot_table(filtered_data, values='Quantity', index='Description 1', aggfunc='sum')

# Reset the index to turn 'Description 1' into a column
pivot_table_reset = pivot_table.reset_index()

# Create a bar chart with Plotly Express
fig = px.bar(pivot_table_reset, x='Description 1', y='Quantity', title='Total Quantity for Each Item', labels={'Description 1': 'Item', 'Quantity': 'Total Quantity'})

# Streamlit app
st.title("Sales Data Visualization")

st.write("### Total Quantity for Each Item")
st.plotly_chart(fig)


# optive

pivot_table = pd.pivot_table(filtered_df, values='Quantity', index='Description 1', aggfunc='sum')

# Reset the index to turn 'Description 1' into a column
pivot_table_reset = pivot_table.reset_index()

# Create a bar chart with Plotly Express
fig = px.bar(pivot_table_reset, x='Description 1', y='Quantity', title='Total Quantity for Each Item', labels={'Description 1': 'Item', 'Quantity': 'Total Quantity'})

# Streamlit app
st.title("Sales Data Visualization")

st.write("### Total Quantity for Each Item")
st.plotly_chart(fig)
