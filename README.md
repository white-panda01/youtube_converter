# Youtube Aud/Vid downloader

## About
This script allows you to download Youtube Video in *.mp4* and convert them into an independent audio file in *.mp3* in the best found quality with just a YouTube link.

## Features
* Downloads Video in .mp4 format
* Extracts only audio in .mp3 format
* Downloads the best found quality.
* Limitless on the download size. *Tested with a 2hr long video*

## Anti-features
* Downloads only the best possible quality. *bigger filesize*.

## How to run
#### Setup 
    have python 3+ installed 

    clone this repo

    pip install -r requirements.txt

#### To run
###### Download both audio & video
    py ytmp.py <insert youtube link here> #Default
###### Download audio only
    py ytmp.py -a <insert youtube link here>
###### Download video only
    py ytmp.py -v <insert youtube link here>

example:
```py ytmp.py https://www.youtube.com/watch?v=NIenFUckU_ieEh```

__NOTE:__ files download in the same folders as the .py file.

## Known Issues
* URL fragments contain __&__ which interfears as a conditional command on cmd. __It throws an error but in no way interferes with the process.__
* Audio is often a few seconds longer than the original youtube video.
