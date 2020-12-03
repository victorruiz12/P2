import os
import subprocess
import socket
os.chdir('/Users/victorruiz/Desktop/SCAV/P2')

subprocess.call('ffprobe -v quiet -print_format json -show_format -show_streams bbb_original_video.mp4',shell=True)

#podemos printear el .json con los datos + relevantes del container

hostname = socket.gethostname()
#path = os.path.abspath("P2")
#os.chdir(path)

os.rename('bbb_10sec_video_160_120.mp4', 'bbb_10sec_video_160_120_' + str(hostname) + '.mp4')

os.rename('bbb_10sec_video_360_240.mp4', 'bbb_10sec_video_360_240_' + str(hostname) + '.mp4')

os.rename('bbb_10sec_video_640_480.mp4', 'bbb_10sec_video_640_480_' + str(hostname) + '.mp4')

os.rename('bbb_10sec_video_1280_720.mp4', 'bbb_10sec_video_1280_720_' + str(hostname) + '.mp4')

def scaleVideo(inputVideo, scale):
    os.chdir('/Users/victorruiz/Desktop/SCAV/P2')
    subprocess.call('ffmpeg -i ' + inputVideo + '.mp4 -vf scale=' + scale + ' ' + inputVideo + '_' + scale + '.mp4',
                    shell=True)
    return 'Cambio de escala DONE!'
def changeCodec(inputVideo, codec):
    subprocess.call('ffmpeg -i ' + inputVideo + '.mp4 -vcodec ' + codec + ' ' + inputVideo + '_' + codec + '.mp4',
                    shell=True)

    return 'Cambio de codec DONE!'

#changeCodec("bbb_10sec_video_160_120_MacBook-Air-de-Victor.local", "h264")
#scaleVideo("bbb_10sec_video_160_120_MacBook-Air-de-Victor.local", "360:240")