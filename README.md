#Api Doc
https://documenter.getpostman.com/view/40098786/2sAYBXDBen


#Docker Run(Recommend)




#Local Run(Optional)
Backend
#setup ENV
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

#install package
pip install flask psycopg2-binary flask-sqlalchemy python-dotenv flask-cors

#start backend server
python app.py

Frontend
npm run serve