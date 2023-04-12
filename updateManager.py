from requests import get
from bs4 import BeautifulSoup

def CheckForUpdates():
    html_text = get("https://raw.githubusercontent.com/silentBeast1357/BINGBOT/main/main.py").text
    soup = BeautifulSoup(html_text,"lxml")
    global_main = soup.find("p").get_text().strip()

    html_text = get("https://raw.githubusercontent.com/silentBeast1357/BINGBOT/main/code").text
    soup = BeautifulSoup(html_text,"lxml")
    global_code = soup.find("p").get_text().strip()

    with open("main.py","r") as file:
        local_main = file.read()
    with open("code","r") as file:
        local_code = file.read()
    
    return local_main == global_main and local_code == global_code

def main():
    html_text = get("https://raw.githubusercontent.com/silentBeast1357/BINGBOT/main/main.py").text
    soup = BeautifulSoup(html_text,"lxml")
    global_main = soup.find("p").get_text()

    html_text = get("https://raw.githubusercontent.com/silentBeast1357/BINGBOT/main/code").text
    soup = BeautifulSoup(html_text,"lxml")
    global_code = soup.find("p").get_text()

    with open("main.py","w") as file : file.write(global_main)
    with open("code","w") as file : file.write(global_code)

if __name__ == "__main__":
    main()