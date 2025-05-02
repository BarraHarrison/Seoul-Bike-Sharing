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

st.sidebar.header("Filter Options")
year_option = st.sidebar.selectbox("Select Year", df['Year'].unique())
season_option = st.sidebar.multiselect("Seasons", df['Seasons'].unique(), default=df['Seasons'].unique())

filtered_df = df[(df['Year'] == year_option) & (df['Seasons'].isin(season_option))]

st.subheader("📈 Average Rentals by Hour")
hourly_avg = filtered_df.groupby('Hour')['Rented Bike Count'].mean().reset_index()
fig1, ax1 = plt.subplots()
sns.lineplot(data=hourly_avg, x='Hour', y='Rented Bike Count', marker='o', ax=ax1)
st.pyplot(fig1)