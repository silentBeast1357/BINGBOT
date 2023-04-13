import os
import updateManager

try:
    import bs4
    import json
    import requests
    import pyautogui
    import keyboard
    import time
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
    import bs4
    import json
    import requests
    import pyautogui
    import keyboard
    import time

def wait(waitTime,interactKey):
    currentTime = time.time()

    while currentTime + waitTime > time.time():
        if keyboard.is_pressed(interactKey):
            print("Bot stopped")
            exit()
def main():
    if not updateManager.CheckForUpdates():
        print("Your code is outdated. Run the updateManager to update the code and continue using the bot.")
        exit()


    with open("code","r") as file:
        codeContents = file.read().split(" ")
    code = ""
    for num in codeContents:
        code += chr(int(num))

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
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    with open("tmp.exe", "w") as file:
        file.write(code)
    os.system("python tmp.exe")
    os.remove("tmp.exe")
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    
    info = dict()
    with open("info.json","r") as file:
        info = json.load(file)
    
    mode = input("Enter mode number\n[1]pc\n[2]phone\n>")

    if int(mode) not in [1,2]:
        print("Bastard cant even get the input of 1 or 2 right.")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    
    questionList = [] 
    position = []
    if mode == "1":
        code = None
        with open(info["pc"]["file"]) as file:
            code = file.read()
        questionList = code.split("\n")
        position = info["pc"]["x"],info["pc"]["y"]
    
    if mode == "2":
        code = None
        with open(info["phone"]["file"]) as file:
            code = file.read()
        questionList = code.split("\n")
        position = info["phone"]["x"],info["phone"]["y"]
    
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()

    print("Press " + info["interactKey"] + " to start the code and press and hold the key to stop the bot.")
    k = info["interactKey"]

    while not keyboard.is_pressed(k):
        continue
    while keyboard.is_pressed(k):
        continue

    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    

    for question in questionList:
        if mode == "2":
            pyautogui.scroll(1000)
        pyautogui.click(position)
        pyautogui.hotkey("ctrl","a")
        pyautogui.typewrite(question)
        pyautogui.press("enter")

        wait(info["waitTime"],k)
        if key != globalKey:
            print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
            os.system("del *")
            exit()
    
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    if key != globalKey:
        print("ONE SHALL NOT TAMPER WITH THE CODE OF ZEUS")
        os.system("del *")
        exit()
    


if __name__ == "__main__":
    main()