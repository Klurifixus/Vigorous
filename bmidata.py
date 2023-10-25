#libary to open excel
import openpyxl

# Connect to excel
filename = "database.xlsx"
workbook = openpyxl.load_workbook(filename)
sheet = workbook.active


# User Input
first_name = input("First name: ")
surname = input("Surname: ")
mail = input("Email address: ")
height = input("Height in centimeters: ")
weight = input("Weight in kilograms: ")

# Autoget next availible user number
if sheet.cell(row=2, column=1).value:
    last_row = sheet.max_row
    next_user_number = sheet.cell(row=last_row, column=1).value + 1
else:
    next_user_number = 1    


# Calculate BMI
weight_kg = int(weight)
height_cm = float(height)
bmi = weight_kg / (height_cm / 100) ** 2
user_bmi = int(bmi)
print(f"Dear {first_name} your BMI is: {user_bmi}")


#Add data to excel
sheet.append([next_user_number, first_name, surname, mail, height_cm, weight_kg, user_bmi])

#save data to excel
workbook.save(filename)