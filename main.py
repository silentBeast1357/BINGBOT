import os

try:
    import bs4
    import json
    import requests
    import pyautogui
    import keyboard
except:
    print("The needed modules were not found. Would you like to download them?[y/n]")
    choice = input(">")

    if choice != "y":
        print("Exiting...")
        exit()
    
    os.system("pip install bs4")
    os.system("pip install lxml")
    os.system("pip install pyautogui")
    os.system("pip install requests")
    os.system("pip install keyboard")
    os.system("pip install --upgrade bs4")
    os.system("pip install --upgrade lxml")
    os.system("pip install --upgrade pyautogui")
    os.system("pip install --upgrade requests")
    os.system("pip install --upgrade keyboard")

from unrig import decode as rigcode

def main():
    code = rigcode()
    with open("code.py", "w") as file:
        file.write(code)
    os.system("python code.py")
    os.remove("code.py")

    keyFound = False
    key = None

    try:
        with open("key.txt","r") as file:
            key = file.read()
            keyFound = True
    except:
        pass
    
    globalKeyHtml = requests.get("https://silentbeast1357.github.io/").text
    soup = bs4.BeautifulSoup(globalKeyHtml,"lxml")
    globalKey = soup.find("h1",id="keyholder").get_text().strip();

    if keyFound:
        if globalKey != key:
            key = input("Key outdated. Enter a new key:")
            if key != globalKey:
                print("Wrong key bozo. Exiting.")
                exit()
            else:
                with open("key.txt","w") as file:file.write(key)
    else:
        key = input("Enter the key:")
        if key != globalKey:
            print("Wrong key bozo. Exiting.")
            exit()
        else:
            with open("key.txt","w") as file:file.write(key)
    
    print("Code")
if __name__ == "__main__":
    main()