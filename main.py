from os import environ
from flask import Flask, request
from db import Db

class Main:
    def __init__(self) -> None:
        pass

    def auth(self, x):
        if x == environ.get('SLACK_TOKEN'):
            pass
        else:
            return 'Unauthorized', 401
    
    def dbOrientation(self, x, y):
        db = Db(x, y)
        dbname = db.newDB()
        user = db.newUser()
        grant = db.grantAccess()
        
        username = user[0]
        passw = user[1]

        return 'database: ' + dbname + ' username: ' + username + ' password: ' + passw + ' status: ' + grant
        
    
    def initDb(self):
        token = request.form.get('token')
        self.auth(token)
        
        data = request.form.get('text')
        split = data.split(" ")
        db = self.dbOrientation(split[0], split[1])
        return db

app = Flask(__name__)
@app.route('/initdb', methods=['POST'])
def initdb():
    msg = Main().initDb()
    return msg

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(environ.get('PORT', 5000)))
