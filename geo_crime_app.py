from flask import Flask,  render_template, request, redirect, url_for
from geopy.geocoders import Nominatim
import requests
import folium

app = Flask(__name__)

def get_api_data(address, crime_date):
    geolocator = Nominatim(user_agent="some_app")
    locate = geolocator.geocode(address)
    url = f'https://data.police.uk/api/crimes-street/all-crime?lat={locate.latitude}&lng={locate.longitude}&date={crime_date}'
    r = requests.get(url)
    if r.ok:
        return r.json()
    else:
        print(r.reason)
    
def get_crime_list(address, crime_date):
    global crime_data
    crime_data = get_api_data(address, crime_date)
    crime_category = []
    for c in crime_data:
        if c['category'] not in crime_category:
            crime_category.append(c['category'])
    return crime_category

def map_it(crime_selected):
    m = folium.Map([51.5240213, -0.0825212])
    print(f'inside the loop:{crime_selected}**')
    for cc in crime_data:
        if cc['category'] == crime_selected:
            #print('loop')
            folium.Marker(
                location=[cc['location']['latitude'], cc['location']['longitude']],
                #tooltip=cc['outcome_status']['category'],
                popup= cc['outcome_status']['category'],      #cc['location']['street']['name'],
                icon=folium.Icon(color='red'),
                ).add_to(m)
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()
    return iframe


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        address = request.form.get('address')
        crime_date = request.form.get('crime_date')
        crime_list = get_crime_list(address, crime_date)
        #crime_map(address, crime_list)
        return redirect(url_for('crime_map', crime=crime_list))
    return render_template('home.html')

@app.route('/crime', methods=['GET', 'POST'])
def crime_map():
    if request.method == 'POST':
        crime_selected = request.form.get('crime_selected')
        print(f'post: {crime_selected}')
        map_ = map_it(crime_selected)
        return render_template("location.html", crimes=crime_selected, iframe=map_)
    else:
        crime_list = request.args.getlist('crime')
        print(crime_list)
        return render_template('location.html', crimes=crime_list)

if __name__ == '__main__':
    app.run()
