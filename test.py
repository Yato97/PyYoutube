from pytube import YouTube
import os
 
# on_progress_callback takes 4 parameters.
def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
    #Gets the percentage of the file that has been downloaded.
    percent = (100*(file_size-remaining))/file_size
    print("{:00.0f}% downloaded".format(percent))
 
#Grabs the file path for Download
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path
 
def start():
    print("Your video will be saved to: {}".format(file_path()))
    #Input
    yt_url = input("Copy and paste your YouTube URL here: ")
    print(yt_url)
    print ("Accessing YouTube URL...")
 
    # Searches for the video and sets up the callback to run the progress indicator.
    try:
        video = YouTube(yt_url, on_progress_callback=progress_Check)
    except:
        print("ERROR. Check your:n  -connectionn  -url is a YouTube urlnnTry again.")
        redo = start()
 
    #Get the first video type - usually the best quality.
    video_type = video.streams.filter(progressive = True, file_extension = "mp4").first()
 
    #Gets the title of the video
    title = video.title
 
    #Prepares the file for download
    print ("Fetching: {}...".format(title))
    global file_size
    file_size = video_type.filesize
    #Starts the download process
    video_type.download(file_path())
 
    print ("Ready to download another video.nn")
    again = start()
 
file_size = 0
begin = start()