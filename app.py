"""
Entry point for the Resume Analyzer application.
This file imports the Flask app from the backend directory.
"""
import sys
import os

# Add the resume_analyzer directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resume_analyzer'))

# Import the Flask app from the backend module
from resume_analyzer.backend.app import app

# This allows the app to be run directly with 'python app.py'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
