# Exercise 4

# Create a python script able to transcode the
# input into an output with another codec that we’ve
# seen in the Theory class
import os
import subprocess


def changeCodec(inputVideo, codec):
    subprocess.call('ffmpeg -i ' + inputVideo + '.mp4 -vcodec ' + codec + ' ' + inputVideo + '_' + codec + '.mp4',
                    shell=True)

    return 'Done!'

changeCodec("bbb_10sec_video_160_120_MacBook-Air-de-Victor.local", "h264")

#It seems the conversion fail sometimes I suppose is because the 160_120 first conversion.

#Stream mapping:
#Stream  # 0:0 -> #0:0 (mpeg4 (native) -> h264 (h264_videotoolbox))
#Stream  # 0:1 -> #0:1 (aac (native) -> aac (native))

#Error initializing output stream 0:0 -- Error while opening encoder for output stream #0:0 -
# maybe incorrect parameters such as bit_rate, rate, width or height
