from flask import Flask, render_template, request
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="web_app",
    user="postgres",
    password="admin"
)

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/collectdata',methods=['GET','POST'])
def collectdata():
    if request.method=='POST':
        fullname = request.form.get('fullname')
        isdcode = request.form.get('isdcode')
        mobileno = request.form.get('mobileno')
        email = request.form.get('email')
        cur = conn.cursor()
        cur.execute(
        "INSERT INTO main_form_data (full_name, isd_code, mobile_no, email) VALUES (%s, %s, %s, %s)", (fullname, isdcode, mobileno, email))
        conn.commit()

        return 'Data Submitted Successfully'

    return render_template("collectdata.html")


if __name__ == '__main__':
    app.run()