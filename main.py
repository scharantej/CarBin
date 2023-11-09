 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(80))
    model = db.Column(db.String(80))
    year = db.Column(db.Integer)
    license_plate = db.Column(db.String(80))

    def __repr__(self):
        return '<Car %r>' % self.make

@app.route('/')
def home():
    cars = Car.query.all()
    return render_template('home.html', cars=cars)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'secret':
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid credentials')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        license_plate = request.form['license_plate']
        car = Car(make=make, model=model, year=year, license_plate=license_plate)
        db.session.add(car)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add_car.html')

@app.route('/view_car/<int:car_id>', methods=['GET', 'POST'])
def view_car(car_id):
    car = Car.query.get(car_id)
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        license_plate = request.form['license_plate']
        car.make = make
        car.model = model
        car.year = year
        car.license_plate = license_plate
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('view_car.html', car=car)

@app.route('/delete_car/<int:car_id>')
def delete_car(car_id):
    car = Car.query.get(car_id)
    db.session.delete(car)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


main.py file:


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(80))
    model = db.Column(db.String(80))
    year = db.Column(db.Integer)
    license_plate = db.Column(db.String(80))

    def __repr__(self):
        return '<Car %r>' % self.make

@app.route('/')
def home():
    cars = Car.query.all()
    return render_template('home.html', cars=cars)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'secret':
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid credentials')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        license_plate = request.form['license_plate']
        car = Car(make=make, model=model, year=year, license_plate=license_plate)
        db.session.add(car)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add_car.html')

@app.route('/view_car/<int:car_id>', methods=['GET', 'POST'])
def view_car(car_id):
    car = Car.query.get(car_id)
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        license_plate = request.form['license_plate']
        car.make = make
        car.model = model
        car.year = year
        car.license_plate = license_plate
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('view_car.html', car=car)

@app.route('/delete_car/<int:car_id>')
def delete_car(car_id):
    car = Car.query.get(car_id)
    db.session.delete(car)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
