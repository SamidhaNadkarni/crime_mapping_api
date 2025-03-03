# UK Crime Mapping API

A Flask-based web application that allows users to search for crime data in UK byt entering zipcode and date. The app retrieves crime data fromt eh UK Police API and displays crime locations on an interactive Folium map.

Example of crime data visualisation on the map

## Installation & Setup
### clone the Repository
```
git clone git@github.com:SamidhaNadkarni/geo_crime_locations_uk.git
cd geo_crime_location_uk
```

### Create a virtual Environment (recommended)
```
python -m venv crime_venv
source crime_venv/bin/activate    # For Mac/Linux
crime_venv\Scripts\activate       # For Windows
```

### Install Dependencies
` pip install -r requirements.txt `

### Set Environment Variables
---------------------------optional

### Run the Flask App
` flask --app geo_crime_app run `

## Usage

## Running Tests
To run all the tests using pytest, from the root folder execute:
` pytest `


## Technologies Used
1. Flask - Web framework
2. Folium - Map visualisation
3. Geopy - Geolocation Services
4. Requests - API requests
5. Pytest - Unit testing

## Contributions
This project was built to learn about forms data, external API integration, templates, redirections, visualising maps and testing APIs. Please feel free to make contributions to the code and help me enhance my skills.  

## Further Improvements
