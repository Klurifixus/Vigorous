import pandas as pd


# Load the Excel file or create if Non-existing.
filename = "database.xlsx"

try:
    df = pd.read_excel(filename, engine='openpyxl')
except FileNotFoundError:
    columns = ['user', 'first_name','surname','mail', 'weight_kg', 'height_cm', 'user_bmi']
    df = pd.DataFrame(columns=columns)    


#Openpyxl is installed? Check if it is installed!
try:
    import openpyxl
except ImportError:
    print("You need to install openpyxl to run this example")
    exit()    


# User Input Gathering
first_name = input("First name: ")
surname = input("Surname: ")
mail = input("Email address: ")

# User Input for BMI Calculation with error handling
while True:
    try:
        weight_cm = int(input("Weight in kilograms: "))
        height_kg = float(input("Height in centimeters: "))
        break
    except ValueError:
        print("Please enter a number")

# Calculate BMI
weight_kg = int(weight_cm)
height_cm = float(height_kg)
bmi = weight_kg / (height_cm / 100) ** 2
user_bmi = int(bmi)
print(f"Dear {first_name} your BMI is: {user_bmi}")



# Get the next available user number
if not df.empty:
    next_user_number = df['user'].max() + 1
else:
    next_user_number = 1




# Append new data to the DataFrame
new_data = {
    'user': next_user_number,
    'first_name': first_name,
    'surname': surname,
    'mail': mail,
    'weight_kg': weight_kg,
    'height_cm': height_cm,
    'user_bmi': user_bmi
}

df = df._append(new_data, ignore_index=True)



# Save updated data back to the Excel file
df.to_excel(filename, index=False, engine='openpyxl')