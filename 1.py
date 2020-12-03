#Exercise 1
#Create a python script able to parse the ‘ffmpeg –
#i BBB.mp4’ file, which can mark at least 3 relevant
#data from the container

import os
import subprocess
os.chdir('/Users/victorruiz/Desktop/SCAV/P2')

subprocess.call('ffprobe -v quiet -print_format json -show_format -show_streams bbb_original_video.mp4',shell=True)

#podemos printear el .json con los datos + relevantes del container