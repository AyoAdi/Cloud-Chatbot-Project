# WiFi Troubleshooting Chatbot

## Overview
This project is a web-based **WiFi Troubleshooting Chatbot** that helps users diagnose and resolve common WiFi issues. The chatbot interface is built using HTML, CSS, and JavaScript, while the backend is powered by Flask and a machine learning model.

## Features
- **User-friendly chat interface** for entering WiFi-related issues.
- **Automated responses** based on trained AI models.
- **Flask-based backend** to handle queries and generate responses.
- **Seamless deployment support** with Gunicorn.
- **AWS Lambda integration** for serverless execution.

## Project Structure
```
project_root/
│── app.py               # Flask backend
│── requirements.txt     # Required dependencies
│
├── templates/
│   └── chatbot.html     # Frontend UI (HTML + CSS + JS)
│
└── aws_lambda/          # AWS Lambda function (not included in repo)
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

## AWS Lambda Integration
This project includes AWS Lambda for handling chatbot queries in a **serverless** environment.

### Steps to Deploy to AWS Lambda
1. Package your dependencies and function code:
   ```bash
   mkdir lambda_package
   cd lambda_package
   pip install -r ../requirements.txt -t .
   cp ../app.py .
   zip -r ../lambda_function.zip .
   ```

2. Upload `lambda_function.zip` to AWS Lambda.
3. Configure the Lambda function with the appropriate runtime and entry point (`app.lambda_handler`).
4. Attach an API Gateway to expose the Lambda function as an endpoint.
5. Use the API Gateway URL in the frontend to communicate with the chatbot.

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
- **AWS Lambda & API Gateway** (Serverless execution)

## Worked on by
K Adithya Vyas

