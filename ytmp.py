import os
import sys

import pafy
from moviepy.editor import * 

def downloadVid(url):
    try:
        video = pafy.new(url)
        fileName = video.title

        best_vid = video.getbest()
        best_vid.download()

        return fileName
    except Exception as e:
        print(e)


def mp4_mp3(file_name):
    try:
        # removes all illegal filename characters 
        fileName = file_name.replace("\"", "_").replace("/", "").replace("\\", "").replace("?", "").replace(":", "").replace("*", "").replace("<", "").replace(">", "").replace("|", "")
        MP4_FILE = fileName + '.mp4'
        MP3_FILE = fileName + '.mp3'
        f = open(MP3_FILE, 'w').close()

        vclip = VideoFileClip(MP4_FILE)
        aclip = vclip.audio
        aclip.write_audiofile(MP3_FILE)

        print('Your files downloaded at {}'.format(os.getcwd()))

        vclip.close()
        aclip.close()
    except Exception as e:
        print(e)

# user arguments
args = sys.argv[1:]

# Main function
def main(args=args):
    if(args == []):
        print("""
        Invalid! enter a youtube URL
        e.g: py ytmp.py www.youtube.com/watch?v=qwerty""")

    else:
        mp4_mp3(downloadVid(args[0]))

main()

## EOF