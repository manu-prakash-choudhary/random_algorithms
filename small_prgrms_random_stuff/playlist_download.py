from selenium import webdriver
import time 
import youtube_dl 
import os


url = input("Enter the Youtube Playlist URL : ")
driver = webdriver.Chrome() 
driver.get(url)
time.sleep(5)

playlist=[]
videos=driver.find_elements_by_class_name('style-scope ytd-playlist-video-renderer')


for video in videos:
    link=video.find_element_by_xpath('.//*[@id="content"]/a').get_attribute("href")
    end=link.find("&")
    link=link[:end]
    playlist.append(link)

"""
For example, a playlist with 6 videos

Enter youtube playlist link : https://www.youtube.com/playlist?list=PLGzz7pyosmlJfx9ivigemSouoZR9uLT2-
['https://www.youtube.com/watch?v=iyL9-EE3ngk&list=PLGzz7pyosmlJfx9ivigemSouoZR9uLT2-&index=1', 'https://www.youtube.com/watch?v=G7E8YrOiYrQ&list=PLGzz7pyosmlJfx9ivigemSouoZR9uLT2-&index=2', 'https://www.youtube.com/watch?v=79D4Y1cUK7I&list=PLGzz7pyosmlJfx9ivigemSouoZR9uLT2-&index=3', 'https://www.youtube.com/watch?v=MUe0FPx8kSE&list=PLGzz7pyosmlJfx9ivigemSouoZR9uLT2-&index=4', 'https://www.youtube.com/watch?v=UkpmjbHYV0Y&list=PLGzz7pyosmlJfx9ivigemSouoZR9uLT2-&index=5', 'https://www.youtube.com/watch?v=WTOFLmB9ge0&list=PLGzz7pyosmlJfx9ivigemSouoZR9uLT2-&index=6']
"""

os.chdir('C:/Users/choud/PL_Whjj') 
ydl_opts = {}
for link in playlist:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
driver.close()


