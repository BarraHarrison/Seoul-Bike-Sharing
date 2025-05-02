import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Seoul Bike Sharing EDA", layout="wide")
st.title("🚴 Seoul Bike Sharing EDA Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("SeoulBikeData.csv", encoding="cp949")
    df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
    df['Day of Week'] = df['Date'].dt.day_name()
    df['Month'] = df['Date'].dt.month
    df['Is Weekend'] = df['Day of Week'].isin(['Saturday', 'Sunday']).astype(int)
    df['Year'] = df['Date'].dt.year
    return df

df = load_data()
