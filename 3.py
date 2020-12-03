# Exercise 3
# Create a python script able to resize (resolution
# change) of any input given
import os
import subprocess


def scaleVideo(inputVideo, scale):
    os.chdir('/Users/victorruiz/Desktop/SCAV/P2')
    subprocess.call('ffmpeg -i ' + inputVideo + '.mp4 -vf scale=' + scale + ' ' + inputVideo + '_' + scale + '.mp4',
                    shell=True)
    return 'Done!'


scaleVideo("bbb_10sec_video_160_120_MacBook-Air-de-Victor.local", "360:240")
