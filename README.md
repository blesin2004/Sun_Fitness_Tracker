# Sun Fitness Tracker

Sun Fitness Tracker is a Streamlit-based web application designed to help users monitor their fitness progress and predict the number of calories burned based on personalized inputs. The app leverages a RandomForestRegressor model to provide accurate calorie predictions and actionable health insights.

## Features
#### Predicts calories burned based on:
- Age
- BMI (Body Mass Index)
- Workout Duration (in minutes)
- Heart Rate
- Body Temperature

✅ Provides personalized health tips based on prediction results
✅ Allows users to save predictions and track past workout data
✅ Displays workout intensity and improvement suggestions
✅ Improved User Interface (UI) with:
- Gender displayed as 'Male' or 'Female' in user data (instead of 1 or 0)
- 'Generate Prediction' button added in the sidebar to control prediction execution
- 'Save Prediction' button repositioned at the bottom for improved workflow
✅ Fixed prediction-saving issue to ensure user data is stored correctly

## Technologies Used
- **Python** (for data handling and model building)
- **Streamlit** (for creating an interactive web application)
- **Pandas** (for data manipulation)
- **Matplotlib/Seaborn** (for visualizing workout trends)
- **RandomForestRegressor** (for accurate calorie prediction)

## How to Use
- Open the website app ->  https://sunfitnesstracker-nuutgwwm6cmqxsajuyvbhe.streamlit.app/
- Enter your personal details (age, BMI, etc.) in the sidebar.
- Click the 'Generate Prediction' button to calculate your calorie burn.
- Review your workout intensity and personalized health tips.
- Click the 'Save Prediction' button to log your progress and track future improvements.

## Future Improvements
- Add data visualization for weekly/monthly workout trends
- Introduce more predictive features for enhanced accuracy
- Implement user authentication for better data security

## Goal
-  To provide users with accurate calorie burn predictions and actionable health insights, helping them track and improve their fitness journey effectively.
