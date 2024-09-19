ExploreEase
Overview
ExploreEase is a travel booking platform that enables users to book flights, hotels, and cabs, as well as explore local attractions. Built with a focus on user experience and simplicity, ExploreEase aims to streamline the travel planning process.

Table of Contents
Technologies Used
APIs Integrated
Installation
Usage
Features
Challenges Faced
Future Improvements
Contributing
License
Technologies Used
Frontend:

HTML
CSS
JavaScript (with Chart.js for data visualization)
Backend:

Python
Flask framework
Database:

MySQL (or PostgreSQL)
Development Tools:

Git
GitHub
Visual Studio Code (or your preferred IDE)
APIs Integrated
Foursquare Places API:

Used for retrieving information on attractions, hotels, and restaurants.
Challenges faced: Difficulty in getting accurate data for attractions and hotels.
Planned APIs:

Amadeus API: For flight and hotel booking services.
Skyscanner API: For comprehensive flight and hotel searches.
Mpesa API: For payment processing.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/mbelenga/exploreease.git
Navigate to the project directory:

bash
Copy code
cd exploreease
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Set up the database (if applicable) and configure environment variables as needed.

Usage
Start the Flask server:

bash
Copy code
flask run
Open your browser and navigate to http://127.0.0.1:5000 to access ExploreEase.

Features
User-friendly interface: Intuitive design for easy navigation.
Search functionality: Allows users to search for flights, hotels, and attractions.
Booking system: Facilitates bookings for flights, hotels, and cabs.
Dynamic suggestions: Provides suggestions for local attractions based on user input.
Challenges Faced
Foursquare API: Encountered issues retrieving data for attractions and hotels.
Flight/Hotel APIs: Difficulty integrating Amadeus and Skyscanner.
Payment Integration: Challenges with integrating Mpesa for payment processing.
Future Improvements
Complete integration of Skyscanner and Amadeus APIs for reliable flight and hotel booking.
Enhance the Mpesa payment gateway or consider alternative payment options.
Implement advanced search features and error handling.
Improve the user interface for a more engaging experience.
