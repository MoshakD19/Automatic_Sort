#!/usr/bin/env python3


import schedule
import os

def main():
    schedule.every(10).seconds.do(os.system('python3 track_downloads.py'))

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=='__main__':
    main()

"""

To run in bakcground enter this in terminal:
python3 auto.py &

To find backforund process:
ps ax | grep auto

To kill background process:
kill -9 3910

To stop text showing in terminal:
nohup python3 auto.py -u &

"""
