from flask import Flask,  render_template, request
from geopy.geocoders import Nominatim
import requests

geolocator = Nominatim(user_agent="some_app")

app = Flask(__name__)

def get_crime_data(url):
    crime_category = []
    r = requests.get(url)
    if r.ok:
            crimes = r.json()
    else:
        print(r.reason)
    for c in crimes:
        if c['category'] not in crime_category:
             crime_category.append(c['category'])
    return crime_category
         

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'POST':
        address = request.form.get('address')
        crime_date = request.form.get('crime_date')
        locate = geolocator.geocode(address)
        crime_url = f'https://data.police.uk/api/crimes-street/all-crime?lat={locate.latitude}&lng={locate.longitude}&date={crime_date}'
        crime_cats = get_crime_data(crime_url)
        crime_selected = request.form.get('crime')
        print(crime_selected)
        return render_template("location.html", crimes=crime_cats)

if __name__ == '__main__':
    app.run()

