import requests
from bs4 import BeautifulSoup
import os

img_folder = "images"
os.makedirs(img_folder, exist_ok=True)

url = "https://www.w3schools.com/css/css_image_gallery.asp"

response = requests.get(url)

if response.status_code == 200:

    print("Get html data...")
    soup = BeautifulSoup(response.text, "html.parser")
    print("Get all images...")
    images = soup.find_all("img")

    with open("images_data.txt", "w", encoding = "utf-8") as im:
        print("Start save data and download images...")

        for i, img in enumerate(images, start=1):
            img_url = img.get("src")

            if not img_url:
                continue

            if not img_url.startswith("http"):

                if not img_url.startswith("/"):
                    img_url = "/css/" + img_url

                img_url = "https://www.w3schools.com" + img_url
                
            im.write(img_url + "\n")
            print(f"Save: {img_url}")

            img_jpg = requests.get(img_url).content
            
            img_name = os.path.join(img_folder, f"{i}.jpg")

            with open(img_name, "wb") as f:
                f.write(img_jpg)
            
            print(f"Download: {img_name}")

else:
    print(f"Error\nStatus code: {response.status_code}")