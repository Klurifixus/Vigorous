# Libraries to open excel
from spire.xls import Workbook

# Create or load a workbook
workbook = Workbook()
workbook.LoadFromFile("database.xlsx")

# Get the first worksheet
worksheet = workbook.Worksheets[0]

# User Input
first_name = input("First name: ")
surname = input("Surname: ")
mail = input("Email address: ")
height = input("Height in centimeters: ")
weight = input("Weight in kilograms: ")

# Autoget next available user number
if worksheet.Range["A2"].Value:
    last_row = worksheet.LastRow
    next_user_number = worksheet.Range[f"A{last_row}"].NumberValue + 1
else:
    next_user_number = 1

# Calculate BMI
weight_kg = int(weight)
height_cm = float(height)
bmi = weight_kg / (height_cm / 100) ** 2
user_bmi = int(bmi)
print(f"Dear {first_name} your BMI is: {user_bmi}")

# Add data to excel
next_row = worksheet.LastRow + 1
worksheet.Range[f"A{next_row}"].NumberValue = next_user_number
worksheet.Range[f"B{next_row}"].Text = first_name
worksheet.Range[f"C{next_row}"].Text = surname
worksheet.Range[f"D{next_row}"].Text = mail
worksheet.Range[f"E{next_row}"].NumberValue = height_cm
worksheet.Range[f"F{next_row}"].NumberValue = weight_kg
worksheet.Range[f"G{next_row}"].NumberValue = user_bmi

# Save data to excel
workbook.SaveToFile("database.xlsx")