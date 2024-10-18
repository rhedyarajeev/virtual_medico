@app.route('/add_complaint', methods=['GET', 'POST'])
def add_complaint():
    if session['log'] == "lo":
        if request.method == "POST":
            complaint = request.form['textarea']
            db = Db()
            db.insert("INSERT INTO complaint VALUES ('', '" + str(session['lid']) + "', '" + complaint + "', CURDATE(), 'pending', 'pending')")
            return '''<script>alert('Add successful');window.location="/doctor_home"</script>'''
        else:
            return render_template('doctor/add_complaint.html')
    else:
        return redirect('/')


@app.route('/add_feedback', methods=['GET', 'POST'])
def add_feedback():
    if session['log'] == "lo":
        if request.method == "POST":
            feedback = request.form['textarea']
            db = Db()
            db.insert("INSERT INTO feedback VALUES ('', '" + str(session['lid']) + "', '" + feedback + "', CURDATE())")
            return '''<script>alert('Add successful');window.location="/doctor_home"</script>'''
        else:
            return render_template('doctor/add_feedback.html')
    else:
        return redirect('/')


@app.route('/update_doc', methods=['GET', 'POST'])
def update_doc():
    if session['log'] == "lo":
        if request.method == 'POST':
            doctor_name = request.form['textfield']
            specialisation = request.form['textfield2']
            email_id = request.form['textfield3']
            contact_no = request.form['textfield4']
            db = Db()
            db.update("UPDATE doctor SET doctor_name='" + doctor_name + "', specialisation='" + specialisation + "', email_id='" + email_id + "', contact_no='" + contact_no + "' WHERE doctor_id='" + str(session['lid']) + "'")
            return '''<script>alert('Update successful');window.location="/doctor_home"</script>'''
        else:
            db = Db()
            qry = db.selectOne("SELECT * FROM doctor, hospital WHERE doctor.hospital_id=hospital.hospital_id AND doctor.doctor_id='" + str(session['lid']) + "'")
            return render_template('doctor/update_doctor.html', data=qry)
    else:
        return redirect('/')


@app.route('/view_booking_doc')
def view_booking_doc():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM booking, user WHERE booking.user_id=user.user_id AND booking.doctor_id='" + str(session['lid']) + "'")
        return render_template('doctor/VIEW_BOOKING.html', data=ss)
    else:
        return redirect('/')


@app.route('/view_patient')
def view_patient():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM booking, user WHERE booking.user_id=user.user_id AND booking.doctor_id='" + str(session['lid']) + "'")
        return render_template('doctor/VIEW_BOOKING.html', data=ss)
    else:
        return redirect('/')


@app.route('/add_pres/<p>', methods=['GET', 'POST'])
def add_pres(p):
    if session['log'] == "lo":
        if request.method == "POST":
            med = request.form['select']
            dose = request.form['textfield']
            db = Db()
            db.insert("INSERT INTO prescription VALUES ('', '" + str(session['lid']) + "', '" + p + "', '" + med + "', '" + dose + "')")
            return '''<script>alert('Add successful');window.location="/view_patient"</script>'''
        else:
            db = Db()
            res = db.select("SELECT * FROM medicine, pharmacy WHERE medicine.pharmacy_id=pharmacy.pharmacy_id")
            return render_template('doctor/add_discription.html', data=res)
    else:
        return redirect('/')


@app.route('/view_user_doc')
def view_user_doc():
    if session['log'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM user")
        return render_template('doctor/VIEW_USER.html', data=ss)
    else:
        return redirect('/')


@app.route('/doctor_home')
def doctor_home():
    if session['log'] == "lo":
        return render_template("doctor/HOME_PAGE.html")
    else:
        return redirect('/')
