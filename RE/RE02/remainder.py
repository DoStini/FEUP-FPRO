from datetime import datetime


hour_ = datetime.now().hour
minute_ = datetime.now().minute

new_hour = hour_ + 8
new_minute = minute_ + 30

if (new_minute > 59):
    new_minute -= 60
    new_hour += 1
    
if (new_hour > 23):
    new_hour -= 24
    
if (new_minute < 10): 
    new_minute = "0" + str(new_minute)
if (new_hour < 10): 
    new_hour = "0" + str(new_hour)
print("{0}:{1}".format(str(new_hour), str(new_minute)))