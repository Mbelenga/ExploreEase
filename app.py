from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/stays')
def stays():
    return render_template('stays.html')

@app.route('/flights', methods=['GET', 'POST'])
def flights():
    if request.method == 'POST':
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        departure_date = request.form.get('departure-date')
        return_date = request.form.get('return-date')
        # Handle flight search logic here
        # For now, render the page with submitted data
        return render_template('flights.html', departure=departure, destination=destination, departure_date=departure_date, return_date=return_date)
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
        pickup_location = request.form.get('pickup-location')
        dropoff_location = request.form.get('dropoff-location')
        # Handle cab booking logic here
        # For now, render the page with submitted data
        return render_template('cabs.html', pickup_location=pickup_location, dropoff_location=dropoff_location)
    return render_template('cabs.html')

if __name__ == '__main__':
    app.run(debug=True)