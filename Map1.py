import folium
import pandas

map = folium.Map(
    location=[37.34, -121.89], #San Jose, CA
    zoom_start=7,
    tiles="Stamen Terrain") 

volcanicDataframe = pandas.read_csv("Volcanoes.txt")
volName = list(volcanicDataframe["NAME"])
volLat = list(volcanicDataframe["LAT"])
volLon = list(volcanicDataframe["LON"])
volElev = list(volcanicDataframe["ELEV"])

featG = folium.FeatureGroup(name="Volcanoes")

for name, lat, lon, elev in zip(volName, volLat, volLon, volElev):
    iframe = folium.IFrame(
        html=f"<a href='https://www.google.com/search?q=%22{name}%22'"
        f"target='_blank'>{name}</a>"
        f"<br>"
        f"{elev} m",
        width=200,
        height=100)
    featG.add_child(
        folium.Marker([lat, lon],
        popup=folium.Popup(iframe),
        icon=folium.Icon(color='red')))

map.add_child(featG)

map.save("Map1.html")