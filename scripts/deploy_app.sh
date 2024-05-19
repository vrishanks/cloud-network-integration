#!/bin/bash
# Script to deploy the sample web application

# Navigate to the app directory
cd src/app

# Run the application (Flask example)
export FLASK_APP=app.py
flask run --host=0.0.0.0
