 Sun Fitness Tracker
A Streamlit-based fitness tracker that predicts calories burned based on personal and exercise parameters. Save and analyze past predictions to track your fitness progress over time.

  Features
- User-friendly interface for inputting personal details and exercise parameters
- Predicts calories burned using a RandomForestRegressor model
- Displays health tips based on BMI and workout intensity
- Saves predictions for future reference
- View and analyze past workout data

 Data Used
calories.csv – Contains calorie data
exercise.csv – Contains exercise parameters (age, duration, heart rate, body temperature, etc.)

 How It Works
Enter personal details (name, age, BMI, gender).
Enter workout details (duration, heart rate, body temperature).
Generate a prediction using a RandomForestRegressor model.
View estimated calories burned and personalized health tips.
Save the prediction for future analysis.


Technologies Used
Python
Streamlit
Pandas, Numpy
Scikit-learn (RandomForestRegressor)

 Goal
To help users improve their fitness journey by tracking and analyzing workout effectiveness.
