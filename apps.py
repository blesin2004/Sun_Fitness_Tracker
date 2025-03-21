import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import time
import os
import warnings
from datetime import datetime
warnings.filterwarnings('ignore')

# checking  variables if they don't exist
if 'input_data' not in st.session_state:
    st.session_state.input_data = None
if 'saved' not in st.session_state:
    st.session_state.saved = False
st.set_page_config(page_title="Fitness Tracker")
st.header("Welcome to Sun Fitness Tracker")
st.write("Get accurate predictions of calories burned based on your exercise parameters and compare your performance with Save your predications for future use.")

def user_input():
    st.sidebar.header("Personal Details")
    name = st.sidebar.text_input("Your Name:", placeholder="Virat Kohli", key="name_input")

    st.sidebar.header("Exercise Parameters")
    age = st.sidebar.slider("Age:", 18, 110, 20, key="age")
    bmi = st.sidebar.slider("BMI:", 15, 40, 25, key="bmi")
    duration = st.sidebar.slider("Duration (min):", 0, 40, 15, key="duration")
    heart_rate = st.sidebar.slider("Heart Rate (bpm):", 60, 130, 80, key="heart_rate")
    body_temp = st.sidebar.slider("Body Temperature (°C):", 36, 42, 38, key="body_temp")
    gender = st.sidebar.radio("Gender:", ["Male", "Female"], horizontal=True, key="gender")
    generate = st.sidebar.button("Generate Prediction")

    if generate:
        if name.strip():
            input_data = {
                "Name": name,"Age": age,"BMI": bmi,"Duration": duration,"Heart_Rate": heart_rate,"Body_Temp": body_temp,"Gender": gender,
            }
            st.session_state.input_data = input_data
            return name, input_data
        else:
            st.sidebar.warning("Please fill in all fields.")
            return None, None
# the input_data is already stored
    elif st.session_state.input_data is not None:
        return st.session_state.input_data["Name"], st.session_state.input_data
    return None, None

def progress(label):
    with st.spinner(f"{label}..."):
        time.sleep(1)
    st.success(f"{label} Complete!")

def train():   
    st.markdown("## Please wait a moment")
    try:
        calories = pd.read_csv("calories.csv")
        exercise = pd.read_csv("exercise.csv")

        data = exercise.merge(calories, on="User_ID").drop(columns="User_ID")
        data["BMI"] = (data["Weight"] / ((data["Height"] / 100) ** 2)).round(2)
        data = data[["Gender", "Age", "BMI", "Duration", "Heart_Rate", "Body_Temp", "Calories"]]
        data = pd.get_dummies(data, drop_first=True)

        X = data.drop("Calories", axis=1)
        y = data["Calories"]

        X_train, x_test, y_train,y_test = train_test_split(
            X, y, test_size=0.2, random_state=43
        )
        model = RandomForestRegressor(n_estimators=1000, max_features=3, max_depth=6, random_state=20)
        model.fit(X_train, y_train)
        return model, data
    except Exception as e:
        st.error(f"Error loading training data: {e}")
        return None, None

def results(df, prediction):
    entry = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Name": df["Name"].values[0],
        "Age": df["Age"].values[0],
        "BMI": df["BMI"].values[0],
        "Duration": df["Duration"].values[0],
        "Heart_Rate": df["Heart_Rate"].values[0],
        "Body_Temp": df["Body_Temp"].values[0],
        "Gender": "Male" if df["Male"].values[0] == 1 else "Female",
        "Calories": round(prediction, 2) }
    file_name = "saved_data.csv"
    if os.path.exists(file_name):
        history = pd.read_csv(file_name)
        history = pd.concat([history, pd.DataFrame([entry])], ignore_index=True)
    else:
        history = pd.DataFrame([entry])
    history.to_csv(file_name, index=False)
    st.session_state.saved = True
    st.success("Results saved successfully!")
    try:
        user_history = history[history["Name"] == df["Name"].values[0]]
        if not user_history.empty:
            st.write(f"### Previous entries for {df['Name'].values[0]}:")
            st.write(user_history.tail(2))
    except Exception as e:
        st.error(f"Error loading saved data: {e}")

def show_predictions():
    file_name = "saved_data.csv"
    if os.path.exists(file_name):
        saved_df = pd.read_csv(file_name)
# index start with 1
        saved_df.index = saved_df.index + 1
        st.write("### All Saved Predictions")
        st.dataframe(saved_df)
    else:
        st.info("No saved predictions found.")

def main():
    name, input_data = user_input()

    if input_data:
        df = pd.DataFrame([input_data])
        st.write(f"## Fitness Tracker \n ### Hello {name.split()[0]}")
        st.write("### Your Personalized Fitness Analysis")
        progress("Processing Input Parameters")
        st.dataframe(df)
        model, data = train()
        if model and data is not None:
            df["Male"] = df["Gender"].apply(lambda x: 1 if x == "Male" else 0)
            df_aligned = df.drop(columns=["Gender"]).reindex(
                columns=data.columns.drop("Calories"), fill_value=0)
            
            prediction = model.predict(df_aligned)[0]
            progress("Calorie Burn Prediction")
            st.metric(
                label="Estimated Calories Burned",
                value=f"{prediction:.2f} kcal",
                delta="High intensity" if prediction > 300 else "Moderate intensity",)
            
            st.write("### Personalized Health Tips")

            if input_data["BMI"] > 25:
                st.warning("Consider adding more cardio workouts to lower your BMI.")
            elif input_data["BMI"] < 18.5:
                st.warning("Include strength training to increase muscle mass.")
            else:
                st.success("Good! Your BMI is within a healthy range.")
            if prediction < 200:
                st.info("Try increasing workout duration by 10-15 minutes for better calorie burn.")
            elif prediction > 400:
                st.success("Great intensity! Remember to stay hydrated and rest well.")

            # Save predication
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Save Prediction"):
                    results(df, prediction)
            if st.session_state.get("saved", False):
                st.success(" saved successfully!")
        else:
            st.error("Failed to load training data.Please check your CSV files.")
            
    # it should the old predication
    if st.button("Show The Previous Predictions"):
        show_predictions()

if __name__ == "__main__":
    main()
