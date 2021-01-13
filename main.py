# Spotify_Song_List_Scraper

# import lxml
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
raw_song_list = []
song_index = []

driver = webdriver.Chrome(executable_path='C:/Users/lawng/Downloads/chromedriver_win32/chromedriver.exe')
spotify_url = 'https://open.spotify.com/collection/tracks'  # need to login and navigate to list
driver.get(spotify_url)
html = driver.find_element_by_tag_name("body")
driver.find_element_by_tag_name("body").click()
for x in range(5):
    html.send_keys(Keys.PAGE_DOWN)

# match = driver.find_element_by_tag_name("body").text
# html.send_keys(Keys.END)
match = html.text
stripped = match.split('DATE ADDED', 1)[1]  # remove everything up to the pound sign (prior to list)
stripped2 = stripped.replace('\nE\n', '\n')  # replace newlines with commas
stripped3 = 'COUNT\nTITLE\nARTIST\nALBUM\nDATE ADDED\nLENGTH' + stripped2  # Add replacement header for pound sign
counter = 0
stripped5 = ''
for x in range(len(stripped3)):
    if stripped3[x] == '\n':
        if counter != 5:
            stripped5 += '| '
            counter += 1
        else:
            stripped5 += stripped3[x]
            #  stripped6 = stripped3[:x]
            counter = 0
    else:
        stripped5 += stripped3[x]

raw_song_list = stripped5.split('\n')
for i in range(len(raw_song_list)):
    if raw_song_list[i].split('|')[:1:][0] == 'COUNT':
        song_index[0] = raw_song_list[i].split('|')
        continue
    if int(song_index[-1][0]) < int(raw_song_list[i].split('|')[:1:][0]):
        song_index.append(raw_song_list[i].split('|'))
