from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app=Flask(__name__)

#Local-Database: 'postgresql://<username-here>:<password-here>@localhost/<database-name>'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username-here>:<password-here>@localhost/<database-name>'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data" #tablename!
    id = db.Column(db.Integer, primary_key=True)
    email_col= db.Column(db.String(120), unique=True)
    age_col= db.Column(db.Integer)

    def __init__(self, email, age):
        self.email_col = str(email)
        self.age_col = int(age)

        

@app.route("/")
def index():
    #the main form
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=="POST":
        email = request.form["email_name"]
        age = request.form["age_name"]
        data = Data(email, int(age))
        # print(email+"\t"+age) #for debugging?
        if db.session.query(Data).filter(Data.email_col == email).count() == 0:
            db.session.add(data)
            db.session.commit()
            avg_age = db.session.query(func.avg(Data.age_col)).scalar()
            avg_age = round(avg_age,1)
            
            return render_template("success.html", avg1=avg_age)
        else:
            print(db.session.query(Data).filter(Data.email_col == email))
            avg_age = db.session.query(func.avg(Data.age_col)).scalar()
            avg_age = round(avg_age,2)
            return render_template("dupe.html", avg1=avg_age)
    else:
        return render_template("error2.html")

if __name__=="__main__":
    app.debug=True
    app.run()