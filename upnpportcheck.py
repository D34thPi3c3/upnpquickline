import schedule
import time
import os

def job():
    try:
        statusPort= os.system("upnpc -v vlan2 -u http://192.168.0.1/RootDevice.xml -l | grep -i 'TeamSpeakDefault' | wc -l")
        if statusPort == "0":
            print("Port ist nicht frei gegeben")
        elif statusPort == "1":
            print("Port ist frei gegeben")
        else:
            print(statusPort)
    except:
        print("OS abfrage funktioniert nicht")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
