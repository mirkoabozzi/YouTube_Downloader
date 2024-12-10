import yt_dlp
import os
import argparse

def downloader(url, outputType="mp4"):
    try:
        download_path = os.path.join(os.getcwd(), "downloads")
        os.makedirs(download_path, exist_ok=True)

        options = {
            "outtmpl": os.path.join(download_path, "%(title)s.%(ext)s"),
            "format": "bestvideo[vcodec^=avc1][height<=1080]+bestaudio[acodec^=mp4a]/best",
            "nocheckcertificate": True,
        }

        if outputType == "mp3":
            options.update({
                "format": "bestaudio/best",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }],
            })

        with yt_dlp.YoutubeDL(options) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get("title", None)
            print(f"Scaricato: {video_title}")
    except Exception as e:
        print(f"Errore nel download: {e}")

# if __name__ == "__main__":
#     parse = argparse.ArgumentParser()
#     parse.add_argument("url", help="URL del video")
#     parse.add_argument("-t", "--tipo", choices=["mp3", "mp4"], default="mp4", help="Formato di output (mp3 o mp4)")
#     args = parse.parse_args()

#     downloader(args.url, args.tipo)


message = input("Inserisci URL: ")
type = input("Inserisci mp3 per audio lascia il campo vuoto per video: ")

downloader(message, type)