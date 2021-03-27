from flask import Flask, render_template, request
import folium
from geopy.geocoders import Nominatim

# This should be working
app = Flask(__name__)


@app.route("/index/")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Map", methods=['POST'])
def map():
    if request.method == 'POST':
        add = request.form["Address"]
        geolocator = Nominatim(user_agent="217.61.226.156")
        location = geolocator.geocode(add)
        Lat = location.latitude
        Lon = location.longitude
        zoom=request.form["Zoom"]
        f_map = folium.Map(location=[Lat, Lon], zoom_start=[zoom])
        f_map.save("templates/Map.html")
    return render_template("Map.html")


if __name__ == '__main__':
    app.run(debug=True)
