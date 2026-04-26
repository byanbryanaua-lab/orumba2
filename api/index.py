import os
import sys

# Add parent directory to path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel serverless handler
def handler(request, response):
    """AWS Lambda / Vercel serverless handler wrapper."""
    from werkzeug.serving import run_wsgi
    return app(request.environ, response.start_response)

# For local testing
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
