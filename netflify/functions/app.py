"""
Netlify serverless function wrapper for Flask app
"""
import sys
import os

# Add the parent directory to the path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import app

# Serverless WSGI handler
try:
    from serverless_wsgi import handle_request
except ImportError:
    # Fallback if serverless_wsgi is not available
    def handle_request(app, event, context):
        return {
            'statusCode': 500,
            'body': 'serverless_wsgi module not found. Install it with: pip install serverless-wsgi'
        }

def handler(event, context):
    return handle_request(app, event, context)