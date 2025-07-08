import requests
import os
import sys
import subprocess
import time

def download_update():
    response = requests.get("https://api.github.com/repos/facufierro/Updater/releases/latest")
    data = response.json()
    download_url = data["assets"][0]["browser_download_url"]
    
    with requests.get(download_url, stream=True) as r:
        with open("app_new.exe", "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    time.sleep(2)
    os.replace("app.exe", "app_old.exe")
    os.replace("app_new.exe", "app.exe")
    os.remove("app_old.exe")
    
    subprocess.Popen(["app.exe"])

if __name__ == "__main__":
    download_update()
