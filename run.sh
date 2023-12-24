# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Run the Flask application in the background
export FLASK_APP=app.py
export FLASK_ENV=development
flask run &
