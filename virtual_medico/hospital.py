@app.route('/hospital_home')
def hospital_home():
    if session['log'] == "lo":
        return render_template("hospital/home_page.html")
    else:
        return redirect('/')


@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if session['log'] == "lo":
        if request.method == "POST":
            doctor_name = request.form['textfield']
            specialisation = request.form['textfield2']
            email_id = request.form['textfield3']
            contact_no = request.form['textfield4']
            password = random.randint(0000, 9999)
            db = Db()
            res = db.insert("INSERT INTO login VALUES ('', '" + email_id + "', '" + str(password) + "', 'doctor')")
            db.insert("INSERT INTO doctor VALUES ('" + str(res) + "', '" + doctor_name + "', '" + specialisation + "', '" + email_id + "', '" + contact_no + "', '" + str(session['lid']) + "')")
            return '''<script>alert('Add successful');window.location="/add_doctor"</script>'''
        else:
            return render_template('hospital/add_doctor.html')
    else:
        return redirect('/')


@app.route('/view_doctor')
def view_doctor():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM doctor WHERE doctor.hospital_id='" + str(session['lid']) + "'")
        return render_template('hospital/view_doctor.html', data=ss)
    else:
        return redirect('/')


@app.route('/update_doctor/<did>', methods=['GET', 'POST'])
def update_doctor(did):
    if session['log'] == "lo":
        if request.method == 'POST':
            doctor_name = request.form['textfield']
            specialisation = request.form['textfield2']
            email_id = request.form['textfield3']
            contact_no = request.form['textfield4']
            db = Db()
            db.update("UPDATE doctor SET doctor_name='" + doctor_name + "', specialisation='" + specialisation + "', email_id='" + email_id + "', contact_no='" + contact_no + "', hospital_id='" + str(session['lid']) + "' WHERE doctor_id='" + did + "'")
            return '''<script>alert('Update successful');window.location="/view_doctor"</script>'''
        else:
            db = Db()
            qry = db.selectOne("SELECT * FROM doctor WHERE doctor_id='" + did + "'")
            return render_template('hospital/update_doctor.html', data=qry)
    else:
        return redirect('/')


@app.route('/delete_doctor/<did>')
def delete_doctor(did):
    if session['log'] == "lo":
        db = Db()
        db.delete("DELETE FROM doctor WHERE doctor_id='" + did + "'")
        return '<script>alert("Delete");window.location="/view_doctor"</script>'
    else:
        return redirect('/')


@app.route('/add_staff', methods=['GET', 'POST'])
def add_staff():
    if session['log'] == "lo":
        if request.method == "POST":
            staff_name = request.form['textfield']
            department_name = request.form['select']
            db = Db()
            res = db.insert("INSERT INTO staff VALUES ('', '" + str(session['lid']) + "', '" + staff_name + "', '" + department_name + "')")
            return '''<script>alert('Add successful');window.location="/hospital_home"</script>'''
        else:
            db = Db()
            qry = db.select("SELECT * FROM department")
            return render_template('hospital/add_staff.html', data=qry)
    else:
        return redirect('/')


@app.route('/view_staff')
def view_staff():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM staff, department WHERE staff.department_id=department.dept_id")
        return render_template('hospital/view_staff.html', data=ss)
    else:
        return redirect('/')


@app.route('/update_staff/<sid>', methods=['GET', 'POST'])
def update_staff(sid):
    if session['log'] == "lo":
        if request.method == 'POST':
            staff_name = request.form['textfield']
            department = request.form['select']
            db = Db()
            db.update("UPDATE staff SET hospital_id='" + str(session['lid']) + "', staff_name='" + staff_name + "', department_id='" + department + "' WHERE staff_id='" + sid + "'")
            return '''<script>alert('Update successful');window.location="/view_staff"</script>'''
        else:
            db = Db()
            qry = db.selectOne("SELECT * FROM staff, department WHERE staff.department_id=department.dept_id AND staff_id='" + sid + "'")
            res = db.select("SELECT * FROM department")
            return render_template('hospital/update_staff.html', data=qry, data1=res)
    else:
        return redirect('/')


@app.route('/delete_staff/<sid>')
def delete_staff(sid):
    if session['log'] == "lo":
        db = Db()
        db.delete("DELETE FROM staff WHERE staff_id='" + sid + "'")
        return '<script>alert("Delete");window.location="/view_staff"</script>'
    else:
        return redirect('/')


@app.route('/add_facility', methods=['GET', 'POST'])
def add_facility():
    if session['log'] == "lo":
        if request.method == "POST":
            facility_name = request.form['textfield']
            description = request.form['textarea']
            db = Db()
            db.insert("INSERT INTO facility VALUES ('', '" + str(session['lid']) + "', '" + facility_name + "', '" + description + "')")
            return '''<script>alert('Add successful');window.location="/add_facility"</script>'''
        else:
            return render_template('hospital/add_facility.html')
    else:
        return redirect('/')


@app.route('/view_facility')
def view_facility():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM facility WHERE hospital_id='" + str(session['lid']) + "'")
        return render_template('hospital/view_facility.html', data=ss)
    else:
        return redirect('/')


@app.route('/delete_facility/<fid>')
def delete_facility(fid):
    if session['log'] == "lo":
        db = Db()
        db.delete("DELETE FROM facility WHERE facility_id='" + fid + "'")
        return '<script>alert("Delete");window.location="/view_facility"</script>'
    else:
        return redirect('/')


@app.route('/update_facility/<fid>', methods=['GET', 'POST'])
def update_facility(fid):
    if session['log'] == "lo":
        if request.method == 'POST':
            facility_name = request.form['textfield']
            description = request.form['textarea']
            db = Db()
            db.update("UPDATE facility SET hospital_id='" + str(session['lid']) + "', facility_name='" + facility_name + "', description='" + description + "' WHERE facility_id='" + fid + "'")
            return '''<script>alert('Update successful');window.location="/view_facility"</script>'''
        else:
            db = Db()
            qry = db.selectOne("SELECT * FROM facility WHERE facility_id='" + fid + "'")
            return render_template('hospital/update_facility.html', data=qry)
    else:
        return redirect('/')


@app.route('/add_department', methods=['GET', 'POST'])
def add_department():
    if session['log'] == "lo":
        if request.method == "POST":
            department_name = request.form['textfield']
            db = Db()
            db.insert("INSERT INTO department VALUES ('', '" + department_name + "')")
            return '''<script>alert('Add successful');window.location="/add_department"</script>'''
        else:
            return render_template('hospital/add_department.html')
    else:
        return redirect('/')


@app.route('/view_department')
def view_department():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM department, staff WHERE staff.department_id=department.dept_id")
        return render_template('hospital/view_department.html', data=ss)
    else:
        return redirect('/')


@app.route('/delete_department/<bid>')
def delete_department(bid):
    if session['log'] == "lo":
        db = Db()
        db.delete("DELETE FROM department WHERE dept_id='" + bid + "'")
        return '<script>alert("Delete");window.location="/view_department"</script>'
    else:
        return redirect('/')


@app.route('/view_booking')
def view_booking():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM booking, user, doctor WHERE booking.user_id=user.user_id AND booking.doctor_id=doctor.doctor_id AND doctor.hospital_id='" + str(session['lid']) + "'")
        return render_template('hospital/view_booking.html', data=ss)
    else:
        return redirect('/')


@app.route('/view_user')
def view_user():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM user")
        return render_template('hospital/view_user.html', data=ss)
    else:
        return redirect('/')
