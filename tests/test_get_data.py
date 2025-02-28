from geo_crime_app.get_data import get_lat_long, get_crime_list

def test_get_lat_long():
    lat, lng = get_lat_long("E10 5NQ")
    assert lat is not None and lng is not None

def test_get_crime_list():
    crimes = get_crime_list("E10 5NQ", "2024-01")
    assert isinstance(crimes, list)