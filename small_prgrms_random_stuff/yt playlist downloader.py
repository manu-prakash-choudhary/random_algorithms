"""
import pytube
#from pytube import YouTube
link = pytube.YouTube("https://www.youtube.com/watch?v=50VNCymT-Cs&list=PL_WhjjTlhY7AmjY2RcAGcktTcJvkKgkmf&ab_channel=AlecBenjamin")

link.streams.filter(only_audio=True, subtype='webm', abr='160kbps').first().download('E:/')

yt = pytube.YouTube("https://www.youtube.com/watch?v=pFX65YC4u2Y")
stream = yt.streams.filter(subtype="mp4")
stream.get_by_resolution("240p").download()
"""


import os
from pytube import YouTube

import requests
import re



#imp functions


def foldertitle(url):

    try:
        res = requests.get(url)
    except:
        print('no internet')
        return False

    plain_text = res.text

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]

    else:
        print('Incorrect attempt.')
        return False

    return cPL



def link_snatcher(url):
    our_links = []
    try:
        res = requests.get(url)
    except:
        print('no internet')
        return False

    plain_text = res.text
    

    if 'list=' in url:
        eq = url.rfind('=') + 1
        
        cPL = url[eq:]
    
    else:
        print('Incorrect Playlist.')
        return False

    tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
    mat = re.findall(tmp_mat, plain_text)
    print(mat)
    for m in mat:
        new_m = m.replace('&amp;', '&')
        work_m = 'https://youtube.com/' + new_m
        if work_m not in our_links:
            our_links.append(work_m)

    print(our_links)
    return our_links


BASE_DIR = os.getcwd()



url = "https://youtube.com/playlist?list=PL_WhjjTlhY7DtbDbMkTZMUfEs44n2eACK"

print('\nCHOOSE ANY ONE - TYPE 360P OR 720P\n')
user_res = str(input())


print('...You choosed ' + user_res + ' resolution\n.')

our_links = link_snatcher(url)

os.chdir(BASE_DIR)

new_folder_name = foldertitle(url)
print(new_folder_name[:7])

try:
    os.mkdir(new_folder_name[:7])
except:
    print('folder already exists')

os.chdir(new_folder_name[:7])
SAVEPATH = os.getcwd()
print(f'\n files will be saved to {SAVEPATH}')

x=[]
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        pathh = os.path.join(root, name)

        
        if os.path.getsize(pathh) < 1:
            os.remove(pathh)
        else:
            x.append(str(name))


print('\nconnecting . . .\n')


print()

for link in our_links:
    
    try:
        yt = YouTube(link)
        main_title = yt.title
        main_title = main_title + '.mp4'
        main_title = main_title.replace('|', '')
        
    except:
        print('connection problem..unable to fetch video info')
        break

    
    if main_title not in x:

        
        if user_res == '360p' or user_res == '720p':
            vid = yt.streams.filter(progressive=True, file_extension='mp4', res=user_res).first()
            print('Downloading. . . ' + vid.default_filename + ' and its file size -> ' + str(round(vid.filesize / (1024 * 1024), 2)) + ' MB.')
            vid.download(SAVEPATH)
            print('Video Downloaded')
        else:
            print('something is wrong.. please rerun the script')


    else:
        print(f'\n skipping "{main_title}" video \n')
    
print(' downloading finished')
print(f'\n all your videos are saved at --> {SAVEPATH}')