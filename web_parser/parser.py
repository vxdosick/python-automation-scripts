import requests
from bs4 import BeautifulSoup

url = "https://tryscrapeme.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    print("Parsing in procces...")

    with open("parsed_data.txt", "w", encoding = "utf-8") as pd:
        h1 = soup.find("h1")
        if h1:
            pd.write("The main title: " + h1.text + "\n")
        else:
            pd.write("The main title: Not found\n")

        h2Array = soup.find_all("h2")
        pd.write("The secondary titles\n")
        if h2Array:
            for h2 in h2Array:
                pd.write(h2.text + "\n")
        else:
            pd.write("Not found\n")
    
        images = soup.find_all("img")
        pd.write("The images src and alt\n")
        if images:
            for image in images:
                pd.write(image.get("src") + " " + image.get("alt", "") + "\n")
        else:
            pd.write("Not found\n")
        
    print("Finish")
else:
    print("ERROR\nStatus: ", response.status_code)