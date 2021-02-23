# EDC-Calculator

I used to always make mistake in those tedious Electronic Devices and Circuits amplifier analysis in lower semesters, hence I searched for various online platforms that would make EDC Calculations easier and faster - especially when you want to cross check the answers. Unfortunately I couldn't find any.
EDC Calculator is developed using Flask framework of Python and MySQL database on Xampp Server.

# Basic Setup
1. Download and Install Python. Set the path on your system.
2. Create the project folder using `mkdir EDC Calculator`
3. Create a virtual enviornment for the project : `py -3 -m venv venv`
4. Before you work on your project, activate the corresponding environment: `venv\Scripts\activate`

# Install Flask and dependency
1. Within the activated environment, use the following command to install Flask: `pip install Flask`
2. Install MySQL connector: `pip install mysql.connector`

# Run the project
1. Start the Xampp server and ennsure that you have the database named `edcflask` and table `user`. The table structure is as follows:
  a. user_id PK, AI, INTEGER(500)
  b. name VARCHAR(50)
  c. email VARCHAR(50)
  d. password VARCHAR(50)
2. Run `main.py` file
3. Open your browser and type the url: `http://127.0.0.1:5000/`

# Sample Output
1. LogIn Page

<img src="https://github.com/imatulkt/EDC-Calculator/blob/master/static/css/LogIn%20Page.png">

2. Register Page
<img src="https://github.com/imatulkt/EDC-Calculator/blob/master/static/css/Register%20Page.png">

3. Amplifier Calculator
<img src="https://github.com/imatulkt/EDC-Calculator/blob/master/static/css/Amplifier%20Gain%20Calculator.png">
