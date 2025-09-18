# ISS-Overhead-Detector
A Python script that sends an email notification when the International Space Station is overhead at your location during night time.

ISS Overhead Notifier
---------------------

This Python script sends you an email notification when the International Space Station (ISS) is above your location at night.  
It uses real-time data from the Open Notify ISS API (http://api.open-notify.org/iss-now.json) and the Sunrise-Sunset API (https://sunrise-sunset.org/api).

---------------------
Features
---------------------
- Detects if the ISS is within ±5° latitude and longitude of your position.
- Checks if it is currently nighttime at your location.
- Sends an automated email alert so you do not miss seeing the ISS.

---------------------
Requirements
---------------------
- Python 3.7+
- Libraries:
  - requests
- Access to an SMTP server (for example: Gmail, Outlook, Yahoo)

---------------------
Installation
---------------------
1. Clone this repository:
   git clone https://github.com/your-username/iss-overhead-notifier.git
   cd iss-overhead-notifier

2. Install dependencies:
   pip install -r requirements.txt

3. Set up environment variables:
   Create a file named .env in the project root with the following content:

   MY_EMAIL=your_email@example.com
   MY_PASSWORD=your_password_here
   MY_LAT=12.34
   MY_LONG=56.78
   SMTP_ADDRESS=smtp.gmail.com

---------------------
Usage
---------------------
Run the script with:
   python main.py

The script will:
1. Check every 60 seconds if the ISS is overhead.
2. Verify if it is nighttime at your location.
3. Send you an email alert if both conditions are true.

---------------------
Project Structure
---------------------
.
├── main.py           (Main script)
├── requirements.txt  (Dependencies)
├── .gitignore        (Ignored files)
├── .env.example      (Example environment file)
└── README.txt        (Project documentation)

---------------------
Security Notes
---------------------
- Do not commit your .env file to GitHub.
- Keep your email and password private.
- Use an app-specific password if your email provider supports it (recommended).

---------------------
License
---------------------
This project is licensed under the MIT License. You are free to use, modify, and share it.

---------------------
Tags
---------------------
python, api, automation, email, iss, space
