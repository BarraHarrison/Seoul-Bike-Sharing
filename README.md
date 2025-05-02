# 📊 Seoul Bike Sharing EDA Project

This project explores the **Seoul Bike Sharing Demand Prediction Dataset** using in-depth Exploratory Data Analysis (EDA) techniques. The goal is to uncover key insights into how weather, time, and seasonal conditions affect public bike rental patterns in Seoul, South Korea.

---

## 📂 Dataset Description

The dataset includes **hourly bike rental counts** along with corresponding **weather conditions**, **seasonal indicators**, and **holiday information**.

**Source:** [Kaggle - Seoul Bike Sharing Demand](https://www.kaggle.com/datasets/sobhanmoosavi/seoul-bike-rental-ai-pro-2020)

**Key columns:**

- Date, Hour, Rented Bike Count (target)
- Temperature, Humidity, Wind Speed, Solar Radiation
- Rainfall, Snowfall
- Seasons, Holiday, Functioning Day

---

## 🧪 Key Features & Analysis Steps

### 🔹 Data Cleaning

- Parsed date column to datetime
- Renamed non-English / inconsistent column names
- Checked for missing values

### 🔹 Feature Engineering

- Extracted: `Day of Week`, `Month`, `Year`, `Is Weekend`
- Created binned versions of `Rainfall` and `Snowfall`

### 🔹 Univariate & Bivariate Analysis

- Histograms and boxplots of all numerical features
- Scatterplots: Temperature, Humidity, Solar Radiation vs Rentals
- Boxplots: Rentals across Rainfall, Snowfall, Seasons, and Holidays

### 🔹 Time Series Analysis

- Daily and Monthly rental trends
- 7-day rolling average
- Average rentals by `Hour` and `Day of Week`

### 🔹 Advanced Insights

- 📊 **Weekday vs Weekend Hourly Patterns**

  - Peak usage on weekdays around 8 AM and 6 PM (commute hours)
  - Weekend usage peaks around late morning to early afternoon

- 🌲 **Random Forest Feature Importance**

  - `Temperature` and `Hour` are the most influential predictors
  - Weather variables like `Solar Radiation`, `Humidity`, and `Rainfall` play supporting roles

---

## 📌 Key Insights

- 🚴 **Temperature** is the strongest predictor of rental count — warm days lead to significantly higher rentals.
- ⏰ **Time of day** drives clear commuting trends, especially on weekdays.
- 🌦️ **Rainfall and Snowfall** reduce rentals sharply, while sunny days correlate with higher demand.
- 🗓️ **Weekends** show different hourly behavior, with bike usage more spread out through the day.

---

## 📁 How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/seoul-bike-sharing.git
   cd seoul-bike-sharing
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter Notebook:

   ```bash
   jupyter lab
   ```

---

## 🚀 Run the Dashboard

To launch the interactive Streamlit dashboard:

1. Make sure you're in the project folder:

   ```bash
   cd seoul-bike-sharing
   ```

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Your browser will automatically open the dashboard at:
   ```
   http://localhost:8501
   ```

Make sure you have the `SeoulBikeData.csv` file in the same directory.

---

## 📌 Technologies Used

- Python 3.9
- Pandas, NumPy
- Seaborn, Matplotlib
- Scikit-learn (for Random Forest)
- Jupyter Lab
- Streamlit

---

## 📘 Author

**Barra Harrison**\
Junior Data Scientist | Full-Stack Developer\
🔗 [LinkedIn](https://www.linkedin.com/in/barraharrison20091997/)\
🔗 [GitHub](https://github.com/BarraHarrison)

---

## 🏁 Future Improvements

- Add predictive modeling section (e.g., XGBoost, time series forecasting)
