import yt_dlp
import imageio_ffmpeg
from pathlib import Path
print("=" * 30)
while True:
    print("Choose a format");Format = input("\t1. MP4 (Video)\n\t2. MP3 (Audio)\n")
    if Format == "1":
        downloads = Path.home() / "Videos"
        downloads.mkdir(parents=True, exist_ok=True)
        choice = True
        while choice == True:
                    height = int(input("Quality:\n\t1. 480p (Low)\n\t2. 720p60 (HD)\n\t3. 1080p60 (FHD)\n"))
                    if height == 1:
                        height = 480
                        choice = False
                    elif height == 2:
                        height = 720
                        choice = False
                    elif height == 3:
                        height = 1080
                        choice = False
                    else:
                        print("Choose a quality")
                        print("=" * 30)
        print("=" * 30)
        url = input("Youtube URL: ")
        yt_dlp.YoutubeDL({
            "format": f"bestvideo[ext=mp4][height<={height}]+bestaudio/best[ext=mp4][height<={height}]",
            "merge_output_format": "mp4",
            "ffmpeg_location": imageio_ffmpeg.get_ffmpeg_exe(),
            "outtmpl": str(downloads / "%(title)s.%(ext)s"),
        }).download([url])
    elif Format == "2":
        downloads = Path.home() / "Music"
        downloads.mkdir(parents=True, exist_ok=True)
        choice = True
        while choice == True:
            kbps = int(input("Quality:\n\t1. 64kbps (Low)\n\t2. 128kbps (High)\n\t3. 192kbps (Best)\n"))
            if kbps == 1:
                kbps = 64
                choice = False
            elif kbps == 2:
                kbps = 128
                choice = False
            elif kbps == 3:
                kbps = 192
                choice = False
            else:
                print("Choose a quality")
                print("=" * 30)
        url = input("Youtube URL: ")
        yt_dlp.YoutubeDL({
            "format": "bestaudio/best",
            "writethumbnail": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": kbps,
                },
                {
                    "key": "FFmpegThumbnailsConvertor",
                    "format": "jpg",
                },
                {
                    "key": "FFmpegMetadata",
                },
                {
                    "key": "EmbedThumbnail",
                },
            ],
            "ffmpeg_location": imageio_ffmpeg.get_ffmpeg_exe(),
            "outtmpl": str(downloads / "%(uploader)s - %(title)s.%(ext)s"),
        }).download([url])