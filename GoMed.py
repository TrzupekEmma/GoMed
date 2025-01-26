from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, redirect, url_for

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

from modules import get_names, get_actor, get_id
import sharedProg
 
import sqlite3
import re

app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

conn1 = sqlite3.connect("GoMed.db");
cur1=conn1.cursor()
pharmacies=cur1.execute("select pNumber, pName, address from pharmacy order by pName, address").fetchall();
prescriptions=cur1.execute("select id, brandName from prescription").fetchall();
pharmaciesFancy = []
i = 0
for pharmacy in pharmacies[:8]:
    (num,name,address,)=pharmacy;
    pharmaciesFancy.append((num,str(name)+" on "+str(address),));
conn1.close();
# with Flask-WTF, each web form is represented by a class
# "NameForm" can change; "(FlaskForm)" cannot
# see the route for "/" and "index.html" to see how this is used
print(pharmacies);
class reportForm(FlaskForm):
    pharmacyChoice = SelectField("Pharmacy",choices=pharmaciesFancy);
    prescriptionChoice = SelectField("Prescription",choices=prescriptions);
    rating = SelectField("Was the Prescription available",choices=[(1,"Yes",),(0,"No")]);
#StringField('Which actor is your favorite? Type a complete name.', validators=[DataRequired(), Length(10, 40)])
    submit = SubmitField('Submit')


class searchForm(FlaskForm):
    prescriptionChoice = SelectField("Prescription",choices=prescriptions);
#StringField('Which actor is your favorite? Type a complete name.', validators=[DataRequired(), Length(10, 40)])
    submit = SubmitField('Search')
# all Flask routes below


@app.route('/')
def index():
    return render_template("Homepage.html");

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    conn = sqlite3.connect("GoMed.db");
    cur = conn.cursor()
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = reportForm()
    message = ""
    if form.validate_on_submit():
        pharmacyChoice = form.pharmacyChoice.data;
        prescriptionChoice = form.prescriptionChoice.data;
        Rating = form.rating.data;
        sharedProg.add_rating(conn,prescriptionChoice, pharmacyChoice,Rating)
	
        return redirect( url_for('success') )
    return render_template('index.html',form=form)
 
@app.route('/search', methods=['GET', 'POST'])
def search():
    conn = sqlite3.connect("GoMed.db");
    cur = conn.cursor()
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = searchForm()
    message = ""
    if form.validate_on_submit():
        prescriptionChoice = form.prescriptionChoice.data;
        print(prescriptionChoice);
        cur.execute("select avg(rating), pName, address from availabilityReport Join pharmacy on pharmacy=pNumber where prescription = ? group by pharmacy order by avg(rating)",prescriptionChoice);
        rows=cur.fetchall()
	
        if len(rows)>0:
            list=[];
            for row in rows:
                (rating,name,address,)=row;
                data={"Rating":str(rating*100)[0:4]+"% chance of being available","Pharmacy":name,"Address":address}
                list.append(data);
            # empty the form field
            # redirect the browser to another route and template
            conn.close();
            return render_template('display.html',form=form,list=list);
        else:
            message = "That medication doesn't have any data."
    return render_template("display.html", form=form, list=[])

@app.route('/success')
def success():
    return render_template("thankspage.html");

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
