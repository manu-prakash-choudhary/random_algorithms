from tkinter import *
import os
from PIL import *
from tkinter import filedialog
import pygame
from pygame import *
from pygame import mixer
import time
from mutagen.mp3 import MP3
from tkinter import ttk


root = Tk()
root.title('Music Player')
root.iconbitmap('C:/Project/music.ico')

pygame.mixer.init()

# length of the song 
def play_time():

    if stopped:
        return

    current_time = mixer.music.get_pos() / 1000
    
    converted_current_time = time.strftime('%H:%M:%S', time.gmtime(current_time))

    current_song = song_box.curselection()
    song = song_box.get(current_song)
    song = f'C:/Project/Songs/{song}.mp3'

    song_mut = MP3(song)
    
    global song_length

    song_length = song_mut.info.length
    converted_song_length = time.strftime('%H:%M:%S', time.gmtime(song_length))
    
    current_time +=1

    if int(slider.get()) == int(song_length):
        status_bar.config(text= f'Time Elapsed: {converted_song_length} of {converted_song_length}  ')
    
    elif paused:
        pass

    elif int(slider.get()) == int(current_time):
        slider_position = int(song_length)
        slider.config(to=slider_position, value=int(current_time))

    else:
        slider_position = int(song_length)
        slider.config(to=slider_position, value=int(slider.get()))

        converted_current_time = time.strftime('%H:%M:%S', time.gmtime(int(slider.get())))

        status_bar.config(text= f'Time Elapsed: {converted_current_time} of {converted_song_length}  ')

        next_time = int(slider.get()) +1
        slider.config(value=next_time)



    #status_bar.config(text= f'Time Elapsed: {converted_current_time} of {converted_song_length}  ')
    
    #slider.config(value=int(current_time))

    status_bar.after(1000, play_time)



# adding song to the list

def add_song():
    song = filedialog.askopenfilename(initialdir='C:/Project/Songs', title='Choose A Song', filetypes=(('mp3 Files', '*.mp3'),))
    song = song.replace('C:/Project/Songs/', '')
    song = song.replace('.mp3', '')
    song_box.insert(0, song)

# removing from list
def delete_song():
    
    stop()
    song_box.delete(ANCHOR)
    mixer.music.stop()

def delete_all_songs():
    stop()
    song_box.delete(0, END)
    mixer.music.stop()

# adding slider  
def slide(x):
    #slider_label.config(text= f' {int(slider.get())} of {int(song_length)}')
    song = song_box.get(ACTIVE)
    song = f'C:/Project/Songs/{song}.mp3'

    mixer.music.load(song)
    mixer.music.play (loops=0, start=int(slider.get()))

# Starting song 
 
def play():
    
    global stopped
    stopped = False

    song = song_box.get(ACTIVE)
    song = f'C:/Project/Songs/{song}.mp3'

    mixer.music.load(song)
    mixer.music.play (loops=0)

    play_time()
   
    slider_position = int(song_length) 
    slider.config(to=slider_position, value=0) 

global stopped
stopped = False

# stop song

def stop():
    status_bar.config(text='')
    slider.config(value=0)

    mixer.music.stop()
    song_box.select_clear(ACTIVE)

    status_bar.config(text='')

    global stopped
    stopped = True

global paused
paused = False

# pause song 

def pause(is_paused):
    global paused
    paused = is_paused
    
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        mixer.music.pause()
        paused = True

# next song

def nextsong():

    status_bar.config(text='')
    slider.config(value=0)

    next_one = song_box.curselection()
    next_one = next_one[0]+1
    song = song_box.get(next_one)
    song = f'C:/Project/Songs/{song}.mp3'

    mixer.music.load(song)
    mixer.music.play (loops=0)

    song_box.select_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one)

# previous song

def previoussong():

    status_bar.config(text='')
    slider.config(value=0)

    next_one = song_box.curselection()
    next_one = next_one[0]-1
    song = song_box.get(next_one)
    song = f'C:/Project/Songs/{song}.mp3'

    mixer.music.load(song)
    mixer.music.play (loops=0)

    song_box.select_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one)





song_box = Listbox(root, bg='black', fg='red',  width=60, selectbackground='yellow', font=('Leauge Spartan',25), selectforeground='black')
song_box.pack(pady=20)

previous_btn_img = PhotoImage(file='C:/Project/previous.png')
next_btn_img = PhotoImage(file='C:/Project/next.png')
play_btn_img = PhotoImage(file='C:/Project/start.png')
pause_btn_img = PhotoImage(file='C:/Project/pp.png')
stop_btn_img = PhotoImage(file='C:/Project/stop.png')

controls_frame = Frame(root)
controls_frame.pack()

previous_button = Button(controls_frame, image=previous_btn_img , borderwidth=0, command=previoussong)
next_button = Button(controls_frame, image=next_btn_img , borderwidth=0, command=nextsong)
play_button = Button(controls_frame, image=play_btn_img , borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img , borderwidth=0, command= lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img , borderwidth=0, command=stop)

previous_button.grid(row = 0, column=1, padx=10)
next_button.grid(row = 0, column=5, padx=10)
play_button.grid(row = 0, column=2, padx=10)
pause_button.grid(row = 0, column=3, padx=10)
stop_button.grid(row = 0, column=4, padx=10)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label= 'Add Songs', menu=add_song_menu)
add_song_menu.add_command(label= 'Add One song to the playlist', command=add_song)

remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label='Remove Songs', menu=remove_song_menu)
remove_song_menu.add_command(label='Delete a song from the playlist', command=delete_song)
remove_song_menu.add_command(label='Clear the playlist', command=delete_all_songs)

status_bar = Label(root, text = '', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

slider = ttk.Scale(root, from_ = 0, to=100, orient=HORIZONTAL, value=0, command=slide, length=650)
slider.pack(pady=30)

root.mainloop()
