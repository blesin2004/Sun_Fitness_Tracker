# Sun Fitness Tracker

**Description:**
Sun Fitness Tracker is a Streamlit-based web application designed to help users monitor their fitness progress and predict the number of calories burned based on personalized inputs. The app leverages a RandomForestRegressor model to provide accurate calorie predictions and actionable health insights.

## Features
✅ Predicts calories burned based on:
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
1. Enter your personal details (age, BMI, etc.) in the sidebar.
2. Click the **'Generate Prediction'** button to calculate calories burned.
3. Review your workout intensity and personalized health tips.
4. Click the **'Save Prediction'** button to log your progress.

## Future Improvements
🔹 Add data visualization for weekly/monthly workout trends
🔹 Introduce more predictive features for enhanced accuracy
🔹 Implement user authentication for better data security

## Contributions
Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

