from flask import Flask, request, render_template
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit(): 
    first_name = request.form['first_name']
    surname = request.form['surname']
    mail = request.form['mail']
    weight_kg = float(request.form['weight_kg'])
    height_cm = float(request.form['height_cm'])

    # Read existing data from the Excel file
    try:
        df = pd.read_excel("database.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame()

    # Add new user data for BMI calculation
    new_data = {
        'First Name': [first_name],
        'Surname': [surname],
        'Mail': [mail],
        'Weight in Kg': [weight_kg],
        'Height in Cm': [height_cm]
    }
    new_df = pd.DataFrame(new_data)
    new_df['user_bmi'] = new_df.apply(lambda row: (row['Weight in Kg'] / (row['Height in Cm'] / 100) ** 2), axis=1)

    # BMI to 1 decimal
    new_df['user_bmi'] = new_df['user_bmi'].round(1)

    # Combine the new data with the existing data and save to the Excel file
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_excel("database.xlsx", index=False)

    # Calculate BMI status
    bmi = new_df['user_bmi'].values[0]
    category = ""
    if bmi < 18.5:
        category = "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        category = "Normal"
    elif bmi >= 25 and bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return f'Your BMI is {bmi} and your BMI category is {category}'

# Run flask to Heroku
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
