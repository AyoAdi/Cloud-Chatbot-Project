# WiFi Troubleshooting Chatbot

## Overview
This project is a web-based **WiFi Troubleshooting Chatbot** that helps users diagnose and resolve common WiFi issues. The chatbot interface is built using HTML, CSS, and JavaScript, while the backend is powered by Flask and a machine learning model.

## Features
- **User-friendly chat interface** for entering WiFi-related issues.
- **Automated responses** based on trained AI models.
- **Flask-based backend** to handle queries and generate responses.
- **Seamless deployment support** with Gunicorn.

## Project Structure
```
project_root/
│── app.py               # Flask backend
│── requirements.txt     # Required dependencies
│
├── templates/
│   └── chatbot.html     # Frontend UI (HTML + CSS + JS)
```

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed along with **pip**.

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project_root
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open a web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Deployment
To deploy using **Gunicorn**:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Technologies Used
- **Flask** (Backend API)
- **Gunicorn** (Deployment)
- **Torch & Transformers** (AI/ML model integration)
- **HTML, CSS, JavaScript** (Frontend UI)

## License
This project is licensed under the **MIT License**.

## Author
Your Name

