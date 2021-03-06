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

        vclip.close()
        aclip.close()

        print('Your files downloaded at {}'.format(os.getcwd()))

        return MP4_FILE

    except Exception as e:
        print(e)

# user arguments
args = sys.argv[1:]

# Main function
def main(args=args):
    if(args == []):
        print("""
        Invalid! enter a youtube URL
        e.g# py ytmp.py www.youtube.com/watch?v=qwerty""")

    else:
        try:
            if(args[0] == '-a'):
                print('downloading only audio from {}'.format(args[1]))
                os.unlink(mp4_mp3(downloadVid(args[1])))
            elif(args[0] == '-v'):
                print('downloading only video from {}'.format(args[1]))
                downloadVid(args[1])
            else:
                print('downloading both audio video')
                mp4_mp3(downloadVid(args[0]))
        except:
            pass
main()
## EOF
