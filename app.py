from flask import Flask, render_template, request, session, redirect, url_for
import requests  # Import requests for API calls

app = Flask(__name__)
app.secret_key = 'cfb53753ab86181b235fec27f2062feaea0bf48fdaa99e3a'

# Foursquare Places API key
FOURSQUARE_API_KEY = 'fsq3QsHMBoW5VtmisozkgOwHed542bGf5tqrKJY0oHDjSJ0'

def get_attractions_from_api(destination):
    """Get attractions using the Foursquare API."""
    url = 'https://api.foursquare.com/v3/places/search'
    headers = {
        'Authorization': FOURSQUARE_API_KEY
    }
    params = {
        'query': 'attractions',
        'near': destination,
        'limit': 10
    }
    
    response = requests.get(url, headers=headers, params=params)

    # Debugging: Log response details to check if API call is successful
    print(f"API Response Status Code: {response.status_code}")
    print(f"API Response Text: {response.text}")

    if response.status_code == 200:
        data = response.json()
        return [
            {
                'name': place.get('name'),
                'location': place['location'].get('formatted_address', 'Unknown location')
            }
            for place in data.get('results', [])
        ]
    else:
        # Log error details if API call fails
        print(f"Error fetching data: {response.status_code}, {response.text}")
        return []  # Return an empty list if the API call fails

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
        
        # Fetch attractions from the API
        suggestions = get_attractions_from_api(query)
    
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

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)