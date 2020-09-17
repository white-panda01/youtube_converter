# Youtube Aud/Vid downloader

## What is it?
Written in python. It downloads Youtube Videos (in .mp4) and also converts them to an independent audio file (in .mp3) in the best found quality with only a youtube link.

## Features
* Downloads Video in .mp4 format
* Extracts only audio from the video in .mp3 format
* Downloads the best found quality.
* Limitless on the download size. (Tested with a 2hr long video)

## Anti-features
* Downloads only the best possible quality. (bigger filesize)
* Creates both .mp4 and .mp3 files. you'll need to delete a file manually as per your requirements.

## How to run
##### Setup 
    have python 3+ installed 

    clone this repo

    pip install -r requirements.txt

##### To run
    py ytmp.py <insert youtube link here>

example ```py ytmp.py https://www.youtube.com/watch?v=NIenFUckU_ieEh```

__NOTE:__ files download in the same folders as the .py file.



## Known Issues
* URL fragments contain __&__ which interfears with the links as arguments on cmd. it throws an error but in no way interferes with the whole process.
* Audio is often a few seconds longer than the original youtube video.
