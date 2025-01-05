# Student Card Generator 🎓

A web application built with Flask that allows students to generate professional student ID cards with their personal information.

## Tutorial Video 🎥
[Watch the tutorial video here](https://mega.nz/file/BikXFYDb#iKsEqNwvrVPLNE3w9NdZm7DV9kLCTbp_pt8sux9a0b8)

## Features 🌟
- User-friendly web interface
- Form-based data collection
- Professional card design with dark theme
- Screenshot functionality
- Responsive design for mobile and desktop
- Printable card format

## Prerequisites 📋
- Python 3.x installed
- pip (Python package manager)

## Quick Start 🚀

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install dependencies:
```bash
pip install flask pyautogui
```

3. Run the application:
```bash
python flaskapp.py
```

4. Open http://localhost:5000 in your browser

## Project Structure 📁
```
student-card-generator/
│
├── flaskapp.py           # Main Flask application
├── requirements.txt      # Project dependencies
│
├── static/
│   ├── indexStyle.css    # Styling for home page
│   └── submitStyle.css   # Styling for card preview
│
└── templates/
    ├── htmlindex.html    # Home page template
    └── htmlsubmit.html   # Card preview template
```

## Usage 💡
1. Click "Créer une Carte Étudiant" on home page
2. Fill in student information:
   - First Name
   - Last Name
   - Field of Study
   - National ID Card Number
   - Massar Code
   - Profile Picture
   - Email
   - Phone Number
3. Submit form to generate card
4. Use "Capture" button to save card as image

## Technologies Used 🛠️
- Backend: Python Flask
- Frontend: HTML, CSS
- Screenshot: PyAutoGUI

## Contributors 👥
- Mohamed Yacine Elfadili (elfadiliyacine@gmail.com | +212 6 50 32 92 24)
- Fahim Youssef (fahimyoussef964@gmail.com | +212 6 34 14 72 01)

## Institution 🏛️
Faculté Polydisciplinaire de Taroudant (FPT)
```
http://www.fpt.ac.ma/
```
