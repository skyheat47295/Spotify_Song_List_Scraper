# Spotify_Song_List_Scraper

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
raw_song_list = []
song_index = [['TITLE', ' ARTIST', ' ALBUM', ' DATE ADDED', ' LENGTH']]
total_songs = 2000  # Next time will grab total songs from web scrape

driver = webdriver.Chrome(executable_path='C:/Users/redacted/Downloads/chromedriver_win32/chromedriver.exe')
spotify_url = 'https://open.spotify.com/collection/tracks'  # need to login and navigate to list
driver.get(spotify_url)  # don't forget to pause so user can login and click on the liked songs list
html = driver.find_element_by_tag_name("body")
driver.find_element_by_tag_name("body").click()

while len(song_index) < total_songs:
    match = html.text
    stripped = match.split('DATE ADDED', 1)[1]  # remove everything up to the pound sign (prior to list)
    stripped2 = stripped.replace('\nE\n', '\n')  # replace newlines with commas
    stripped3 = 'TITLE\nARTIST\nALBUM\nDATE ADDED\nLENGTH' + stripped2  # Add replacement header for pound sign
    counter = 0
    stripped5 = ''
    for x in range(len(stripped3)):
        if stripped3[x] == '\n':
            if counter != 4:
                stripped5 += '| '
                counter += 1
            else:
                stripped5 += stripped3[x]
                counter = 0
        else:
            stripped5 += stripped3[x]

    raw_song_list = stripped5.split('\n')
    for i in range(len(raw_song_list)):
        if raw_song_list[i].split('|')[:1:][0] == 'TITLE':
            continue
        if raw_song_list[i] not in song_index:
            song_index.append(raw_song_list[i])

    for x in range(3):
        html.send_keys(Keys.PAGE_DOWN)

file1 = open("C:/Users/redacted/Downloads/songs.txt", "w")
for songs in song_index:
    for record in songs:
        file1.writelines([record])
    file1.writelines('\n')
file1.close()
