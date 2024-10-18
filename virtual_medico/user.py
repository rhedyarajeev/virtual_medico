@app.route('/user_registration', methods=['get', 'post'])
def user_registration():
    if request.method == "POST":
        name = request.form['textfield']
        house_name = request.form['textfield2']
        place = request.form['textfield3']
        pin_code = request.form['textfield4']
        gender = request.form['radio']
        age = request.form['textfield5']
        phone = request.form['textfield6']
        email_id = request.form['textfield7']
        district = request.form['select']
        password = random.randint(0000, 9999)

        db = Db()
        res = db.insert("insert into login values('', '"+email_id+"', '"+str(password)+"', 'user')")
        db.insert("insert into user values('"+str(res)+"', '"+name+"', '"+house_name+"', '"+place+"', '"+pin_code+"', '"+gender+"', '"+age+"', '"+phone+"', '"+email_id+"', '"+district+"')")
        
        return '''<script>alert('add successful');window.location="/"</script>'''
    else:
        return render_template('user/USER REGISTRATION.html')


@app.route('/view_doctor_us')
def view_doctor_us():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("select * from doctor, hospital where doctor.hospital_id = hospital.hospital_id")
        return render_template('user/view_doctor.html', data=ss)
    else:
        return redirect('/')


@app.route('/add_booking/<a>', methods=['get', 'post'])
def add_booking(a):
    if session['log'] == "lo":
        db = Db()
        db.insert("insert into booking values('', '"+str(session['lid'])+"', '"+str(a)+"', curdate())")
        return '''<script>alert('add successful');window.location="/view_doctor_us"</script>'''
    else:
        return redirect('/')


@app.route('/user_home')
def user_home():
    if session['log'] == "lo":
        return render_template("user/USER_HOME.html")
    else:
        return redirect('/')


@app.route('/user_view_pres')
def user_view_pres():
    if session['log'] == "lo":
        db = Db()
        res = db.select("select * from prescription, doctor, user, medicine, pharmacy where prescription.doctor_id = doctor.doctor_id and prescription.patient_id = user.user_id and prescription.medicine_id = medicine.medicine_id and medicine.pharmacy_id = pharmacy.pharmacy_id")
        return render_template('user/VIEW_PRESCRIPTION.html', data=res)
    else:
        return redirect('/')


@app.route('/purchase_med/<m>', methods=['get', 'post'])
def purchase_med(m):
    if session['log'] == "lo":
        if request.method == "POST":
            qnty = request.form['textfield']
            db = Db()
            db.insert("insert into `order` VALUES ('', '"+str(session['lid'])+"', '"+m+"', '"+qnty+"', curdate())")
            return '''<script>alert('DONE');window.location="/user_view_pres"</script>'''
        else:
            return render_template('user/ORDER.html')
    else:
        return redirect('/')


@app.route('/add_complaint_us', methods=['get', 'post'])
def add_complaint_us():
    if session['log'] == "lo":
        if request.method == "POST":
            complaint = request.form['textarea']
            db = Db()
            db.insert("insert into complaint values('', '"+str(session['lid'])+"', '"+complaint+"', curdate(), 'pending', 'pending')")
            return '''<script>alert('add successful');window.location="/add_complaint_us"</script>'''
        else:
            return render_template('user/ADD_COMPLAINT.html')
    else:
        return redirect('/')


@app.route('/add_feedback_us', methods=['get', 'post'])
def add_feedback_us():
    if session['log'] == "lo":
        if request.method == "POST":
            feedback = request.form['textarea']
            db = Db()
            db.insert("insert into feedback values('', '"+str(session['lid'])+"', '"+feedback+"', curdate())")
            return '''<script>alert('add successful');window.location="/add_feedback_us"</script>'''
        else:
            return render_template('user/ADD_FEEDBACK.html')
    else:
        return redirect('/')


@app.route('/view_pharmacy')
def view_pharmacy():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("select * from pharmacy")
        return render_template('user/VIEW_PHARMACY.html', data=ss)
    else:
        return redirect('/')


@app.route('/view_Reply')
def view_reply():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("select * from complaint")
        return render_template('user/VIEW_REPLAY.html', data=ss)
    else:
        return redirect('/')


@app.route('/view_department_us')
def view_department_us():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("select * from department")
        return render_template('user/VIEW_DEPARTMENT.html', data=ss)
    else:
        return redirect('/')


@app.route('/user_view_facility')
def user_view_facility():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("select * from facility, hospital where facility.hospital_id = hospital.hospital_id")
        return render_template('user/view_facility.html', data=ss)
    else:
        return redirect('/')
