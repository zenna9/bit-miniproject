import os
import branca.element
import folium
import pandas as pd
from selenium import webdriver
import webbrowser
from folium.plugins import MarkerCluster
from python.html.html_store import popup_html


free_stores = pd.read_csv("D:/files/stores_db_04v.csv", sep=',', encoding="utf-8")

text2 = free_stores['lat']
text3 = free_stores['lng']
text4 = free_stores['idx']

driver = webdriver.Chrome("D:/chromedriver.exe")
driver.get("https://mycurrentlocation.net/")

longitude = driver.find_elements_by_xpath('//*[@id="longitude"]') #Replace with any XPath
longitude = [x.text for x in longitude]
longitude = str(longitude[0])
latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
latitude = [x.text for x in latitude]
latitude = str(latitude[0])
driver.quit()
# print(latitude,longitude)


map_free = folium.Map(location=[latitude, longitude], zoom_start=11)

# 현재 위치
folium.Marker(location=[latitude, longitude], icon=folium.Icon(color='red', icon='star')).add_to(map_free)

# 미니맵
# minimap = plugins.MiniMap()
# map_free.add_child(minimap)

map_free.save(os.path.join('results'))

marker_cluster = MarkerCluster().add_to(map_free)

for i in text4:
    html = popup_html(int(i), free_stores)
    iframe = branca.element.IFrame(html=html)
    popup = folium.Popup(folium.Html(html, script=True))
    j = free_stores.index[free_stores['idx'] == int(i)].tolist()
    lat = free_stores['lat'].iloc[j[0]]
    lng = free_stores['lng'].iloc[j[0]]
    free = folium.Marker([lat, lng],
                         popup=popup).add_to(marker_cluster)

output_file = 'C:/Users/bit/PycharmProjects/freefood/python/maps/stores_map.html'
map_free.save(output_file)
webbrowser.open(output_file, new=2)

# C:/Users/bit/PycharmProjects/freefood/python/maps/stores_map.html

