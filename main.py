import geopandas as g
import folium

landlot = g.read_file('/shapes/земельные_участки.shp')
windbreak = g.read_file('/shapes/лесосполосы.shp')
roads = g.read_file('/shapes/дороги_полевые.shp')
field_roads = g.read_file('/shapes/дороги_асфальтированные.shp')
borders = g.read_file('/shapes/границы.shp')
wood= g.read_file('/shapes/древесная.shp')
another_lot = g.read_file('/shapes/прочие земли.shp')
hayfields = g.read_file('/shapes/сенекосы.shp')

map = folium.Map(
    location=[54.13750, 73.61010],
    # tiles = 'http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}',
    # attr='a href="https://www.leventhalap.org/">Leventhal Map & Education Center at the Boston Public Library</a>',
    zoom_start = 12,
    width = 1000, height = 800,
)

folium.GeoJson(
  landlot.to_json(),
  name='Земельные участки'
).add_to(map)

folium.GeoJson(
  windbreak.to_json(),
  name='Лесосполосы'
).add_to(map)

folium.GeoJson(
  roads.to_json(),
  name='Дороги полевые'
).add_to(map)

folium.GeoJson(
  field_roads.to_json(),
  name='Дороги асфальтированные'
).add_to(map)

folium.GeoJson(
  borders.to_json(),
  name='Границы'
).add_to(map)

folium.GeoJson(
  wood.to_json(),
  name='Древесная'
).add_to(map)

folium.GeoJson(
  another_lot.to_json(),
  name='Прочие земли'
).add_to(map)

folium.GeoJson(
  hayfields.to_json(),
  name='Сенекосы'
).add_to(map)

folium.TileLayer('OpenStreetMap').add_to(map)
folium.TileLayer(
    tiles='https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg',
    attr='Map tiles by <a href="http://stamen.com">Stamen Design</a>, '
         '<a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
    name='Stamen Terrain'
).add_to(map)

folium.TileLayer(
    tiles='https://stamen-tiles.a.ssl.fastly.net/toner/{z}/{x}/{y}.png',
    attr='Map tiles by <a href="http://stamen.com">Stamen Design</a>, '
         '<a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
    name='Stamen Toner'
).add_to(map)

folium.TileLayer(
    tiles='https://stamen-tiles.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.jpg',
    attr='Map tiles by <a href="http://stamen.com">Stamen Design</a>, '
         '<a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
    name='Stamen Watercolor'
).add_to(map)

# Save the map to an HTML file

map.add_child(folium.LatLngPopup())

minimap = folium.plugins.MiniMap(toggle_display=True)
map.add_child(minimap)

folium.LayerControl().add_to(map)
folium.plugins.ScrollZoomToggler().add_to(map)
folium.plugins.MeasureControl(
  position='topleft',
  primary_length_unit='Метры',
  secondary_length_unit='Мили',
  primary_area_unit='м2',
  secondary_area_unit='acres'
  ).add_to(map)


map.save('map.html')