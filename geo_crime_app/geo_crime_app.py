from . import create_app
from flask import render_template, request, redirect, url_for
import geo_crime_app.get_data as h

app = create_app('default')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        address = request.form.get('address')
        crime_date = request.form.get('crime_date')
        crime_list = h.get_crime_list(address, crime_date)
        return redirect(url_for('crime_map', crime=crime_list))
    return render_template('home.html')

@app.route('/crime', methods=['GET', 'POST'])
def crime_map():
    if request.method == 'POST':
        crime_selected = request.form.get('crime_selected')
        map_ = h.map_it(crime_selected)
        return render_template('crime_map.html', crimes=crime_selected, iframe=map_)
    else:
        crime_list = request.args.getlist('crime')
        return render_template('crime_map.html', crimes=crime_list)

if __name__ == '__main__':
    app.run()
