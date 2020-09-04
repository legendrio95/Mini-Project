import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_prodcer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'blue'


map = folium.Map(location=[25.587993, 85.179487],
                 zoom_start=17, titles="Stamen Terrain")

var = folium.FeatureGroup(name="Home")
var_vol = folium.FeatureGroup(name="Volcano")
var_poly = folium.FeatureGroup(name="Population")

var.add_child(folium.Marker(location=[
              25.587993, 85.179487], popup="My Home", icon=folium.Icon(color='green')))

var.add_child(folium.Marker(location=[
              24.297101, 83.659650], popup="Stranger", icon=folium.Icon(color='red')))

for coordinates in [[23.374225, 85.440443], [22.374225, 83.440443]]:
    var.add_child(folium.Marker(location=coordinates,
                                popup="idk", icon=folium.Icon(color='black')))

for lt, ln, el in zip(lat, lon, elev):
    var_vol.add_child(folium.Marker(
        location=[lt, ln], popup=str(el) + ' m', icon=folium.Icon(color=color_prodcer(el))))

var_poly.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 9000000 else 'orange' if 9000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(var)
map.add_child(var_vol)
map.add_child(var_poly)

map.add_child(folium.LayerControl())


map.save("Map1.html")
