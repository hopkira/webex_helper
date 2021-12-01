import requests
import time
import psutil

def checkforprocess(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.exe().lower():             
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def checkforwebex():
    result = checkforprocess("Meeting Center.app/Contents/Helpers/webexmta.app/Contents/MacOS/webexmta")
    return result

def webex(status):
    '''
    Execute web service to start flow
    '''
    service = "webex_finish"
    base_url = 'http://octopi.local:1880/'
    if status: service = "webex_start"
    myobj = {'status': service}
    url_on = base_url + service
    requests.post(url_on, data = myobj)

while True:
    result = checkforwebex()
    webex(result)
    print(result)
    time.sleep(1)
