import os
import sys
# import youtube_dl
import time
import pyautogui
import psycopg2


def run_yt():
    # default time to run the video
    timer = 60  # default time to run the video

    db = False
    if db:
        # conn = psycopg2.connect(
        #     dbname='postgres',
        #     user='readonly_user.ihuewstpkilkxjqjewkp',
        #     password='Hello123',
        #     host='aws-0-ap-south-1.pooler.supabase.com',
        #     port='5432',
            
        # )

        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres.ihuewstpkilkxjqjewkp',
            password='manu0331',
            host='aws-0-ap-south-1.pooler.supabase.com',
            port='5432',
            
        )
        # try to connect and check if the connection is successful
        curr = None
        try:
            curr = conn.cursor()
            print("Connected to the database")
        except Exception as e:
            print("Unable to connect to the database")
            print("Error: ", e)
            pass

        # fetch the data from the database
        curr.execute("SELECT * FROM public.yt_video ORDER BY created_at DESC;")
        # data = curr.fetchall()
        # print("Data: ", data)
        # fetch latest record
        record = curr.fetchone()
        # record format: (id, created_at, Name, Link, Duration)
        print("Record: ", record)

        time_in_string = record[4]
        hour, min, sec = time_in_string.split(":")
        timer = int(hour)*3600 + int(min)*60 + int(sec)
    
        print("Time to run the video: ", timer)
        while True:
            os.system(f"start {record[3]}")
            time.sleep(timer)
            print("Video is running")    

    else:
        print("Time to run the video: ", timer)
        link = "https://www.youtube.com/watch?v=mTaq9vEpb50"
        while True:
            os.system(f"start {link}")
            time.sleep(5)
            os.system(f"start {link}")
            time.sleep(5)
            os.system(f"start {link}")
            time.sleep(5)
            print("Videos are running")
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'shift', 'a')
            time.sleep(0.5)
            # pyautogui.hotkey('down')
            # time.sleep(0.5)
            pyautogui.hotkey('down')
            time.sleep(0.5)
            pyautogui.hotkey('enter')
            time.sleep(timer)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'w')
            print("Finished")


# run the function
run_yt()
