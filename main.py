# Spotify_Song_List_Scraper

# import lxml
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/redacted/Downloads/chromedriver_win32/chromedriver.exe')
spotify_url = 'https://open.spotify.com'  # need to login and navigate to list
driver.get(spotify_url)
match = driver.find_element_by_tag_name("body").text
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
            counter = 0
    else:
        stripped5 += stripped3[x]
