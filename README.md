1. Planning and Design:

- Layout: Simple with text input, label, button, background picture, etc.

----------------------
2. Front-End Development:

- Registration Form: Create an HTML form where users can enter their name, height, weight, and email.

- Reminder Option: Include a checkbox for users to opt-in for free reminders.

- Use CSS for styling and JavaScript (or a library like jQuery) for user interactions.

----------------------
3. Back-End Development:

- Database: Setup a database

- Sever: A server to handle requests.

- BMI Calculation: After form submission, calculate the BMI and determine health status.

- Email Integration: If the user opts-in for reminders, send them the daily reminders.

----------------------
4. Email Integration:
 
 - Integrate with an email service provider.

 - After user registration, send the user their BMI and health status.

 - If they've opted for reminders, send them daily emails with the dishes and training challenges.

----------------------
5. Content for Recommendations:

- Dishes: Maintain a list or database of healthy dishes.

- Training Challenges: Create a list/database of exercises, specifying the duration or repetition count for each.

----------------------
6. Security:

- Secure your database to prevent unauthorized access.

----------------------
7. Testing

- Heroku web hosting

- Deploy webpage.

----------------------
8. Launch!

- Send that shit to the Moon!


---------------------------------------------------------------
How to do it with python: (Chat GDP guidences below)

1. Prerequisites:

- Create a project and enable Google Docs and Google Sheets Api.

- Create a service account an download its JSON key.

- Install Python Packages or upgrade


2. Setting up the Spreadsheet on Google Sheets

-Create a new spreadsheet

-Share your spreadsheet with service account email(json key)

- Colums for Name, Height, Weight; Email and Dialogflow for Opt-in reminders.

3.  Python Script: (chat gdp guidelines below)

- Googlesheets connection:


import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_service_account.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Your_Spreadsheet_Name').sheet1

- Recive user data:

users = sheet.get_all_records()

- Process Data & send emails:

import smtplib

for user in users:
    name = user["Name"]
    height = user["Height"]
    weight = user["Weight"]
    email = user["Email"]
    opt_in = user["Opt-in"]
    
    bmi = weight / (height/100)**2  # Height is in cm and weight in kg

    # Calculate health status based on BMI...

    # If opted-in, generate dishes and training reminders...

    # Send email (using smtplib or another email library)
    # Gmail's SMTP for simplicity or another provider


4. Google Doc for BMI Info:

You can have a Google Doc template that you duplicate and populate with the user's info. To interact with Google Docs, use the googleapiclient library in Python. You'll need to find placeholders in the doc and replace them with the user's data.

5. Automating the Script:

You can run the Python script daily using a task scheduler. For Windows, you can use Task Scheduler. 





















![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. If you are using Gitpod then you need [this template](https://github.com/Code-Institute-Org/gitpod-full-template) instead.  We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **August 30th, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!
