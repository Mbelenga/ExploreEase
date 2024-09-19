from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'cfb53753ab86181b235fec27f2062feaea0bf48fdaa99e3a'

# Simulate a flight search with mock data
def search_flights(departure, destination, departure_date, return_date):
    """Simulate a flight search with static data."""
    return [
        {
            'airline': 'Kenya Airways',
            'departure_city': departure,
            'destination_city': destination,
            'price': 450
        },
        {
            'airline': 'Emirates',
            'departure_city': departure,
            'destination_city': destination,
            'price': 650
        },
        {
            'airline': 'Qatar Airways',
            'departure_city': departure,
            'destination_city': destination,
            'price': 600
        }
    ]

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
    flights = []
    if request.method == 'POST':
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        departure_date = request.form.get('departure-date')
        return_date = request.form.get('return-date')

        # Simulate a flight search and return results
        flights = search_flights(departure, destination, departure_date, return_date)

        # Store selected flight details in session if needed
        session['flight'] = {
            'departure': departure,
            'destination': destination,
            'departure_date': departure_date,
            'return_date': return_date,
            'flights': flights  # Store available flights (or selected one)
        }

    return render_template('flights.html', flights=flights)

def get_attractions_from_api(query):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'fsq3QsHMBoW5VtmisozkgOwHed542bGf5tqrKJY0oHDjSJ0='
    }
    
    params = {
        'query': query,
        'limit': 10  # You can change this number depending on how many results you want
    }
    
    api_url = 'https://api.foursquare.com/v3/places/search'
    
    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()
        return data.get('results', [])  # Return the list of attractions from the JSON response
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return []  # Return an empty list if the API call fails

@app.route('/attractions', methods=['GET', 'POST'])
def attractions():
    query = ''
    
    if request.method == 'POST':
        query = request.form.get('query', '')  # Get query from form submission
        
    elif request.method == 'GET':
        query = request.args.get('query', '')  # Get query from URL query parameters
    
    suggestions = get_attractions_from_api(query)  # Call the function to get API results
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