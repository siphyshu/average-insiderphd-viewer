import os
import requests
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

img_urls = ["https://pbs.twimg.com/media/GAwjPPvWkAMfCOE?format=jpg&name=small","https://pbs.twimg.com/media/GAwkML8W8AAaGVj?format=jpg&name=small","https://pbs.twimg.com/media/GAwkoKOXMAAUEK_?format=jpg&name=small","https://pbs.twimg.com/media/GAwlDWbWIAACUjL?format=jpg&name=small","https://pbs.twimg.com/media/GAwllZMXYAA8Gka?format=jpg&name=small","https://pbs.twimg.com/media/GAwmXYmWoAASXMU?format=jpg&name=small","https://pbs.twimg.com/media/GAwnrUoWsAAS0bi?format=jpg&name=small","https://pbs.twimg.com/media/GAwoX8UXsAEzNFJ?format=jpg&name=small","https://pbs.twimg.com/media/GAwov9ZWgAMDzLg?format=jpg&name=small","https://pbs.twimg.com/media/GAwpYynXsAAwUEl?format=jpg&name=small","https://pbs.twimg.com/media/GAwqHLsWUAAbUid?format=jpg&name=small","https://pbs.twimg.com/media/GAwsT9uXkAEsxEz?format=jpg&name=small","https://pbs.twimg.com/media/GAwsvSpWUAAIPVI?format=jpg&name=small","https://pbs.twimg.com/media/GAws6JzXIAAmPjo?format=jpg&name=small","https://pbs.twimg.com/media/GAwtp4vW4AA6ihv?format=jpg&name=small","https://pbs.twimg.com/media/GAwuXfVW8AAlU7f?format=jpg&name=small","https://pbs.twimg.com/media/GAwu59eXcAA0jC1?format=jpg&name=small","https://pbs.twimg.com/media/GAwvk3nXoAA5tRr?format=jpg&name=small","https://pbs.twimg.com/media/GAwv89rWsAAd7VF?format=jpg&name=small","https://pbs.twimg.com/media/GAwwjgcXoAAWI10?format=jpg&name=small","https://pbs.twimg.com/media/GAwyKx9XcAAbMV5?format=jpg&name=small","https://pbs.twimg.com/media/GAwyg5XW4AAszIu?format=jpg&name=small","https://pbs.twimg.com/media/GAw0G9VXoAAgstd?format=jpg&name=small","https://pbs.twimg.com/media/GAw0NP7W0AAdgDR?format=jpg&name=small","https://pbs.twimg.com/media/GAw1-fJWUAAxqQI?format=jpg&name=small","https://pbs.twimg.com/media/GAw74iiWcAEAkRl?format=jpg&name=small","https://pbs.twimg.com/media/GAw8Uh1WYAA4GBh?format=jpg&name=small","https://pbs.twimg.com/media/GAw8q-LXkAACguh?format=jpg&name=small","https://pbs.twimg.com/media/GAw9SjLXMAAHAh7?format=jpg&name=small","https://pbs.twimg.com/media/GAw9z06WAAA2WfS?format=jpg&name=small","https://pbs.twimg.com/media/GAw-IzQWoAEu9pl?format=jpg&name=small","https://pbs.twimg.com/media/GAw-cW1WAAAc69E?format=jpg&name=small","https://pbs.twimg.com/media/GAw-1YoWYAA7sXW?format=jpg&name=small"] 
usernames = ["","@thebinarybot","@Hari0mSingh22","@theshyhat","@kushagrasarathe","@MohdAsadAL","@rounak131106","@bsidesgoa","@_SteveG_","@jaighk","@Daviey","@TIE__SUN","@siphyshu","@barakadewise","@SubitusNex","@CoreyD97","@kittoh_","@CollinsMaganga","@dynohackula","@Null0x5","@ArchAngelDDay","@trobbierob","@karstetter","@ThisIsDK999","@thiagomattos105","@545ch4_","@anan7pa73l","@utkarshrai28","@hahasver","@statictear","@djchateau","@wa1tf0r_me",""][::-1]
avatars = {}
for i in range(len(img_urls)):
        avatars[str(i).zfill(3)] = {
            "img_url": img_urls[i],
            "username": usernames[i]
        }

        

def download_and_annotate_avatars(avatars, dir_path):
    for i in range(len(img_urls)):
        filename = f"{str(i).zfill(3)}.jpg"
        file_path = os.path.join(dir_path, filename)
        img_url = avatars[filename[:-4]]["img_url"]
        username = avatars[filename[:-4]]["username"]

        r = requests.get(img_url)
        with open(file_path, "wb") as f:
            f.write(r.content)
        print(f"Downloaded avatar {str(i).zfill(3)}")

        img = Image.open(file_path)
        if username != "":
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("IndieFlower-Regular.ttf", 20)
            draw.text((10, img.height-30), username, "#000000", font=font)
        img.save(file_path)
        print(f"Written {username} on avatar {str(i).zfill(3)}")



def create_video(input_folder, output_path, fps):
    input_pattern = os.path.join(input_folder, "%03d.jpg")

    ffmpeg_cmd = [
        "ffmpeg",
        "-framerate", str(fps),
        "-i", input_pattern,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",
        output_path
    ]

    subprocess.run(ffmpeg_cmd, check=True)


if __name__ == "__main__":
    dir_path = os.path.join(ROOT_DIR, "avatars")
    output_path = os.path.join(ROOT_DIR, "average_insiderphd_viewer.mp4")
    fps = 3
    download_and_annotate_avatars(avatars, dir_path)
    create_video(dir_path, output_path, fps)