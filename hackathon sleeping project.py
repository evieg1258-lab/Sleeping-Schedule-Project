import time
import datetime
print("Let's set up your sleep schedule")
print("When do you want to start sleeping? (ex 10:00 or 09:30)")
answer=input()
h,m=map(int,answer.split(":"))
sleep=datetime.time(hour=h,minute=m)
#Just in case:
if m==60:
    h+=1
    m=0
    print("There are only 60 minutes in an hour")
elif m>60:
    m=59
if m<0:
    m=00
    print("There aren't negative minutes")
if h>=24:
    h=0
    print("There are 24 hours in a day")
if h<0:
    h=00
    print("There aren't negative hours")
#Setting times   
print("When do you want your reminder? (ex 9:50)")
r=input()
h1,m1=map(int,r.split(":"))
reminder=datetime.time(hour=h1,minute=m1)
print("You're all set!")
print("You can always change the time by resetting the code")
#To see the time
sleeping=False
once=True
once2=True
once3=True
mins=0
hours=0
#track=time.time()
while True:
    if sleeping==True:
        if once2==True:
            print("If you would like to see how much you slept,")
            print("the time is displayed below every minute")
            once2=False
        if time.time()-track>=60:
            mins+=1
            track=time.time()
            if mins==60:
                mins=0
                hours+=1
            print(hours,"hour(s) :",mins,"minute(s)")
    else:
        current=datetime.datetime.now().time()
        #print(current)
        if (current.hour>reminder.hour or (current.hour==reminder.hour and current.minute>=reminder.minute)) and once==True:
            print("Time to sleep")
            once=False
        if (current.hour>sleep.hour or (current.hour==sleep.hour and current.minute>=sleep.minute)) and once3==True:
            print("Sleep mode is on")
            sleeping=True
            track=time.time()
            once3=False
    time.sleep(1)
