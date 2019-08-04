import  folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])
name = list(data["NAME"])


def get_color(elevation):
    """
    get a string of color for the elevation value that is received.
    """
    if elevation<1000:
        return 'green'
    elif elevation>1000 and elevation<3000:
        return 'orange'
    return 'red'

map = folium.Map(location=(38,-99),zoom_start=4)
Volcanoes_group=folium.FeatureGroup(name="Volcanoes")

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    Volcanoes_group.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe),fill_color=get_color(el),color='gery',fill_opacity=0.7))

Population_group=folium.FeatureGroup(name="Population")

json_data=open('world.json','r',encoding='utf-8-sig').read()
Population_group.add_child(folium.GeoJson(data=json_data,
                               style_function=lambda  x: {'fillColor':'green' if x['properties']['POP2005']<1000000
                               else 'orange' if 1000000 <= x['properties']['POP2005']<2000000 else 'red'}))

map.add_child(Volcanoes_group)
map.add_child(Population_group)
map.add_child(folium.LayerControl())
map.save("map1.html")






