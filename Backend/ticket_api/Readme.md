###setup ENV

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

#install package
pip install flask psycopg2-binary flask-sqlalchemy python-dotenv flask-cors

#start backend server
python app.py
