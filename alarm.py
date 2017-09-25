import time
import os

s=0
m=0
while (s<=60):
     os.system('cls')
     print (m, 'Minutes', s, 'Seconds')
     time.sleep(1)
     s+=1
     if (s==60):
         m+=1
         s=0
     if (m==240):
             os.system('totem /home/muhammad/Downloads/alarm.mp4')
 

