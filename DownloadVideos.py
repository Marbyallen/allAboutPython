from pytube import YouTube
from pytube import Playlist

import os
from pathlib import Path

# download videos inside the playlist

def DownloadVideosFromPlaylist(link):
    p = Playlist(link)
    #change directory where you going to redirect the downloads
    myfolder_path = 'Downloads/'
    path_to_download_folder = str(os.path.join(Path.home(), myfolder_path))
    
    try:
        print(f'Downloading: {p.title}')
        # getting the urls from each video inside the playlist
        for url in p.video_urls:
            youtubeObject = YouTube(url)
            video = youtubeObject.streams.get_highest_resolution()
            
            print("Downloading..... ", youtubeObject.title)
            video.download(path_to_download_folder)
        print('All videos on the playlist has been downloaded successfully.')    
    except:
        print("An error has occurred")

#Download single video
def Download(link):
    youtubeObject = YouTube(link)
    myfolder_path = 'Downloads/'
    path_to_download_folder = str(os.path.join(Path.home(), myfolder_path))
    try:
        print("Downloading..... ", youtubeObject.title)
        video = youtubeObject.streams.get_highest_resolution()
        video.download(path_to_download_folder)
    except:
        print("An error has occurred")
    print("Download is completed successfully")

#   get video thumbnail
def GetThumbnail(link):
    youtubeObject = YouTube(link)
    try:
        print("Thumbnail url: ", youtubeObject.thumbnail_url)
    except:
        print("An error has occurred")

#download audio only
def DownloadAudio(link):
    youtubeObject = YouTube(link)
    
    myfolder_path = 'Downloads/'
    path_to_download_folder = str(os.path.join(Path.home(), myfolder_path))

    print('Downloading...',youtubeObject.title)
    stream = youtubeObject.streams.get_by_itag(251)
    stream.download(path_to_download_folder)
    print('Download Successfully')

#Main
#pytube documentation:
#https://pytube.io/en/latest/index.html
#pytube github repo
#https://github.com/pytube/pytube

#Function 1: Dowload entire videos from the playlist
#initialize playlist link:
playListLink = ''   #insert link inside
# DownloadVideosFromPlaylist(playListLink)


#Function 2: Download single Video
Video_link = ''
# Download(Video_link)

#Function 3: Get thumbnail of the video
#there's problem for getting the full image of the thumbnail of the video
Video_url = ''
# GetThumbnail(Video_url)

#function 4: Download audio
#details about itag: 
# https://pytube.io/en/latest/user/streams.html#filtering-streams
# https://gist.github.com/sidneys/7095afe4da4ae58694d128b1034e01e2
DownloadAudio(Video_url)