import pandas as pd


# Load the Excel file into a DataFrame
filename = "database.xlsx"
df = pd.read_excel(filename, engine='openpyxl')



#Openpyxl is installed? Check if it is installed!
try:
    import openpyxl
except ImportError:
    print("You need to install openpyxl to run this example")
    exit()    


# User Input
first_name = input("First name: ")
surname = input("Surname: ")
mail = input("Email address: ")
height = input("Height in centimeters: ")
weight = input("Weight in kilograms: ")



# Calculate BMI
weight_kg = int(weight)
height_cm = float(height)
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

df = df.append(new_data, ignore_index=True)



# Save updated data back to the Excel file
df.to_excel(filename, index=False, engine='openpyxl')