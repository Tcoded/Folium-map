import folium
import pandas

map = folium.Map(
    location=[37.34, -121.89],
    zoom_start=7,
    titles="Stamen Terrain") #San Jose, CA

volcanoDataframe = pandas.read_csv("Volcanoes.txt")
volLat = list(volcanoDataframe["LAT"])
volLon = list(volcanoDataframe["LON"])

featG = folium.FeatureGroup(name="Volcanoes")

for lat, lon in zip(volLat, volLon):
    featG.add_child(
        folium.Marker([lat, lon],
        popup="VOLCANO",
        icon=folium.Icon(color='red')))

map.add_child(featG)

map.save("Map1.html")