# Connect to excel
filename = "database.xlsx"

# User Input
# first_name = input("First name: ")
# surname = input("Surname: ")
# mail = input("Email address: ")
# height = input("Height in centimeters: ")
# weight = input("Weight in kilograms: ")



# Calculate BMI
weight_kg = int(weight)
height_cm = float(height)
bmi = weight_kg / (height_cm / 100) ** 2
user_bmi = int(bmi)
print(f"Your BMI is: {user_bmi}")


# Read Data from an Excel Worksheet in Python

#Add data to excel
sheet.append([first_name, surname, email, height_cm, weight_kg, user_bmi])