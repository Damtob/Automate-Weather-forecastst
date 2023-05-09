# Automate-Weather-forecastst
Auto-generate daily weather forecast social media posts through pre-made templates and OpenWeatherMap API.

Welcome to Automate-Weather-Forecasts! 
This project is a simple weather forecasting application that uses an API to fetch the current weather conditions for a specified location at time. This README will guide you through the installation and setup of the application.

INSTALLATION
Clone the repository from Github:
https://github.com/Damtob/Automate-Weather-forecastst.git

INSTALL THE REQUIRED PACKAGES:
pip install -r requirements.txt

CREATE A .ENV FILE IN THE ROOT DIRECTORY OF THE PROJECT WITH THE FOLLOWING CONTENTS:
API_KEY=your_api_key
SENDER_EMAIL=your_sender_email
SENDER_PASSWORD=your_sender_password
RECIPIENT_EMAIL=your_recipient_email
Note: Replace your_api_key, your_sender_email, your_sender_password, and your_recipient_email with your own values.

Run the main.py file:
python main.py

USAGE
Once the application is running, it will prompt you to enter the name of a city or town for which you want to retrieve the weather forecast. After you enter the city or town name, the application will fetch the current weather conditions for that location and send them to the specified email address.

CONTRIBUTING
If you would like to contribute to this project, please fork the repository and submit a pull request. All contributions are welcome!

LICENSE
This project is licensed under the MIT License - see the LICENSE file for details.
