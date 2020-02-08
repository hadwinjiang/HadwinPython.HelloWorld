
# Create venv
mkdir globomantics
cd globomantics/
python3 -m venv venv
source ./venv/bin/activate
pip install Flask
pip freeze > requirements.txt // pip install -r requirements.txt

# Run the Flask
export FLASK_ENV=development
export FLASK_APP=app.py
flask run
