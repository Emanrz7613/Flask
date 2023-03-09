from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret'

ORGANIZATIONS = ['Club A', 'Club B', 'Club C', 'Club D', 'Club E']
registrations = {}

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', orgs=ORGANIZATIONS)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    org = request.form.get('org')
    
    if not name:
        flash('Please enter your name.')
        return redirect(url_for('home'))

    if not org:
        flash('Please select an organization.')
        return redirect(url_for('home'))

    if org not in ORGANIZATIONS:
        flash('Invalid organization.')
        return redirect(url_for('home'))

    # Check if user already exists
    if name in registrations:
        flash(f'{name} is already registered for {registrations[name]}.')
    else:
        registrations[name] = org
        flash(f'{name} has been registered for {org}.')

    return redirect(url_for('registered_students'))

@app.route('/registered', methods=['GET'])
def registered_students():
    return render_template('registered.html', students=registrations.items())

if __name__ == '__main__':
    app.run(debug=True)
