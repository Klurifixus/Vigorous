what has been done: 

1. Started out with a guide from udemy with some basics from: 100 Days of Code: The Complete Python Pro Bootcamp for 2023 with Angela Wu. this was the startingpoint for me to create a bmi Calculator.

2. Then i watched : https://www.youtube.com/watch?v=4F9jnTDvxv0&list=PLeqKi_WI1m2fp6nZGwlleEFCeb92rS4Q2

* Point 1 and 2 above helped me to start writing the actual code.
(in additional a have watch all information on codeinstitute for pp3.)

(pretty soon i realized i had problems to read the excelfile). and one of the problem was that i used widows and the system file wasn't accessiblebecause of two installed pythons from an earlier point.)

* Here is how to solve that problem after you first ensured yourself that you have uninstalled all python on your computer and then reinstalled the latest version:

-Add Python to PATH
    1. Search for "Environment Variables" on your computer.
    2. Select "Edit the system's environment variables."
    3. Click on "Environment Variables..." at the bottom right.
    4. Under "System Variables," look for a variable named "Path" and double-click it.
    5. Click "New" and add the path to your Python installation and the Scripts folder. Typically, these are: 

    - C:\Users\[YourUsername]\AppData\Local\Programs\Python\[PythonVersion]\
    - C:\Users\[YourUsername]\AppData\Local\Programs\Python\[PythonVersion]\Scripts\
    6. Click "OK" until you're back on the desktop.

--------------------------LINKS------------------------



How to Create a GitHub Account (2023) - Full Tutorial: https://www.youtube.com/watch?v=Gn3w1UvTx0A

Video about heroku signup: https://www.youtube.com/watch?v=6WREMAr8mS4

- First-Time Git Setup: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

- Getting Started on Heroku with Python: https://devcenter.heroku.com/articles/getting-started-with-python#create-and-deploy-the-app

- Link to Download Python: https://www.python.org/downloads/

- Link to Install Python and much more: https://www.python.org/about/gettingstarted/

- Link on how to install Spire.XLS for Python in VS Code: https://www.e-iceblue.com/Tutorials/Python/Spire.XLS-for-Python/Getting-Started/How-to-Install-Spire.XLS-for-Python-in-VS-Code.html

- Link on how to install Pandas for Python in VS Code: https://www.pythoncentral.io/how-to-install-pandas-in-python/

- Link on how to install openpyxl for Python in VS Code: https://www.geeksforgeeks.org/how-to-install-openpyxl-in-python-on-windows/

- Dockerize Your Python Flask application and deploy it onto Heroku:  https://medium.com/analytics-vidhya/dockerize-your-python-flask-application-and-deploy-it-onto-heroku-650b7a605cc9

* Unfortunately in my trails and arrows i had made more problems for my self as i tried to make it work with fist openpyxl then spire.xls and later on with pandas again.
And while i was trying thing out I installed a Virtual Enviroment (myenv) that made me problems i had problems with how to get ridd of. But after I reInstalled python  

With these commands i finaly made it work in these steps below:

- I gave my self admin- promission to delete the whole myenv folder with all in it in my main branch, this made it delete the files on my computer as well. 
- C:\Users\XXXXXX\AppData\Local\Programs\Python\Python312\python.exe
- python -m pip install --upgrade pip
- python -m pip uninstall pandas openpyxl
- pip install openpyxl
- pip install pandas

And after that i was up running again. Now with the purpose of using pandas for the excel files.


3. I used inspiration from Alice Yang aswell when i started working with this. A really well done guide.
https://medium.com/@alice.yang_10652/read-data-from-excel-files-in-python-a-comprehensive-guide-bbf91d38d7c5


4. I have to be honest, with out Chat GPT i wouldnt have solved the problems with paths this way. I belive i would have spent a lot of hours finding information but not solved it totaly. And in the end i would have reinstalled my whole computer. Spend hours collecting pages and logins for everything. And now i dont have to. And for being an online student , it is awesome when you dont understand. you just askes what does this do? or give me all values of this style and explain the diffrence or something like that. And thats good enought. Dont trust it completely doe, it has its flaws and sometimes it puts you in the wrong path of finding the answears. 





-------------Starting with NVP.---------------------



Future features:
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
How to do it with python: (Chat GPT guidences below)

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
