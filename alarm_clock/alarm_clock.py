import time
from playsound import playsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN="\033[H"

def alarm(sec):
    timeElasped=0
    
    print(CLEAR)
    while timeElasped<sec:
        time.sleep(1)
        timeElasped+=1
        
        timeLeft= sec-timeElasped
        hourLeft=timeLeft//3600
        minLeft=timeLeft//60
        secLeft=timeLeft%60
        print(f"{CLEAR_AND_RETURN}{hourLeft:02d}:{minLeft:02d}:{secLeft:02d}")
    playsound("fanfare.mp3")

hour=int(input("How many Hours to wait "))        
minutes=int(input("How many Minutes to wait "))        
second=int(input("How many Seconds to wait "))        


totSec= minutes*60+hour*3600+second
alarm(totSec)