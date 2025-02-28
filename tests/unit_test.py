from geo_crime_app.get_data import get_lat_long

def test_get_lat_long():
    lat, long = get_lat_long("E15 4HJ")
    assert isinstance(lat, float)
    assert isinstance(long, float)

