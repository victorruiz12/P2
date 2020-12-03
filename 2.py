#Exercise 2
#Create a python script able to rename the 5
#quality outputs of the BBB that you did in last
#seminar

import os
import subprocess
import socket

hostname = socket.gethostname()
#path = os.path.abspath("P2")
#os.chdir(path)

os.rename('bbb_10sec_video_160_120.mp4', 'bbb_10sec_video_160_120_' + str(hostname) + '.mp4')

os.rename('bbb_10sec_video_360_240.mp4', 'bbb_10sec_video_360_240_' + str(hostname) + '.mp4')

os.rename('bbb_10sec_video_640_480.mp4', 'bbb_10sec_video_640_480_' + str(hostname) + '.mp4')

os.rename('bbb_10sec_video_1280_720.mp4', 'bbb_10sec_video_1280_720_' + str(hostname) + '.mp4')