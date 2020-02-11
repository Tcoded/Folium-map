import folium

map = folium.Map(
    location=[37.34, -121.89],
    zoom_start=7,
    titles="Stamen Terrain") #San Jose, CA

featG = folium.FeatureGroup(name="My Map")
featG.add_child(
    folium.Marker([37.44, -122.14],
    popup="Palo Alto, CA",
    icon=folium.Icon(color='purple')))

map.add_child(featG)

map.save("Map1.html")