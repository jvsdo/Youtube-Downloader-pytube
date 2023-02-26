from pytube import YouTube

# Create a YouTube object with the link to the video
yt = YouTube("https://youtu.be/dQw4w9WgXcQ")

# Get the first video available for streaming
streams = yt.streams.filter(only_audio=False, file_extension='mp4')

# Select the highest quality audio stream
stream = streams.order_by('abr').desc().first()

# Set the destination path for the video
destination = ""

# Download the video
stream.download(destination)
