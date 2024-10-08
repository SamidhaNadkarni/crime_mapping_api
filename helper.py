from geopy.geocoders import Nominatim
import requests
import folium

def get_lat_long(address):
    geolocator = Nominatim(user_agent="some_app")
    locate = geolocator.geocode(address)
    return (locate.latitude, locate.longitude)

def get_api_data(address, crime_date):
    latitude, longitude = get_lat_long(address)
    url = f'https://data.police.uk/api/crimes-street/all-crime?lat={latitude}&lng={longitude}&date={crime_date}'
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
    for cc in crime_data:
        if cc['category'] == crime_selected:
            folium.Marker(
                location=[cc['location']['latitude'], cc['location']['longitude']],
                #tooltip=cc['outcome_status']['category'],
                popup= cc['outcome_status']['category'],      #cc['location']['street']['name'],
                icon=folium.Icon(color='red'),
                ).add_to(m)
    m.get_root().width = '800px'
    m.get_root().height = '600px'
    iframe = m.get_root()._repr_html_()
    return iframe
