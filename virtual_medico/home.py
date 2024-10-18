import random
import sys
from flask import Flask, render_template, request, redirect, session  # type: ignore

# Add the current directory to the Python path to find Dbconnection
sys.path.append(r'C:\Users\redhyarajeev\Desktop\virtual_medico')

from Dbconnection import Db  # type: ignore

app = Flask(__name__)
app.secret_key = "kkkk"

@app.route('/', methods=['get', 'post'])
def login():
    if request.method == "POST":
        username = request.form['textfield']
        password = request.form['textfield2']
        db = Db()
        res = db.selectOne("SELECT * FROM login WHERE user_name = %s AND password = %s", (username, password))
        
        if res:
            session['log'] = "lo"
            session['lid'] = res['login_id']
            return redirect(f'/{res["user_type"]}_home')  # Redirect based on user type
        else:
            return '''<script>alert('User not found or invalid password');window.location="/"</script>'''
    else:
        return render_template("login.html")

@app.route('/admin_home')
def admin_home():
    if session.get('log') == "lo":
        return render_template('admin/admin_home.html')
    return redirect('/')

@app.route('/add_hospital', methods=['get', 'post'])
def add_hospital():
    if session.get('log') == "lo":
        if request.method == "POST":
            hospital_name = request.form['textfield']
            place = request.form['textfield2']
            post = request.form['textfield3']
            district = request.form['select']
            pin = request.form['textfield5']
            contact_no = request.form['textfield6']
            email_id = request.form['textfield4']
            password = random.randint(1000, 9999)  # Ensure 4 digits
            db = Db()
            res = db.insert("INSERT INTO login (email_id, password, user_type) VALUES (%s, %s, 'hospital')", (email_id, str(password)))
            db.insert("INSERT INTO hospital (login_id, hospital_name, place, post, district, pin, contact_no, email_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (res, hospital_name, place, post, district, pin, contact_no, email_id))
            return '''<script>alert('Register successful');window.location="/admin_home"</script>'''
        return render_template('admin/add_hospital.html')
    return redirect('/')

@app.route('/add_notification', methods=['get', 'post'])
def add_notification():
    if session.get('log') == "lo":
        if request.method == "POST":
            notification = request.form['textarea']
            db = Db()
            db.insert("INSERT INTO notification (notification, date) VALUES (%s, CURDATE())", (notification,))
            return '''<script>alert('Add Notification');window.location="/admin_home"</script>'''
        return render_template('admin/add_notification.html')
    return redirect('/')

@app.route('/view_hospital')
def view_hospital():
    if session.get('log') == "lo":
        db = Db()
        ss = db.select("SELECT * FROM hospital")
        return render_template('admin/view_hospital.html', data=ss)
    return redirect('/')

@app.route('/delete_hospital/<hid>')
def delete_hospital(hid):
    if session.get('log') == "lo":
        db = Db()
        db.delete("DELETE FROM hospital WHERE hospital_id = %s", (hid,))
        return '''<script>alert("Delete");window.location="/view_hospital"</script>'''
    return redirect('/')

@app.route('/edit_hospital/<hid>', methods=['get', 'post'])
def edit_hospital(hid):
    if session.get('log') == "lo":
        if request.method == "POST":
            hospital_name = request.form['textfield']
            place = request.form['textfield2']
            post = request.form['textfield3']
            district = request.form['select']
            pin = request.form['textfield5']
            contact_no = request.form['textfield7']
            email_id = request.form['textfield6']
            db = Db()
            db.update("UPDATE hospital SET hospital_name = %s, place = %s, post = %s, district = %s, pin = %s, contact_no = %s, email_id = %s WHERE hospital_id = %s", (hospital_name, place, post, district, pin, contact_no, email_id, hid))
            return '''<script>alert('Update successful');window.location="/view_hospital"</script>'''
        db = Db()
        res = db.selectOne("SELECT * FROM hospital WHERE hospital_id = %s", (hid,))
        return render_template('admin/edit_hospital.html', data=res)
    return redirect('/')

@app.route('/view_pharmacy_rqst')
def view_pharmacy_rqst():
    if session.get('log') == "lo":
        db = Db()
        ss = db.select("SELECT * FROM login, pharmacy WHERE login.login_id = pharmacy.pharmacy_id AND login.user_type='pending'")
        return render_template('admin/approve_pharmacy.html', data=ss)
    return redirect('/')

@app.route('/approve_pharmacy/<id>')
def approve_pharmacy(id):
    if session.get('log') == "lo":
        db = Db()
        db.update("UPDATE login SET user_type = 'pharmacy' WHERE login_id = %s", (id,))
        return '''<script>alert('Approved');window.location="/view_pharmacy_rqst"</script>'''
    return redirect('/')

@app.route('/reject_pharmacy/<id>')
def reject_pharmacy(id):
    if session.get('log') == "lo":
        db = Db()
        db.delete("DELETE FROM login WHERE login_id = %s", (id,))
        db.delete("DELETE FROM pharmacy WHERE pharmacy_id = %s", (id,))
        return '''<script>alert('Rejected');window.location="/view_pharmacy_rqst"</script>'''
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
