from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'cfb53753ab86181b235fec27f2062feaea0bf48fdaa99e3a'

# Sample data for demonstration purposes
attractions_list = [
    "Eiffel Tower, Paris",
    "Louvre Museum, Paris",
    "Statue of Liberty, New York",
    "Central Park, New York",
    "Great Wall of China, Beijing",
    "Forbidden City, Beijing",
]

def get_suggestions(query, data_list):
    """Get search suggestions based on user query."""
    suggestions = [item for item in data_list if query.lower() in item.lower()]
    return suggestions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stays', methods=['GET', 'POST'])
def stays():
    if request.method == 'POST':
        # Store stay booking in session
        session['stay'] = {
            'destination': request.form['destination'],
            'checkin': request.form['checkin'],
            'checkout': request.form['checkout'],
            'guests': request.form['guests'],
            'rooms': request.form['rooms']
        }
        return redirect(url_for('payment'))  # Redirect to payment or summary page
    return render_template('stays.html')

@app.route('/flights', methods=['GET', 'POST'])
def flights():
    if request.method == 'POST':
        # Store flight booking in session
        session['flight'] = {
            'departure': request.form.get('departure'),
            'destination': request.form.get('destination'),
            'departure_date': request.form.get('departure-date'),
            'return_date': request.form.get('return-date')
        }
        return redirect(url_for('payment'))  # Redirect to payment or summary page
    return render_template('flights.html')

@app.route('/attractions', methods=['GET', 'POST'])
def attractions():
    suggestions = []
    if request.method == 'POST':
        query = request.form.get('attraction-destination')
        suggestions = get_suggestions(query, attractions_list)
    return render_template('attractions.html', suggestions=suggestions)

@app.route('/cabs', methods=['GET', 'POST'])
def cabs():
    if request.method == 'POST':
        # Store cab booking in session
        session['cab'] = {
            'pickup_location': request.form.get('pickup-location'),
            'dropoff_location': request.form.get('dropoff-location')
        }
        return redirect(url_for('payment'))  # Redirect to payment or summary page
    return render_template('cabs.html')

@app.route('/payment')
def payment():
    # Get bookings from session and pass to the template
    stay = session.get('stay')
    flight = session.get('flight')
    cab = session.get('cab')
    return render_template('payment.html', stay=stay, flight=flight, cab=cab)

if __name__ == '__main__':
    app.run(debug=True)