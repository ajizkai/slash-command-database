import psycopg2
import string
import random

from os import environ

class Db:
    def __init__(self, uname, dbname) -> None:

        self.uname = uname
        self.dbname = dbname

        db = psycopg2.connect(user=environ.get('DB_USER'),password=environ.get('DB_PASS'), 
                              host=environ.get('DB_URL'), 
                              port=environ.get('DB_PORT'), 
                              database=environ.get('DB_DEFAULT'))

        db.autocommit = True

        self.cursor = db.cursor()
        pass
    
    def newDB(self):
        self.cursor.execute("create database " + self.dbname)
        return self.dbname

    def pass_gen(self):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        all = lower + upper + num
        temp = random.sample(all, 8)
        passw = "".join(temp)
        return passw

    def newUser(self):
        pas = self.pass_gen()
        passw = "'" + pas + "'"
        self.cursor.execute("create user " + self.uname + 
                            " with encrypted password " + passw + ";")
        return self.uname,pas

    def grantAccess(self):
        self.cursor.execute("GRANT ALL PRIVILEGES ON DATABASE "+ self.dbname +
                            " TO " + self.uname + ";")
        return "Granted"

