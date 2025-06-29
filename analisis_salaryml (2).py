# -*- coding: utf-8 -*-
"""Analisis-SalaryML.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ijes9yJG2KYm3wzFRz5yPmKmwx4oPRq8
"""

import numpy as np # linear algebra
import pandas as pd # data processing

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Salary.csv')
df.head()

"""### Split the dataset into Independent(X) and Dependent(y) Variables"""

X = df.iloc[:, :-1].values    # Features => Years of experience => Independent Variable
y = df.iloc[:, -1].values     # Target => Salary => Dependent Variable

X

y

"""### Divide the complete dataset into training and testing data"""

# divide the dataset in some amount of training and testing data
from sklearn.model_selection import train_test_split

# random_state => seed value used by random number generator
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

"""### Modeling-Implement Classifier based on Simple Linear Regression"""

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
predictions

y_test

"""### Viasulisasi"""

import seaborn as sns
sns.distplot(predictions-y_test)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Calculate metrics
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Squared Error: {mse:.2f}")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R-squared: {r2:.2f}")

# Residual plot (better than confusion matrix for regression)
plt.scatter(y_test, y_test - predictions)
plt.axhline(y=0, color='r', linestyle='-')
plt.title('Residual Plot')
plt.xlabel('Actual Salary')
plt.ylabel('Residuals')
plt.show()

"""### Evaluasi-Plotting the Best-fit Linear Regression Graph

* Formula for the Linear Regression : Salary = B0 + B1*(Experience)
* B0 = intercept => salary when experience is 0, B1 = slope => increase in salary with unit increase in salary
"""

X = df[['YearsExperience']]
y = df['Salary']

# Buat model regresi linear
model = LinearRegression()
model.fit(X, y)

# Prediksi nilai salary
y_pred = model.predict(X)

# Tampilkan hasil regresi
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])
print("R^2 Score:", model.score(X, y))

# Visualisasi
plt.scatter(X, y, color='red')  # Data asli
plt.plot(X, y_pred, color='blue')  # Garis regresi
plt.title('Pengalaman Kerja vs Gaji')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

!pip install streamlit
!pip install pyngrok

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Regresi Linear Gaji", layout="centered")

st.title("📊 Prediksi Gaji berdasarkan Pengalaman Kerja")

# Upload file CSV
uploaded_file = st.file_uploader("Salary.csv", type=["csv"])

if uploaded_file is not None:
    # Baca file
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Data Awal")
    st.write(df.head())

    # Cek apakah kolom sesuai
    if 'YearsExperience' in df.columns and 'Salary' in df.columns:
        # Model regresi
        X = df[['YearsExperience']]
        y = df['Salary']
        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)

        # Plot
        fig, ax = plt.subplots()
        ax.scatter(X, y, color='red', label='Data Aktual')
        ax.plot(X, y_pred, color='blue', label='Garis Regresi')
        ax.set_title("Pengalaman Kerja vs Gaji")
        ax.set_xlabel("Years of Experience")
        ax.set_ylabel("Salary")
        ax.legend()

        st.subheader("📈 Visualisasi Regresi Linear")
        st.pyplot(fig)

        # Menampilkan koefisien dan intercept
        st.subheader("📌 Informasi Model")
        st.write(f"**Koefisien (Slope):** {model.coef_[0]:.2f}")
        st.write(f"**Intercept (Y-offset):** {model.intercept_:.2f}")
    else:
        st.error("❌ File harus memiliki kolom 'YearsExperience' dan 'Salary'.")