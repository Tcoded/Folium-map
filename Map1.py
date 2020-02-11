import folium

map = folium.Map(location=[37.34, -121.89], zoom_start=7, titles="Stamen Terrain") #San Jose, CA
map.save("Map1.html")